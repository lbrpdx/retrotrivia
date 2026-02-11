# Simple Quiz Game Engine in PyGame
# for Batocera Retrotrivia
# lbrpdx - 2020-2026
# https://github.com/lbrpdx/retrotrivia
# License: LGPL 3.0
import pygame
import subprocess
import os
import signal

FFMPEG_BIN       = '/usr/bin/ffmpeg'   # Full path to ffmpeg executable
TMP_AUDIO_FILE   = '/tmp/retrotrivia_audio.wav'

#######################################
### Video to PyGame converter
class VideoSprite(pygame.sprite.Sprite):
    def __init__(self, rect, filename, sound_manager, mode, FPS=20):
        pygame.sprite.Sprite.__init__(self)
        commandvideo = [ FFMPEG_BIN,
                '-loglevel', 'quiet', '-nostdin',
                '-i', filename,
                '-f', 'image2pipe',
                '-s', '%dx%d' % (rect.width, rect.height),
                '-r', '%d' % FPS,
                '-pix_fmt', 'rgb24',
                '-vcodec', 'rawvideo',
                '-' ]
        commandaudio = [ FFMPEG_BIN,
                '-loglevel', 'quiet', '-nostdin', '-y',
                '-i', filename, '-vn',
                '-c:a', 'pcm_s16le',
                '-b:a', '128k',
                '-r', '%d' % FPS,
                TMP_AUDIO_FILE ]
        self.bytes_per_frame = rect.width * rect.height * 3

        # Start video ffmpeg as subprocess; we must terminate this later
        self.procvideo = subprocess.Popen(
            commandvideo,
            stdout=subprocess.PIPE,
            bufsize=self.bytes_per_frame * 3
        )

        # Audio: blocking call is fine; it exits when extraction is done
        try:
            os.remove(TMP_AUDIO_FILE)
        except FileNotFoundError:
            pass
        except Exception:
            pass

        # Note: subprocess.call returns an exit code, not a process
        self.procaudio_return = subprocess.call(
            commandaudio,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        self.image  = pygame.Surface((rect.width, rect.height), pygame.HWSURFACE)
        self.rect   = self.image.get_rect()
        self.rect.x = rect.x
        self.rect.y = rect.y

        # Used to maintain frame-rate
        self.last_at     = 0              # time frame starts to show
        self.frame_delay = int(1000 / FPS)

        # audio playback
        if os.path.isfile(TMP_AUDIO_FILE):
            sound_manager.play(TMP_AUDIO_FILE, 800)

        # video control
        self.video_stop = False
        self.eof        = False
        self.last_image = None

        # effect mode
        self.mode       = mode
        self.coeff      = 2  # how slow you want to un-pixellate
        self.time_start = pygame.time.get_ticks()

    def _kill_proc(self):
        if self.procvideo is None:
            return
        try:
            # First, ask politely
            if self.procvideo.poll() is None:
                self.procvideo.terminate()
                try:
                    self.procvideo.wait(timeout=0.5)
                except subprocess.TimeoutExpired:
                    # Still alive? Kill it.
                    self.procvideo.kill()
                    self.procvideo.wait()
        except Exception:
            # Best-effort cleanup; ignore errors
            pass
        finally:
            try:
                if self.procvideo.stdout:
                    self.procvideo.stdout.close()
            except Exception:
                pass
            self.procvideo = None

    def stop(self):
        self.video_stop = True
        self._kill_proc()

    def __del__(self):
        # Safety net in case stop() was never called
        self._kill_proc()

    def update(self, timer, tmax):
        if self.video_stop or self.eof:
            # Show last frame if available, but don't read from ffmpeg anymore
            if self.last_image is not None:
                self.image = self.last_image
            return

        if self.procvideo is None:
            # Process already dead / cleaned up
            return

        time_now = pygame.time.get_ticks()
        if time_now <= self.last_at + self.frame_delay:
            return

        self.last_at = time_now

        try:
            raw_image = self.procvideo.stdout.read(self.bytes_per_frame)
            # EOF or short read: stop the video and clean up ffmpeg
            if not raw_image or len(raw_image) < self.bytes_per_frame:
                self.eof = True
                self._kill_proc()
                return

            img_temp = pygame.image.frombuffer(
                raw_image,
                (self.rect.width, self.rect.height),
                'RGB'
            )
            self.last_image = img_temp

            if self.mode == "pixelated":
                if timer > 3:
                    mmax = max(timer, tmax)
                    px = pow(2, int((mmax - timer + 1) / self.coeff))
                    py = pow(2, int((mmax - timer + 1) / self.coeff))
                    if (px, py) < (self.rect.width, self.rect.height):
                        img_temp = pygame.transform.scale(img_temp, (px, py))
                self.image = pygame.transform.scale(
                    img_temp,
                    (self.rect.width, self.rect.height)
                )

            elif self.mode == "rotated":
                angle = (180 - (time_now - self.time_start) / 20) % 360
                rotated = pygame.transform.rotate(img_temp, angle).convert_alpha()
                (x, y) = self.rect.center
                rotated = pygame.transform.scale(
                    rotated,
                    (self.rect.width, self.rect.height)
                ).convert_alpha()
                self.image = rotated
                self.rect = self.image.get_rect()
                self.rect.center = (x, y)

            elif self.mode == "zoom":
                (x, y) = self.rect.center
                ttime = (time_now - self.time_start) / 1000.0
                htime = min(ttime, tmax)
                hx = max(0, x * (1 - htime / tmax))
                hy = max(0, y * (1 - htime / tmax))
                rct = pygame.Rect(
                    hx,
                    hy,
                    self.rect.width * htime / tmax,
                    self.rect.height * htime / tmax
                )
                sub = img_temp.subsurface(rct)
                self.image = pygame.transform.scale(
                    sub,
                    (self.rect.width, self.rect.height)
                ).convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.center = (x, y)

            else:
                # regular
                self.image = img_temp

        except Exception as e:
            # Any error while reading from pipe -> assume EOF / broken pipe
            print(f"Videoplayer running: error {e}")
            self.eof = True
            self._kill_proc()

