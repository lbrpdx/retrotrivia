# Retrotrivia 
![Retrotrivia](https://raw.githubusercontent.com/lbrpdx/retrotrivia/master/assets/logo.png)

A trivia game for retrogaming lovers.

## What's the game?

You will be asked questions about your retro video games, and some general retro-gaming trivia. 
Several gaming modes ara available:
 - 210+ handcrafted trivia questions
 - video thumbnails: guess what game is shown, this is the easiest mode
 - pixelate: same as video thumbnails, but pixelated video (listen carefully to the audio track!)
 - rotate: like good old demo makers -- or after a severe hangover
 - zoom: start with a tiny part of the screen, and then zoom out until you see the full picture

Rules: you have a countdown timer for each question. You need to answer before the countdown times out. Let's say you give your answer with 5 seconds left on the timer: if your answer is correct, you score 5 points, if not, you lose 5 points. Be fast, be bold: you won't go below 0 on your score.

Oh, and you can play with up to 4 players for a friendly competition.

In future releases:
 - new trivia questions (please feel free to contribute!)
 - other game modes...

## Installation

This game is primarily meant to be used with [Batocera](https://batocera.org/). It's been developed and tested with Batocera 31 (earlier releases with 29 and 30) and its [PyGame](https://www.pygame.org) installation. You can most probably adapt it to other retrogaming distribiutions using EmulationStation `gamelist.xml` classic format.

On Batocera, you can easily download a version from the Content Downloader (in the `Upgrades & Downloads` menu). Or, if you want the latest and greatest, you can get the files from this GitHub repository, and put them into `/userdata/roms/pygame/retrotrivia`.

Controls:
 - D-Pad to select the answer (or analog stick)
 - A (or B) button to select/move to the next question.

## License

Retrotrivia is [free and opensource software](https://en.wikipedia.org/wiki/Free_and_open-source_software) and can't be sold unless explicitely permitted by its main author and maintener (@lbrpdx). As of today, nobody has gotten permission to sell it, so if you paid for it, someone abused you.

All the code is given under the [LGPL v3](https://www.gnu.org/licenses/lgpl-3.0.html) license. All the code and video game assets can be freely modified and redistributed as long as this README.md file is distributed with it, in its original form.

## How can you contribute?

Please, let me know if you face issues and bugs. If the game crashes, please send me the `logs/es_launch_stderr.log` file.

Feel free to submit PRs, this game is meant to be enriched by the community. If you don't know how to code, you can still probably help with graphic design, sounds, additional trivia questions and so on.

If you want to discuss this game, join the communituy on the `#games` channel of the [Batocera Discord](https://discord.gg/ndyUKA5) server.

Happy retrogaming!
