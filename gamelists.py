# Simple Quiz Game Engine in PyGame
# for Batocera Retrotrivia
# lbrpdx - 2020
# https://github.com/lbrpdx/retrotrivia
# License: LGPL 3.0
import xml.etree.ElementTree as ET
import random
import os

BASEPATH  = '/userdata/roms/'
XML       = '/gamelist.xml'
MIN_GAMES = 10   # Don't index if fewer than this
MAX_GAMES = 3000 # Don't index full sets
SYSTEMS   = [  '3do', '3ds', 'amiga1200', 'amiga500', 'amigacd32', 'amigacdtv', 'amstradcpc', 'apple2', 'atari2600', 'atari5200', 'atari7800', 'atari800', 'atarist', 'atomiswave', 'c128', 'c20', 'c64', 'colecovision', 'daphne', 'dos', 'dreamcast', 'fbneo', 'fds', 'gameandwatch', 'gamecube', 'gamegear', 'gb', 'gba', 'gbc', 'gx4000', 'intellivision', 'jaguar', 'lynx', 'mame', 'mastersystem', 'megadrive', 'msx', 'msx1', 'msx2', 'msx2+', 'n64', 'naomi', 'nds', 'neogeo', 'neogeocd', 'nes', 'ngp', 'ngpc', 'o2em', 'openbor', 'pc88', 'pc98', 'pcengine', 'pcenginecd', 'pcfx', 'pico8', 'pokemini', 'ports', 'prboom', 'ps2', 'ps3', 'psp', 'psx', 'satellaview', 'saturn', 'scummvm', 'sega32x', 'segacd', 'sg1000', 'snes', 'sufami', 'supergrafx', 'thomson', 'tic80', 'vectrex', 'virtualboy', 'wii', 'wiiu', 'windows', 'wswan', 'wswanc', 'x68000', 'zx81', 'zxspectrum' ]

class gamelist:
    def __init__(self):
        self.Q =[]

    def load(self, system):
        self.tree = ET.parse(BASEPATH+system+XML)
        root = self.tree.getroot()
        setgames = set()
        for item in root.findall('game/name'):
            short=item.text.split('(')[0] # Remove (USA, Europe...)
            setgames.add(short.rstrip(' '))
        allgames = [n for n in setgames]
        print ("Loading "+system+" games : "+str(len(allgames)))
        if len(allgames) < MIN_GAMES:
            return

        indexed_games = 0
        for item in root.findall('game'):
            vid = item.find('video')
            file_vid = False
            if vid is not None:
                v = vid.text
                try:
                    if os.path.isfile(BASEPATH+system+'/'+v):
                        file_vid = True
                    else:
                        pass
                except:
                    pass
                if file_vid:
                    name = item.find('name')
                    n = name.text.split('(')[0].rstrip(' ')
                    it = list(range(4))
                    it = [i+1 for i in it]
                    random.shuffle(it)
                    possval = random.sample(allgames, 5)
                    if n in possval:
                        possval.remove(n)
                    res = n, possval[0], possval[1], possval[2]
                    line = [ BASEPATH+system+'/'+v, it[0], '', '', '', '']
                    for i in list (range(4)):
                        line[1+it[i]]=res[i]
                    out = tuple(line)
                    self.Q.append(out)
                    indexed_games += 1
                    if indexed_games >= MAX_GAMES:
                        print ("Warning: "+system+" hits the max games number.")
                        return

    def load_all(self):
        for sys in SYSTEMS:
            if os.path.isfile(BASEPATH+sys+XML):
                self.load(sys)
        return self.Q

    def show(self):
        for item in self.Q:
            print (item)

if __name__ == '__main__':
    gl = gamelist()
    gl.show()
