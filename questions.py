# Simple Quiz Game Engine in PyGame
# for Batocera Retrotrivia
# lbrpdx - 2020
# https://github.com/lbrpdx/retrotrivia
# License: LGPL 3.0
Q = [
        ('Which video game designer created Mario and Zelda?', 4, 'Hideo Kojima', 'Satoru Iwata', 'Gunpei Yokoi', 'Shigeru Miyamoto' ),
        ('How was the Nintendo Entertainement System called in South Korea?', 1, 'Hyundai Comboy', 'Samsung Gamicom', 'Goldstar Compai', 'Gangam Metro'),
        ('In 1991, "Titus the Fox" was a remake of a Titus game originally sold in France under the name:', 2, 'Tintin et les Sept Boules de Cristal', 'Lagaf: Les Aventures de Moktar', 'Lucky Luke et la ballade des Dalton', 'Les Guignols de l\'Info'),
        ('What was Lara Croft\'s original name in the early development of Tomb Raider?', 2, 'Leah Drake', 'Laura Cruz', 'Tabatha Crush', 'Carla Raft'),
        ('What home console supported HDTV first?', 2, 'Sega Dreamcast', 'Microsoft Xbox', 'Sony Playstation 2', 'Nintendo Gamecube'),
        ('What was the first commercial home console?', 2, 'MB Vectrex', 'Magnavox Odyssey', 'Atari 2600', 'Sega SG-1000'),
        ('The Sega Megadrive was called "Genesis" in the USA because of a trade mark dispute against:', 4, 'a movie by Universal', 'a video game by Accolade', 'a pharmaceutical medication by Pfizer', 'an American computer storage company'),
        ('What is the Russian name of the "Tetris theme Type-A" classical song?', 1, 'Korobeiniki', 'Zubrowskaia Terika', 'Novaya Kalinka', 'Podmoskovnie'),
        ('According to John Romero himself, what\'s the name of Doom hero?', 4, 'B.J. Blazkowicz', 'Flynn Taggart', 'John Kane', 'Doom Guy'),
        ('Space Invaders hit arcade rooms in:', 3, '1974', '1976', '1978', '1980'),
        ('Nintendo released its Game Boy handheld console In Japan in:', 1, '1989', '1990', '1991', '1992'),
        ('MegaMan\'s Dr. Light full name is: ', 4, 'William Light', 'Michael Light', 'George Light', 'Thomas Light'),
        ('What\'s Paras evolution in the Pokemon series?', 1, 'Parasect', 'Pamichuk', 'Bulbazaar', 'Saragon'),
        ('What\'s the English name of the red ghost in Pac-Man?', 1, 'Blinky', 'Pinky', 'Inky', 'Clyde'),
        ('When designing \'Donkey Kong\', which character did Nintendo want to use as the hero before Mario?', 4, 'Superman', 'Pac-Man', 'Archie', 'Popeye'),
        ('What\'s the name of the Russian fighter in Nintendo Punch-Out?', 2, 'Dimitri Lakkai', 'Soda Popinski', 'Mikhail Gorbinski', 'Boris Stokanov'),
        ('Who\'s the "voice" of Mario?', 1, 'Charles Martinet', 'Mike Danieri', 'Bob Lasalle', 'Phil Plumley'),
        ('Who\'s the "voice" of Cortana, Peach and Toad?', 4, 'Michele Williams', 'Alison Heart', 'Cherie Dawsir', 'Jen Taylor'),
        ('The PlayStation 2 design is a heavily inspired by an old computer manufactured by:', 3, 'Amstrad', 'Commodore Amiga', 'Atari', 'Sinclair'),
        ('Who did *NOT* play a part in the game Wing Commander III?', 4, 'Mark Hamill', 'Malcom McDowell', 'John Rhys-Davies', 'Ian McKellen'),
        ('What does CAPCOM stand for?', 1, 'Capsule Computers', 'Capacious Computers', 'Capital Computers', 'Caption Computers'),
        ('What word is written on the chip powering a Dreamcast VMU?', 3, 'Genius', 'Wasabi', 'Potato', 'Brain'),
        ('What year was born Toru Iwatani, creator of Pac-Man?', 3, '1935', '1945', '1955', '1965'),
        ('Which of the following titles has *NEVER* been released?', 2, 'Street Fighter II: the New Challengers', 'Super Street Fighter II: Ultra Combo Fight', 'Hyper Street Fighter II: The Anniversary Edition', 'Super Street Fighter II: Turbo HD Remix'),
        ('Which company manufactured the Nintendo 64 Graphic Processor Unit?', 2, 'IBM', 'Silicon Graphics', 'Cray', 'Nvidia'),
        ('How was named Apple\'s video game console, manufactured with Bandai? ', 1, 'Pippin', 'Gamelink', 'Newton', 'Psion'),
        ('How was called the Sega Dreamcast online service?', 4, 'Sega Virtua Gameroom', 'Sega X-Connect', 'Sega Hyperspace', 'Sega Net'),
        ('What was the maximum storage size of a Nintendo Gamecube disc?', 2, '1.1 GB of data', '1.5 GB of data', '1.8 GB of data', '2.1 GB of data'),
        ('Introduced in 1991, when was the NeoGeo AES discontinued?', 4, '1998', '2000', '2002', '2004'),
        ('What was the introduction price of the Atari Lynx in 1989, the first color handheld console ever?', 2, '$99', '$149', '$199', '$249'),
        ('Originally, the Sony Playstation was intended to be a CD-ROM add-on to:', 1, 'Super Nintendo Entertainment System', 'Sega Megadrive/Genesis', 'NeoGeo AES', 'Comcast Cablebox'),
        ('Who *NEVER* produced any 3DO Interactive Multiplayer System?', 1, 'Philips', 'Panasonic', 'Sanyo', 'Goldstar'),
        ('What was the name of the Amiga expansion board system?', 4, 'Diego', 'Calabro', 'Tornado', 'Zorro'),
        ('What does SEGA stand for?', 4, 'Sensei Games', 'Sensation Games', 'Select Games', 'Service Games'),
        ('What year was the original Grand Theft Auto released?', 3, '1993', '1995', '1997', '1999'),
        ('Before computers, Amstrad was known in the UK for their:', 1, 'hi-fi and stereo systems', 'kitchen appliances', 'car parts', 'business telephones'),
        ('"Another World" (Out of This World) was designed and coded by this single person:', 2, 'Paul Cuisset', 'Eric Chahi', 'Michel Ancel', 'Frederick Raynal'),
        ('How is called the Central Processing Unit originally designed for the PlayStation 2?', 4, 'Agnes', 'Lightning', 'Magic Wand', 'Emotion Engine'),
        ('In the Legend of Zelda universe, Ganon is a hybrid of a Demon and a:', 1, 'Gerudo', 'Goron', 'Korok', 'Sheikah'),
        ('What was the original name of Tecmo when they released "Bomb Jack" in 1984?', 3, 'Ryokan', 'Acmo', 'Tehkan', 'Komodo'),
        ('What was the original name of the MAME emulator when Nicola Salmoria started his project?', 3, 'Emul-Them-All', 'Arcadia', 'Multi-Pac', 'Galastar'),
        ('The original Nintendo Game Boy CPU could run at:', 1, '4 MHz', '8 MHz', '16 MHz', '32 MHz' ),
        ('Before creating Apple Computers, Steve Jobs was employee #40 at:', 2, 'IBM', 'Atari', 'Commodore', 'Texas Instruments'),
        ('A gene in the human body, ensuring our organs grow at the right place,  was called after a video game:', 2, 'SMB - Super Mario Bros', 'SHH - Sonic the HedgeHog', 'SF2 - Street Fighter II', 'MGS - Metal Gear Solid'),
        ('In the 1990s, who was a regular Tetris champion, printed out in the "Nintendo Power" magazine?', 1, 'Steve Wozniak', 'Bill Gates', 'Mark Zuckerberg', 'Elon Musk'),
        ('When was the first version of Batocera Linux released?', 2, '2015', '2016', '2017', '2018'),
        ('Robin Williams, the deceased actor, was a video game nerd who named his daughter:', 4, 'Cecil (from Final Fantasy)', 'Daphne (from Dragon\'s Lair)', 'Lara (from Tomb Raider)', 'Zelda (from the Legend of Zelda)'),
        ('In South Korea, since 2011 it is forbidden for under-16 gamers to:', 1, 'play online video games after midnight', 'play a gender-neutra/non-binary character', 'kill an opponent in an online video game', 'use virtual currencies, even in offline games'),
        ('Nolan Bushnell, founder of Atari, also founded this fast food chain:', 2, 'Burger King', 'Chuck E Cheese', 'Taco Bell', 'Shake Shack'),
        ('Gunpei Yokoi, the creator of the GameBoy started his career at Nintendo as a:', 4, 'Translator', 'HR Recruiter', 'Financial Analyst', 'Janitor'),
        ('Donkey Kong was named as such because Miyamoto thought "donkey" in English meant', 3, 'Strong', 'Giant', 'Stupid', 'Monkey'),
        ('What video game did Daniel Barry played on the Space Shuttle mission STS-96 in 1999?', 4, 'Quake', 'Half-Life', 'Grand Theft Auto', 'Starcraft'),
        ('What band made more money from their "Guitar Hero" edition than the sales of any of their previous albums?', 2, 'AC/DC', 'Aerosmith', 'Metallica', 'Van Halen'),
        ('Xbox was originally supposed to be named:', 4, 'Project Nolan', 'PSK (aka the PlayStation Killer)', 'Microsoft Future TV', 'DirectX-Box (for the graphic API)'),
        ('The Nintendo character Kirby was named after John Kirby:', 1, 'An attorney who won a lawsuit for Nintendo', 'Their US head of marketing', 'An all-star Engineer who coded 80% of the original game', 'No, nobody: "Kirby" is just a cute name'),
        ('Henry Cavill missed his first audition for the role of Superman because he was too busy playing:', 2, 'Halo', 'World of Warcraft', 'Call of Duty', 'Guitar Hero'),
        ('Goldeneye 007 on the Nintendo 64 was developed by a team of:', 2, '2 developers', '10 developers', '50 developers', 'about 100 developers'),
        ('If Mario was a real person, how far would he have to run to complete the origianl Super Mario Bros?', 2, '0.9 mile / 1.5 km', '3.4 miles / 5.5 km', '7.5 miles / 12 km', '12.4 miles / 20 km'),
        ('On a global scale, what is the average age of a video game player', 4, '15', '20', '25', '30'),
        ('Before he was given the name "Mario", what was the name  of this character in the early Nintendo games?', 4, 'Ooyaji', 'Damaro', 'Felix', 'Jumpman'),
        ('From the litteral Japanese, the Pokemon "Pikachu" name would translate in English into:', 1, 'Lightning squeak', 'Cute cat', 'Brave sidekick', 'Yellow blast'),
        ('In the Nintendo games, the full name of Princess Peach is:', 4, 'Peach Rosegarden', 'Peach Mushy', 'Peach Juicy', 'Peach Toadstool'),
        ('In "Burnout Paradise", DJ Atomica makes several references to another video game:', 1, 'SSX', 'The Sims', 'Need for Speed', 'Medal of Honor'),
        ('In the original Golden Axe, some of the death screams are digitized from the movie:', 4, 'Terminator', 'Rambo', 'The Exorcist', 'Conan the Barbarian'),
        ('Devil May Cry was originally to set be a chapter in the following series:', 1, 'Resident Evil', 'Street Fighter', 'Mega Man', 'Monster Hunter'),
        ('In ancient Greek, "Kratos" from God of War, means:', 4, 'Fire', 'Warrior', 'Anger', 'Power'),
        ('The first video game to feature multiple endings depending on how you play was:', 4, 'ET on the Atari 2600', 'Parsec on the TI-99', 'Galaga on the MSX', 'Castlevania 2 (Simon\'s Quest) on the NES'),
        ('The game "Malice" on PS2 featured voice-overs and songs from:', 2, 'Brtiney Spears', 'Gwen Stefani', 'Christina Aguilera', 'P!nk'),
        ('The perfect score on the original Pac-Man arcade game was achived in 1999 by Billy Mitchell with:', 2, '999,990 points', '3,333,360 points', '9,999,990 points', '33,666,000 points'),
        ('"World of Warcraft" was the highest grossing video game when it crossed the mark of:', 3, '10 million dollars', '100 million dollars', '10 billion dollars', '100 billion dollars'),
        ('The highest number a human can press a controller button is:', 3, '4 times om a second', '8 times in a second', '16 times in a second', '32 times in a second'),
        ('What\'s the name of the Japanese neuroscientist who helped develop the "Brain Age" series of video games on the Nintendo DS', 4, 'Dr. Kawasaki', 'Dr. Matashima', 'Dr. Mashimata', 'Dr. Kawashima'),
        ('What\'s the largest sum ever offered as prize money in an e-sport tournament?', 4, '81,000 dollars', '180,000 dollars', '1.8 million dollars', '18 million dollars'),
        ('The American musical duo "Buckner & Garcia" is best known for a song about:', 1, 'Pac-Man', 'Space Invaders', 'Duck Hunt', 'Sonic the Hedgehog'),
        ('Before video games, what product did Nintendo release first?', 4, 'Medical devices', 'Rice cookers', 'Rain boots', 'Playing cards'),
        ('In what game series can you find the "Umbrella Corporation" pharmaceutical company?', 1, 'Resident Evil', 'Metal Gear Solid', 'Final Fantasy', 'Fallout'),
        ('In the original "Legend of Zelda", the maximum amount of rupees you could you get was:', 2, '99', '254', '999', '1024'),
        ('What home console was the first to ship with 1MB internal memory?', 3, 'Sony PlayStation', 'Nintendo 64', 'Sega Saturn', 'Atari Jaguar'),
        ('What is the name of the home planet in "Gears of War?"', 4, 'Arrakis', 'Caladan', 'Lylat', 'Sera'),
        ('The Obama campaign paid for in-game ads in the following game:', 1, 'Burnout Paradise', 'Little Big Planet', 'Fallout 3', 'Mirror\'s Edge'),
        ('In a 1993 movie, Bob Hoskins, the famous English actor, portrayed:', 1, 'Mario', 'Blanka', 'Dr. Robotnik', 'Sub-Zero'),
        ('In what year was "Fortnite" released?', 3, '2015', '2016', '2017', '2018'),
        ('Which music star secretly composed music for Sonic 3?', 2, 'Prince', 'Michael Jackson', 'Paul McCartney', 'Bono'),
        ('How many buttons does the Atari 2600 controller have?', 1, '1', '2', '3', '4'),
        ('What is the name of the alien alliance in the first "Halo" games?', 4, 'The Horde', 'The Chozo', 'The Perdition', 'The Covenant'),
        ('What is the name of the woman to be saved by Mario in the original Donkey Kong game?', 4, 'Camilla', 'Peach', 'Rosalina', 'Pauline'),
        ('What item makes Matio invincible in the original "Super Mario Bros"?', 3, 'Mushroom', 'Flower', 'Starman', 'Yoshi Egg'),
        ('What is the name of the star system where "Star Fox" takes place?', 3, 'Arrakis', 'Caladan', 'Lylat', 'Sera'),
        ('What game officially featured Michael Jackson as the hero?', 2, 'Thriller', 'Moonwalker', 'Space Channel 5', 'Dance Dance Revolution'),
        ('What was the name of the peripheral device adding vibration to the Nintendo 64 controller?', 3, 'Vibratron', 'Visual Memory Unit', 'Rumble Pak', 'Haptic 64'),
        ('Which character goes by the codename "Killer Bee"?', 4, 'Bayonetta', 'Lara Croft', 'Meryl Silverburgh', 'Cammy'),
        ('In "Metal Gear", Solid and Liquid Snake were born as a result of which secret operation?', 1, 'Les Enfants Terribles', 'Les Miserables', 'Guernica', 'The Beauty and the Beast'),
        ('Who steals all the bananas in "Donkey Kong Country"?', 4, 'Tiki Tak Tribe', 'Dixie Kong', 'Kiki Koro', 'King K. Rool'),
        ('What is the final course in every "Mario Kart" game?', 1, 'Rainbow Road', 'Bowser\'s Castle', 'Choco Island', 'DK\'s Jungle'),
        ('Which was the first Nintendo console to use optical discs?', 3, 'Super Nintendo', 'Nintendo 64', 'Gamecube', 'Wii'),
        ('Which video game series has "Underground", "Most Wanted" and "Hot Pursuit" installments?', 4, 'Call of Duty', 'Burnout', 'Medal of Honor', 'Need for Speed'),
        ('Before being known as a plumber, Mario originally was a:', 2, 'Fireman', 'Carpenter', 'Waiter', 'Butcher'),
        ('"Myst", the adventure puzzle game, was designed by two brothers:', 4, 'Larry and Andy Wachowski', 'Jake and Elwood Blues', 'Matt and Ross Duffer', 'Robyn and Rand Miller'),
        ('LucasArts\'s "The Day of the Tentacle" is a sequel to:', 3, 'Loom', 'The Dig', 'Maniac Mansion', 'Zak McKracken'),
        ('Who wrote successful adventure games in the 1980s and 1990s like "Dark Crystal", "King\'s Quest" and "Phantasmagoria"?', 1, 'Roberta Williams', 'Tim Schafer', 'Ron Gilbert', 'David Cage'),
        ('Which editor originally published "Arkanoid"?', 4, 'Capcom', 'Tecmo', 'Konami', 'Taito'),
#        ('', 4, '', '', '', ''),
     ]
