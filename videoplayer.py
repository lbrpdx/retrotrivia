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

    def __init__(self, rect, filename, FPS=30):
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
        self.audiotrack=pygame.mixer.Sound('/tmp/retrotrivia_audio.wav')
        self.audiotrack.set_volume(SOUND_VOL)
        self.audiotrack.play()
        # and tell when to stop it
        self.video_stop  = False

    def stop(self):
        self.video_stop  = True
        self.audiotrack.stop()

    def update(self):
        if (not self.video_stop):
            time_now = pygame.time.get_ticks()
            if (time_now > self.last_at + self.frame_delay):   # has the frame shown for long enough
                self.last_at = time_now
                try:
                    raw_image = self.procvideo.stdout.read(self.bytes_per_frame)
                    self.image = pygame.image.frombuffer(raw_image, (self.rect.width, self.rect.height), 'RGB')
                    #self.proc.stdout.flush()  - doesn't seem to be necessary
                except:
                    # error getting data, end of file?  Black Screen it
                    self.image = pygame.Surface((self.rect.width, self.rect.height), pygame.HWSURFACE)
                    self.image.fill((0,0,0))
                    self.video_stop = True
