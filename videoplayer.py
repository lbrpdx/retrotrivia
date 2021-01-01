# Simple Quiz Game Engine in PyGame
# for Batocera Retrotrivia
# lbrpdx - 2020
# https://github.com/lbrpdx/retrotrivia
# License: LGPL 3.0
import pygame
import subprocess

FFMPEG_BIN       = "/usr/bin/ffmpeg"   # Full path to ffmpeg executable
SOUND_VOL        = 0.7   # FIXME: to sync up with GameState object

#######################################
### Video to PyGame converter
class VideoSprite(pygame.sprite.Sprite):

    def __init__(self, rect, filename, sound_volume, pixelated, FPS=30):
        pygame.sprite.Sprite.__init__(self)
        commandvideo = [ FFMPEG_BIN,
                '-loglevel', 'quiet',
                '-i', filename,
                '-f', 'image2pipe',
                '-s', '%dx%d' % (rect.width, rect.height),
                '-pix_fmt', 'rgb24',
                '-vcodec', 'rawvideo', 
                '-' ]
        commandaudio = [ FFMPEG_BIN,
                '-loglevel', 'quiet', '-y',
                '-i', filename, '-vn',
                '-c:a', 'pcm_s16le',
                '-b:a', '128k',
                '/tmp/retrotrivia_audio.wav' ]
        self.bytes_per_frame = rect.width * rect.height * 3
        self.procvideo   = subprocess.Popen(commandvideo, stdout=subprocess.PIPE, bufsize=self.bytes_per_frame*3)
        self.procaudio   = subprocess.call(commandaudio, stdout=subprocess.PIPE, bufsize=1024*1024)
        self.image       = pygame.Surface((rect.width, rect.height), pygame.HWSURFACE)
        self.rect        = self.image.get_rect()
        self.rect.x      = rect.x
        self.rect.y      = rect.y
        # Used to maintain frame-rate
        self.last_at     = 0           # time frame starts to show
        self.frame_delay = 1000 / FPS  # milliseconds duration to show frame
        # audio
        self.audiotrack  = None
        if sound_volume > 0:
            self.audiotrack=pygame.mixer.Sound('/tmp/retrotrivia_audio.wav')
            self.audiotrack.set_volume(0.2*sound_volume)
            self.audiotrack.play()
        # and tell when to stop it
        self.video_stop  = False
        # optional pixelate effect
        self.pixelated   = pixelated
        self.coeff       = 2 # how slow you want to un-pixelate

    def stop(self):
        self.video_stop  = True
        if self.audiotrack:
            self.audiotrack.stop()

    def update(self, timer, tmax):
        if (not self.video_stop):
            time_now = pygame.time.get_ticks()
            if (time_now > self.last_at + self.frame_delay):   # has the frame shown for long enough
                self.last_at = time_now
                try:
                    raw_image = self.procvideo.stdout.read(self.bytes_per_frame)
                    img_temp = pygame.image.frombuffer(raw_image, (self.rect.width, self.rect.height), 'RGB')
                    if self.pixelated:
                        # timer in second: don't pixellate if < 3 sec left
                        if timer > 3:
                            mmax = max (timer, tmax)
                            (px, py) = (pow(2,int((mmax - timer +1)/self.coeff)), pow(2,int((mmax - timer +1)/self.coeff)))
                            # print ((px,py))
                            if (px, py) < (self.rect.width, self.rect.height):
                                img_temp = pygame.transform.scale(img_temp, (px,py))
                        self.image = pygame.transform.scale(img_temp, (self.rect.width, self.rect.height))
                    else:
                        self.image = img_temp
                    #self.proc.stdout.flush()  - doesn't seem to be necessary
                except:
                    # error getting data, end of file?  Black Screen it
                    self.image = pygame.Surface((self.rect.width, self.rect.height), pygame.HWSURFACE)
                    self.image.fill((0,0,0))
                    self.video_stop = True
