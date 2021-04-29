# Simple Quiz Game Engine in PyGame
# for Batocera Retrotrivia
# lbrpdx - 2020/2021
# https://github.com/lbrpdx/retrotrivia
# License: LGPL 3.0
import pygame
import subprocess
import os

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
        self.procvideo   = subprocess.Popen(commandvideo, stdout=subprocess.PIPE, bufsize=self.bytes_per_frame*3)
        try:
            os.remove(TMP_AUDIO_FILE)
        except:
            pass
        self.procaudio   = subprocess.call(commandaudio, stdout=subprocess.PIPE, bufsize=1024*1024)
        self.image       = pygame.Surface((rect.width, rect.height), pygame.HWSURFACE)
        self.rect        = self.image.get_rect()
        self.rect.x      = rect.x
        self.rect.y      = rect.y
        # Used to maintain frame-rate
        self.last_at     = 0              # time frame starts to show
        self.frame_delay = int(1000/FPS)  # milliseconds duration to show frame
        # audio
        if os.path.isfile(TMP_AUDIO_FILE):
            sound_manager.play(TMP_AUDIO_FILE, 800)
        # and tell when to stop it
        self.video_stop  = False
        # optional pixelate effect
        self.mode        = mode
        self.coeff       = 2.5        # how slow you want to un-pixelate
        self.time_start  = pygame.time.get_ticks()

    def stop(self):
        self.video_stop  = True

    def update(self, timer, tmax):
        if (not self.video_stop):
            time_now = pygame.time.get_ticks()
            if (time_now > self.last_at + self.frame_delay):   # has the frame shown for long enough
                self.last_at = time_now
                try:
                    raw_image = self.procvideo.stdout.read(self.bytes_per_frame)
                    img_temp = pygame.image.frombuffer(raw_image, (self.rect.width, self.rect.height), 'RGB')
                    self.last_image = img_temp
                    if self.mode == "pixelated":
                        # timer in second: don't pixellate if < 3 sec left
                        if timer > 3:
                            mmax = max (timer, tmax)
                            (px, py) = (pow(2,int((mmax - timer +1)/self.coeff)), pow(2,int((mmax - timer +1)/self.coeff)))
                            if (px, py) < (self.rect.width, self.rect.height):
                                img_temp = pygame.transform.scale(img_temp, (px,py))
                        self.image = pygame.transform.scale(img_temp, (self.rect.width, self.rect.height))
                    elif self.mode == "rotated":
                        self.image = pygame.transform.rotate(img_temp, (180-(time_now-self.time_start)/20)%360).convert_alpha()
                        (x, y) = self.rect.center
                        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height)).convert_alpha()
                        self.rect = self.image.get_rect()
                        self.rect.center = (x,y)
                    elif self.mode == "zoom":
                        (x, y) = self.rect.center
                        ttime = (time_now-self.time_start)/1000 # milliseconds elapsed
                        htime = ttime
                        if ttime > tmax:
                            htime = tmax
                        hx = max (0, x*(1-htime/tmax))
                        hy = max (0, y*(1-htime/tmax))
                        rct = pygame.Rect(hx, hy, self.rect.width*htime/tmax, self.rect.height*htime/tmax)
                        self.image = img_temp.subsurface(rct)
                        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height)).convert_alpha()
                        self.rect = self.image.get_rect()
                        self.rect.center = (x,y)
                    else:
                        self.image = img_temp
                    self.proc.stdout.flush()  # doesn't seem to be necessary
                except Exception as e:
                    # error getting data, end of file?
                    print ("Videoplayer running: error {}".format(e))
        else:
            try:
                self.image = self.last_image
                self.proc.stdout.flush()  # doesn't seem to be necessary
            except Exception as e:
                print ("Videoplayer stopped: error {}".format(e))
