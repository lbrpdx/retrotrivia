# Simple Quiz Game Engine in PyGame
# for Batocera Retrotrivia
# lbrpdx - 2020-2026
# https://github.com/lbrpdx/retrotrivia
# License: LGPL 3.0
import xml.etree.ElementTree as ET
import random
import os

BASEPATH  = '/userdata/roms/'
XML       = 'gamelist.xml'
MIN_GAMES = 10    # Don't index if fewer than this
MAX_GAMES = 20000 # Don't index full sets

class gamelist:
    def __init__(self):
        self.Q = []
        self.systems = []
        for folder in sorted(os.listdir(BASEPATH)):
            full_path = os.path.join(BASEPATH, folder)
            # Check if it's a directory and contains a gamelist.xml
            if os.path.isdir(full_path):
                if os.path.isfile(os.path.join(full_path, XML)):
                    self.systems.append(folder)

    def load(self, system):
        q = []
        try:
            self.tree = ET.parse(os.path.join(BASEPATH, system, XML))
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
            v = self.load(sys)
            if len(v) > 0:
                self.Q.append(v)
        return self.Q

    def show(self):
        for item in self.Q:
            print (item)

if __name__ == '__main__':
    gl = gamelist()
    gl.load_all()
    gl.show()
