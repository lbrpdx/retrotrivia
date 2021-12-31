# Simple Quiz Game Engine in PyGame
# for Batocera Retrotrivia
# lbrpdx - 2020/2021
# https://github.com/lbrpdx/retrotrivia
# License: LGPL 3.0
import xml.etree.ElementTree as ET
import random
import os

BASEPATH  = '/userdata/roms/'
XML       = '/gamelist.xml'
MIN_GAMES = 10    # Don't index if fewer than this
MAX_GAMES = 10000 # Don't index full sets
SYSTEMS   = [ '3do', '3ds', 'abuse', 'adam', 'advision', 'amiga1200', 'amiga500', 'amigacd32', 'amigacdtv', 'amstradcpc', 'apfm1000', 'apple2', 'apple2gs', 'arcadia', 'atari2600', 'atari5200', 'atari7800', 'atari800', 'atarist', 'atomiswave', 'bbc', 'c128', 'c20', 'c64', 'cavestory', 'cdi', 'channelf', 'coco', 'colecovision', 'cplus4', 'daphne', 'dos', 'dreamcast', 'easyrpg', 'ecwolf', 'fbneo', 'fds', 'flash', 'fm7', 'fmtowns', 'fpinball', 'gamate', 'gameandwatch', 'gamecom', 'gamecube', 'gamegear', 'gb', 'gba', 'gbc', 'gmaster', 'gx4000', 'intellivision', 'j2me', 'jaguar', 'lcdgames', 'lutro', 'lynx', 'mame', 'mastersystem', 'megadrive', 'megaduck', 'model2', 'model3', 'msx', 'msx1', 'msx2', 'msx2+', 'msxturbor', 'mugen', 'n64', 'n64dd', 'naomi', 'nds', 'neogeo', 'neogeocd', 'nes', 'ngp', 'ngpc', 'o2em', 'openbor', 'opentyrian', 'pc88', 'pc98', 'pcengine', 'pcenginecd', 'pcfx', 'pet', 'pico8', 'pokemini', 'ports', 'prboom', 'ps2', 'ps3', 'psp', 'psx', 'pv1000', 'samcoupe', 'satellaview', 'saturn', 'scummvm', 'scv', 'sega32x', 'segacd', 'sg1000', 'sgb', 'snes', 'nes-msu1', 'solarus', 'sufami', 'supervision', 'supergrafx', 'thomson', 'ti99', 'tic80', 'tutor', 'tvgames', 'uzebox', 'vectrex', 'virtualboy', 'wii', 'wiiu', 'windows', 'wswan', 'wswanc', 'x1', 'xbox', 'x68000', 'zc210', 'zx81', 'zxspectrum' ]

class gamelist:
    def __init__(self):
        self.Q = []
        self.systems = SYSTEMS

    def load(self, system):
        q = []
        if not os.path.isfile(BASEPATH+system+XML):
            return q
        try:
            self.tree = ET.parse(BASEPATH+system+XML)
        except Exception as e:
            print("Warning: unable to load {}/gamelist.xml".format(system))
            return q
        root = self.tree.getroot()
        setgames = set()
        try:
            for item in root.findall('game/name'):
                short=item.text.split('(')[0] # Remove (USA, Europe...)
                setgames.add(short.rstrip(' '))
        except Exception as e:
            print("No game with video for {}".format(system))
            return q
        allgames = [n for n in setgames]
        if len(allgames) < MIN_GAMES:
            return q
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
                    q.append(out)
                    indexed_games += 1
                    if indexed_games >= MAX_GAMES:
                        return q
        return q

    def load_all(self):
        for sys in self.systems:
            self.Q.append(self.load(sys))
        return self.Q

    def show(self):
        for item in self.Q:
            print (item)

if __name__ == '__main__':
    gl = gamelist()
    gl.load_all()
    gl.show()
