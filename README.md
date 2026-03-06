# PythonOS .PY Edition

> A MS-DOS inspired operating system shell written entirely in Python.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
![Version](https://img.shields.io/badge/Version-0.1%20Build%201-orange)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

```
                  //,
           /////((((((((((((/
          ///   ((((((((((((
         /(((((((((((((((((
     ,///((((((((((((((((((@  ,,,,
  /////((((((((((((((((((@@@  ,,,,,,,
 ////((((((((((((((((((@@@@@ ,,,,,,,,,
 //((((((((((((((((((@@@@@@ ,,,,,,,,,,
,((((((((((   ,,,,,,,,,,,,,,,,,,,,&&&&&&&&&&&&&
 ((((((((  ,,,,,,,,,,,,,,,,,,,,/&&&&&*      &&&&&.
 (((((((( ,,,,,,,,,,,,,,,,,,,,,/&&&&&       &&&&&.    *&&&&&&&&&&&&
   (((((( ,,,,,,,,,,,,,,,,,,***/&&&&&       &&&&&.  &&&&&
          ,,,,,,,,,,,,,,,***   .&&&&&       &&&&&.    *&&&&&&&&&&&&
          ,,,,,,,,,,,,*  ,**   .&&&&&       &&&&&.               &&&&&
           ,,,,,,,*****   **      &&&&&&&&&&&&&     &&&&&&&&&&&&&&&
             ,,**********
```

---

## Table of Contents
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Commands](#-commands)
- [Games](#-games)
- [License](#-license)

---

## Features

- **MS-DOS style shell** with a familiar command-line interface
- **Graphical web browser** powered by Chromium
- **Weather forecast** via wttr.in
- **Notepad** — text editor that saves files to the `files/` folder
- **Task Manager** — CPU, RAM, and GPU usage with ASCII progress bars
- **6 built-in games** — Snake, Tetris, Minesweeper, Blackjack, Maze, Tic Tac Toe, Rock Paper Scissors
- **Calculator** — normal calculator
- **Typing speed test** — well, its just speed test, dont forget about a period!
- **File manager** — view, read, and delete files

---

## Requirements

**Required:**
```
pip install psutil gputil PyQt5 PyQtWebEngine pynput
```

---

## Installation

```bash
git clone https://github.com/sowhatevering/PythonOS
cd PythonOS
pip install pynput psutil gputil PyQt5 PyQtWebEngine
python PYTHON_OS_PY_EDITION_v2.py
```

> Before using **NOTEPAD**, **TYPE**, **DEL** or **DIR**, create a folder named `files` in the same directory as the script.

---

## Commands

| Command | Description |
|---|---|
| `HELP` | List all available commands |
| `PYVER` | Show OS version info |
| `LICENSE` | Show Apache 2.0 license |
| `WHOAMI` | Show logged-in username |
| `DATE / TIME` | Show current date and time |
| `CLEAR` | Clear the screen |
| `DIR` | List files in the `files/` folder |
| `TYPE [file]` | Display contents of a file |
| `DEL [file]` | Delete a file |
| `NOTEPAD` | Open text editor |
| `CALC` | Open calculator (supports `+ - * / ** % //`) |
| `TASKMGR` | Show CPU, RAM and GPU usage |
| `WEATHER [city]` | Show 3-day weather forecast |
| `BROWSER` | Open graphical web browser |
| `GITHUB` | Open GitHub's main page |
| `MYGITHUB` | Open author's GitHub |
| `EXIT` | Exit PythonOS |

---

## Games

| Command | Game |
|---|---|
| `SNAKE` | Classic Snake — arrow keys to move |
| `TETRIS` | Tetris — arrows + space to rotate |
| `MINESWEEPER` | Minesweeper — enter coordinates |
| `TICTACTOE` | Tic Tac Toe vs AI |
| `RPS` | Rock Paper Scissors vs AI |
| `BLACKJACK` | Blackjack vs AI Dealer (multiplayer maybe coming soon)|
| `MAZE` | Randomly generated maze — arrow keys |
| `TYPETEST` | Typing speed test (WPM) |

---


## License

Licensed under the **Apache License 2.0**. 
See [https://www.apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0)

Copyright © 2026 Whatevering
