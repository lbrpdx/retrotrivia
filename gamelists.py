# Simple Quiz Game Engine in PyGame
# for Batocera Retrotrivia
# lbrpdx - 2020-2025
# https://github.com/lbrpdx/retrotrivia
# License: LGPL 3.0
import xml.etree.ElementTree as ET
import random
import os

BASEPATH  = '/userdata/roms/'
XML       = '/gamelist.xml'
MIN_GAMES = 10    # Don't index if fewer than this
MAX_GAMES = 20000 # Don't index full sets
SYSTEMS   = [ '3do', '3ds', 'abuse', 'adam', 'advision', 'amiga1200', 'amiga500', 'amigacd32', 'amigacdtv', 'amstradcpc', 'apfm1000', 'apple2', 'apple2gs', 'arcadia', 'archimedes', 'arduboy', 'astrocde', 'atari2600', 'atari5200', 'atari7800', 'atari800', 'atarijaguardcd', 'atarist', 'atom', 'atomiswave', 'bbc', 'bennugd', 'boom3', 'bstone', 'c128', 'c20', 'c64', 'camplynx', 'cannonball', 'catacomb', 'catacombgl', 'cavestory', 'cdi', 'cdogs', 'cgenius', 'channelf', 'chihiro', 'coco', 'colecovision', 'commanderx16', 'corsixth', 'cpet', 'cplus4', 'crvision', 'daphne', 'devilutionx', 'dice', 'doom3', 'dos', 'dreamcast', 'dxx-rebirth', 'easyrpg', 'ecwolf', 'eduke32', 'electron', 'enterprise', 'etlegacy', 'fallout1-ce', 'fallout2-ce', 'fbneo', 'fds', 'flash', 'flatpak', 'fm7', 'fmtowns', 'fpinball', 'fury', 'gamate', 'gameandwatch', 'gamecom', 'gamecube', 'gamegear', 'gamepock', 'gb', 'gb2players', 'gba', 'gbc', 'gbc2players', 'gmaster', 'gp32', 'gx4000', 'gzdoom', 'hcl', 'hurrican', 'ikemen', 'info.txt', 'intellivision', 'iortcw', 'j2me', 'jaguar', 'jaguarcd', 'jazz2', 'jkdf2', 'jknight', 'laser310', 'lcdgames', 'lindbergh', 'lowresnx', 'lutro', 'lynx', 'macintosh', 'mame', 'mastersystem', 'megacd', 'megadrive', 'megaduck', 'model2', 'model3', 'mohaa', 'moonlight', 'mrboom', 'msu-md', 'msx1', 'msx2', 'msx2+', 'msxturbor', 'mugen', 'multivision', 'n64', 'n64dd', 'namco22', 'namco2x6', 'naomi', 'naomi2', 'nds', 'neogeo', 'neogeocd', 'nes', 'ngp', 'ngpc', 'o2em', 'odcommander', 'openbor', 'openjazz', 'openjk', 'openjkdf2', 'openlara', 'openmohaa', 'oricatmos', 'pc88', 'pc98', 'pcengine', 'pcenginecd', 'pcfx', 'pdp1', 'pet', 'pico', 'pico8', 'plugnplay', 'pokemini', 'ports', 'prboom', 'ps2', 'ps3', 'ps4', 'psp', 'psvita', 'psx', 'pv1000', 'pygame', 'pyxel', 'quake', 'quake2', 'quake3', 'raze', 'reminiscence', 'rott', 'samcoupe', 'satellaview', 'saturn', 'scummvm', 'scv', 'sdlpop', 'sega32x', 'segacd', 'sg1000', 'sgb', 'sgb-msu1', 'singe', 'snes', 'snes-msu1', 'socrates', 'solarus', 'sonic3-air', 'sonic-mania', 'sonicretro', 'spectravideo', 'steam', 'sufami', 'superbroswar', 'supergrafx', 'supervision', 'supracan', 'systemsp', 'theforceengine', 'thextech', 'thomson', 'ti99', 'tic80', 'traider1', 'traider2', 'triforce', 'tutor', 'tvgames', 'tyrian', 'tyrquake', 'uqm', 'uzebox', 'vc4000', 'vectrex', 'vemulator', 'vgmplay', 'videopacplus', 'vircon32', 'virtualboy', 'vis', 'vitaquake2', 'voxatron', 'vpinball', 'vsmile', 'wasm4', 'wii', 'wiiu', 'windows', 'windows_installers', 'wswan', 'wswanc', 'x1', 'x68000', 'xash3d_fwgs', 'xbox', 'xbox360', 'xegs', 'xrick', 'zc210', 'zx81', 'zxspectrum' ]

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
