import time
import os
import ast
import operator as op_module
import platform
import random
import webbrowser
from pynput import keyboard

os.system('cls' if os.name == 'nt' else 'clear')


# ─── ANSI COLORS ──────────────────────────────────────────────────────────────
class C:
    RESET  = "\033[0m"
    GREEN  = "\033[92m"
    CYAN   = "\033[96m"
    RED    = "\033[91m"
    YELLOW = "\033[93m"
    WHITE  = "\033[97m"
    BOLD   = "\033[1m"

# ─── UTILITIES ────────────────────────────────────────────────────────────────
def full_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.2)
    print('\n')
    print('                  //,')
    print('           /////(((((((((((/')
    print('          ///   ((((((((((((')
    print('         /(((((((((((((((((')
    print('     ,///((((((((((((((((((@  ,,,,')
    print('  /////((((((((((((((((((@@@  ,,,,,,,')
    print(' ////((((((((((((((((((@@@@@ ,,,,,,,,,')
    print(' //((((((((((((((((((@@@@@@ ,,,,,,,,,,')
    print(',((((((((((   ,,,,,,,,,,,,,,,,,,,,&&&&&&&&&&&&&')
    print(' ((((((((  ,,,,,,,,,,,,,,,,,,,,/&&&&&*      &&&&&.')
    print(' (((((((( ,,,,,,,,,,,,,,,,,,,,,/&&&&&       &&&&&.    *&&&&&&&&&&&&')
    print('   (((((( ,,,,,,,,,,,,,,,,,,***/&&&&&       &&&&&.  &&&&&')
    print('          ,,,,,,,,,,,,,,,***   .&&&&&       &&&&&.    *&&&&&&&&&&&&')
    print('          ,,,,,,,,,,,,*  ,**   .&&&&&       &&&&&.               &&&&&')
    print('           ,,,,,,,*****   **      &&&&&&&&&&&&&     &&&&&&&&&&&&&&&')
    print('             ,,**********')
    print('\n')
    print('PYTHON OS .PY EDITION 0.2\n')
    print("Python and the Python logo are copyrighted by the Python Software Foundation © 2001-2026")

# ─── INFO COMMANDS ────────────────────────────────────────────────────────────
def display_pyver():
    print(f'\n{C.CYAN}Python OS{C.RESET}')
    print('Version 0.1 (OS Build 1)')
    print('PythonOS .PY EDITION © 2026 by SoWhatevering')
    print('\nThis software is licensed under the GNU GENERAL PUBLIC LICENSE 3.0 to:\n')
    print(user)
    print('\n')

def display_license():
    print(f'\n{C.CYAN}Apache License, Version 2.0{C.RESET}')
    print('Copyright (C) 2026 SoWhatevering')
    print()
    print('Licensed under the Apache License, Version 2.0 (the "License");')
    print('you may not use this file except in compliance with the License.')
    print('You may obtain a copy of the License at:')
    print(f'  {C.CYAN}https://www.apache.org/licenses/LICENSE-2.0{C.RESET}')
    print()
    print('Unless required by applicable law or agreed to in writing, software')
    print('distributed under the License is distributed on an "AS IS" BASIS,')
    print('WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.')

def display_help():
    print(f'\n{C.YELLOW}Welcome in help section! This is the list of available commands:{C.RESET}')
    time.sleep(1)
    cmds = [
        ("HELP",        "Display this help section."),
        ("DIR",         "Show files in the \'files\' folder."),
        ("PYVER",       "Show Python OS version information."),
        ("LICENSE",     "Show license info."),
        ("WHOAMI",      "Show current logged-in user."),
        ("DATE / TIME",  "Show current date and time."),
        ("WEATHER [city]","Show weather forecast for a city."),
        ("BROWSER",      "Graphical web browser (Chromium engine)."),
        ("TYPE [file]", "Show contents of a file from \'files\' folder."),
        ("DEL [file]",  "Delete a file from the \'files\' folder."),
        ("NOTEPAD",     "Simple text editor (saves to \'files\' folder)."),
        ("TASKMGR",     "Show system & process info (CPU, RAM, GPU)."),
        ("CALC",        "Open the calculator."),
        ("TYPETEST",    "Test your typing speed."),
        ("SNAKE",       "Play Snake!"),
        ("TETRIS",      "Play Tetris!"),
        ("RPS",         "Play Rock-Paper-Scissors with AI!"),
        ("TICTACTOE",   "Play Tic Tac Toe with AI!"),
        ("MINESWEEPER", "Play Minesweeper!"),
        ("BLACKJACK",   "Play Blackjack with AI Dealer!"),
        ("MAZE",        "Play Maze!"),
        ("GITHUB",      "Redirect to GitHub\'s main page."),
        ("MYGITHUB",    "Redirect to author\'s GitHub profile."),
        ("CLEAR",       "Clear the screen."),
        ("EXIT",        "Exit Py-Dos mode."),
    ]
    for cmd, desc in cmds:
        print(f"  {C.CYAN}{cmd:<20}{C.RESET} {desc}")

def display_ascii():
    print("""
                     @@@@@@@@@@@@@@@@@@@@@@@*               
                   @@@@@@%%%%%%%%%%%%%&@@@@@@@@@            
                 @@@@@%%%%%%%%%%%%%%%%%%%%%@@@@@@@          
                @@@@@%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@%        
               @@@@@&%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@.      
               @@@@&%%%%%%@@@@@@*,,,,,,,     ,,,,@@@@@@%    
              @@@@&&%%%%%%@@@@##*,,,,,,           ,,%@@@@   
       @@@@@@@@@@@&&%%%%%%@@@&###*,,,,,,,,,,,,,,,,,,,*@@@(  
     @@@@@@@@@@@@@&&%%%%%%@@@@######,,,,,,,,,,,,,,/###@@@#  
    @@@@@%%%%%@@@@&&%%%%%%%@@@@######################@@@@*  
    @@@@%%%%%&@@@&&&&%%%%%%%@@@@@@##############%@@@@@@@%   
    @@@@&&&&&&@@@&&&&%%%%%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@     
    @@@@&&&&&&@@@&&&&%%%%%%%%%%%%%@@@@@@@@@%%%%%%%%@@@@     
   .@@@@&&&&&&@@@&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%&@@@@%    
   /@@@&&&&&&&@@@&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%&@@@@@    
   /@@@&&&&&&&@@@&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%&@@@@@    
   /@@@&&&&&&&@@@&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%&&@@@@@    
   /@@@&&&&&&&@@@&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%&&&&@@@@,    
    @@@@&&&&&&@@@@&&&&&&&&&&&&&&&&&&%%&&&&&&&&&&&&&@@@@     
    @@@@@&&&&&@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@     
     @@@@@@@@@@@@@&&&&&&&&&&&&&@@@&&&&&&&&&&&&&&&&@@@@      
       (@@@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@@@&&&&&&@@@@@      
              @@@@&&&&&&&&&&&@@@@@  @@@@&&&&&&&&&@@@@*      
              %@@@&&&&&&&&&&&@@@@@  @@@@&&&&&&&&&@@@@       
               @@@@&&&&&&&&&&@@@@@   @@@@&&&&&&&@@@@*       
               @@@@@&&&&&&&&@@@@@     @@@@@@@@@@@@     
                @@@@@@@@@@@@@@@

 AMONGUS
""")

def knee():
    print("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%#&&%/#&&&&&&&&(#&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&&&&&&&%&&&&#&&%#%&&&&&&%#%&%&&&&%%&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&%&&&&&%&&%%%%%##%%%%%%%%&&&&%%&%%(##(%&&&&%&(#%&%&%&%#%%%&&&&&&&&&&&&&&&&&&&&
&&&&&&&&%%&%%&&&&&&&&&&&%%%&&&%%%%%&&&%%%%%%%#%%%%%%%&#((%%%%%%/#%(##(###%&%%&&&%%%%%%%%&&&&&&&&&&&&
&%%%%&%&&&&&&%%%%%%%&%%%%%%%%%%%%%%%%%%%%%%%%%%%##%%##(#%%((*((#%%%###%%%%%&%%%%%%%%%%%&&&&&&&&&%%%&
%&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##%#(((((%%#(((#%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(#(###((%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(((###(#((#((%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%################((((((//((//****(#######%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(((((#((((((((#(((((#(/#(((((((((##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(((((((###(##(#(####((/***,,/,***//(/(/((///(%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%#(///(((/((((((((((##(((/(((/(((((((((#((((/**/*******(##%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%#((#########%#####((((#####(((/****,*,*,*((((/(*/(((/(/(/*,/#%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%#///(/*//((((((####(((((##(((**/((((##%%%%%%%&&&&%#((//(///((//*,/##%%%%%%%%%%%%%%%%%
%%%%%%%%%%##%%%%%%%%&%%%%(/((((((####((//**/(%%%%&&%&&&&%####%&%%##((((((((((((/**##%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%&&@@(*/#%&&&&%&%##%%#%%%&&@@&%(*,.   (%@,@@&%%%%##(/*****,**////(//##%%%%%%%%%%%%%
%%%%(**,,*/(((((((((###########(((///**///(%&&&&%%%%%####(((((///////**//(((((((((((((//(//**/((#%%%
(/,,,,,,,............,,**((((/((##((#,,,,,,,,,,,,,,,,,,,,,**////((((((((((###########%#####((((##%%%
*,,,***(#*.....,,,***//((((((((/*,,,,,,,,,,,,,...,,.,,,,***//(((((((###%%#(#################(((((/(#
(**///(#/,,,,,.,,,,,,*,,****/*,,,,,,,,,,,,,,,,,,,,,,,*****/(//(((((((((%##(((((#####%#######(((((((#
#((((/((((,,,,,,,,,,,,,,,,,,,*,,,,,,,,,,,,,,,*******///(((((((((((((##((((((((###(###%%#####((((##%%
%%#(//(/*//((**********,,,***/****,**/******////(/((((((((((((#%%##((((((((((#((############(((#(##%
%%%%%#(//***/*/(((((//(((((((((((((*//((((((((((((((#%%&&%####(#((((((((((((######%####(((((##%%%%%%
%%%%%%%%#((****/**/(((##(((((((###%%%%&&&&&%%%%%%########(((#(((####(######%#######(((((#(%%%%%%%%%%
%%%%%%%%%%%%%#(/***(((((((###################################################(((((#(((%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%#(*///((((((##############(#((#(###(#(##(###############((((((##%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%#(//((((######################################(((###%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(#((((#####################%#%###%##(#(%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#((((###%##%#%%##%%#%%###%%#%#(%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(((#(######%#%#%#%###(#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(((##((#(((((#(##((%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(##((((((((((#(#((((#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&%
%%%&%&&&%&&&%&&%%%%%%%&%%%%%%%%%%%%%%%%(((((#((((((((#((##(((((%%%%%%%%%%%%%%%%%%%%%%%%%%&&&%&&&%&&&
&&&%%%%%%%%%&&%%&%%%%&%%%%%%%%%%%%%#(((((#(#(((((#(((((((((((#(((##(#####%%%&%%&%%%%%%%&%%%%%&&&&&&&
&&#(%#/%((/%%%#(((//((//(((((######%%#####(###(#(((((#(#(#(((((###########(((((((((/((///(#%%%&&&&&&
""")

# ─── NEW COMMANDS ─────────────────────────────────────────────────────────────
def show_datetime():
    from datetime import datetime
    now = datetime.now()
    print(f'\n{C.CYAN}Date: {C.WHITE}' + now.strftime('%A, %d %B %Y') + C.RESET)
    print(f'{C.CYAN}Time: {C.WHITE}' + now.strftime('%H:%M:%S') + C.RESET)

def whoami():
    print(f'\n{C.CYAN}Logged in as: {C.WHITE}' + user + C.RESET)

def type_file(filename):
    if not filename:
        print('Usage: TYPE [filename]')
        return
    path = os.path.join('files', filename)
    if not os.path.exists(path):
        print(f'{C.RED}File not found: ' + filename + C.RESET)
        return
    if os.path.isdir(path):
        print(filename + ' is a directory, not a file.')
        return
    try:
        with open(path, 'r', encoding='utf-8') as f:
            print('\n' + f.read())
    except Exception as e:
        print('Error reading file: ' + str(e))

def del_file(filename):
    if not filename:
        print('Usage: DEL [filename]')
        return
    path = os.path.join('files', filename)
    if not os.path.exists(path):
        print(f'{C.RED}File not found: ' + filename + C.RESET)
        return
    if os.path.isdir(path):
        print('Cannot delete a directory with DEL.')
        return
    confirm = input("Are you sure you want to delete '" + filename + "'? [y/n]: ").strip().lower()
    if confirm == 'y':
        os.remove(path)
        print(f'{C.GREEN}Deleted: ' + filename + C.RESET)
    else:
        print('Deletion cancelled.')

def notepad():
    folder = 'files'
    if not os.path.exists(folder):
        print(f"{C.RED}ERROR: Folder 'files' does not exist!{C.RESET}")
        print("Please create a folder named 'files' manually in the same directory as this script.")
        print("Then run NOTEPAD again.")
        return
    filename = input('Enter filename (e.g. note.txt): ').strip()
    if not filename:
        print('No filename given.')
        return
    path = os.path.join(folder, filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            existing = f.read()
        print('\nFile exists. Current content:')
        print('-' * 40)
        print(existing)
        print('-' * 40)
    else:
        print('\nNew file: ' + filename)
    print('Type your text below.')
    print('  SAVE  -> save and exit')
    print('  QUIT  -> cancel without saving')
    print('-' * 40)
    lines = []
    while True:
        line = input()
        if line.strip().upper() == 'SAVE':
            with open(path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
            print(f'{C.GREEN}Saved: ' + filename + C.RESET)
            break
        elif line.strip().upper() == 'QUIT':
            print('Cancelled. File not saved.')
            break
        else:
            lines.append(line)

def taskmgr():
    print(f'\n{C.CYAN}=== TASK MANAGER ==={C.RESET}')
    print(f'\n{C.YELLOW}System:{C.RESET}')
    print('  OS:        ' + platform.system() + ' ' + platform.release())
    print('  Version:   ' + platform.version())
    print('  Machine:   ' + platform.machine())
    print('  Processor: ' + (platform.processor() or 'N/A'))
    print('  Python:    ' + platform.python_version())
    print('  User:      ' + user)

    try:
        import psutil
        mem = psutil.virtual_memory()
        cpu = psutil.cpu_percent(interval=1)
        print(f'\n{C.YELLOW}Resources:{C.RESET}')
        bar_len = 20
        cpu_bar = '[' + '#' * int(cpu/100*bar_len) + '-' * (bar_len - int(cpu/100*bar_len)) + ']'
        mem_bar = '[' + '#' * int(mem.percent/100*bar_len) + '-' * (bar_len - int(mem.percent/100*bar_len)) + ']'
        print('  CPU Usage:  ' + cpu_bar + ' ' + str(round(cpu, 1)) + '%')
        print('  RAM Total:  ' + str(mem.total // (1024**2)) + ' MB')
        print('  RAM Used:   ' + mem_bar + ' ' + str(round(mem.percent, 1)) + '% (' + str(mem.used // (1024**2)) + ' MB)')
        print('  RAM Free:   ' + str(mem.available // (1024**2)) + ' MB')

        print(f'\n{C.YELLOW}Top Processes (by memory):{C.RESET}')
        procs = []
        for proc in psutil.process_iter(['pid', 'name', 'memory_percent', 'status']):
            try:
                procs.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        procs.sort(key=lambda x: x.get('memory_percent', 0), reverse=True)
        print('  ' + 'PID'.ljust(8) + 'Name'.ljust(28) + 'Mem%'.rjust(6) + '  Status')
        print('  ' + '-'*8 + '-'*28 + '-'*6 + '--' + '-'*10)
        for p in procs[:12]:
            name = (p['name'] or 'N/A')[:27]
            print('  ' + str(p['pid']).ljust(8) + name.ljust(28) + str(round(p['memory_percent'],2)).rjust(6) + '%  ' + str(p.get('status','?')))
    except ImportError:
        print('\npsutil not installed. Run: pip install psutil')

    print(f'\n{C.YELLOW}GPU(s):{C.RESET}')
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        if not gpus:
            print('  No GPUs detected by GPUtil.')
        for gpu in gpus:
            bar_len = 20
            load_pct = gpu.load * 100
            vram_pct = gpu.memoryUtil * 100
            load_bar = '[' + '#' * int(load_pct/100*bar_len) + '-' * (bar_len - int(load_pct/100*bar_len)) + ']'
            vram_bar = '[' + '#' * int(vram_pct/100*bar_len) + '-' * (bar_len - int(vram_pct/100*bar_len)) + ']'
            print('  [GPU ' + str(gpu.id) + '] ' + gpu.name)
            print('    Load:  ' + load_bar + ' ' + str(round(load_pct, 1)) + '%')
            print('    VRAM:  ' + vram_bar + ' ' + str(round(vram_pct, 1)) + '% (' + str(round(gpu.memoryUsed)) + ' MB / ' + str(round(gpu.memoryTotal)) + ' MB)')
            print('    Temp:  ' + str(gpu.temperature) + ' C')
    except ImportError:
        print(f'  {C.RED}GPUtil not installed. Run: pip install gputil{C.RESET}')
    except Exception as e:
        print('  GPU error: ' + str(e))

def file_dir():
    folder_path = 'files'
    if not os.path.exists(folder_path):
        print("Folder 'files' does not exist! Create it manually first.")
        return
    items = os.listdir(folder_path)
    if not items:
        print('Folder is empty.')
        return
    print(f"\n{C.CYAN}Contents of 'files':{C.RESET}")
    for item in items:
        full = os.path.join(folder_path, item)
        if os.path.isdir(full):
            print('  [DIR] ' + item)
        else:
            print('  ' + item.ljust(32) + str(os.path.getsize(full)) + ' bytes')

# ─── SAFE CALCULATOR ──────────────────────────────────────────────────────────
def safe_eval(expr):
    allowed_ops = {
        ast.Add: op_module.add, ast.Sub: op_module.sub,
        ast.Mult: op_module.mul, ast.Div: op_module.truediv,
        ast.Pow: op_module.pow, ast.USub: op_module.neg,
        ast.Mod: op_module.mod, ast.FloorDiv: op_module.floordiv,
    }
    def _eval(node):
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.BinOp):
            return allowed_ops[type(node.op)](_eval(node.left), _eval(node.right))
        elif isinstance(node, ast.UnaryOp):
            return allowed_ops[type(node.op)](_eval(node.operand))
        else:
            raise ValueError('Unsupported expression')
    return _eval(ast.parse(expr, mode='eval').body)

def calculator():
    print('\nWelcome to the Calculator!')
    print('Supported: + - * / ** % //')
    print("Type 'exit' to return to the main menu.")
    while True:
        try:
            expression = input('calc> ').strip()
            if expression.lower() == 'exit':
                print('Exiting calculator.')
                break
            if not expression:
                continue
            result = safe_eval(expression)
            print('= ' + str(result))
        except Exception as e:
            print('Error: ' + str(e))

# ─── GAMES ────────────────────────────────────────────────────────────────────
def snake_game():
    WIDTH, HEIGHT = 30, 15
    snake = [(5, 5)]
    direction = (0, 1)
    food = (random.randint(0, HEIGHT - 1), random.randint(0, WIDTH - 1))
    score = 0
    game_over = False

    def draw_board():
        full_clear()
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if (y, x) in snake:
                    print('O', end='')
                elif (y, x) == food:
                    print('X', end='')
                else:
                    print('.', end='')
            print()
        print('Score: ' + str(score))

    def move_snake():
        nonlocal snake, food, score, game_over
        head = snake[0]
        new_head = (head[0] + direction[0], head[1] + direction[1])
        if (new_head in snake or new_head[0] < 0 or new_head[1] < 0 or
                new_head[0] >= HEIGHT or new_head[1] >= WIDTH):
            game_over = True
            return
        snake.insert(0, new_head)
        if new_head == food:
            score += 1
            food = (random.randint(0, HEIGHT - 1), random.randint(0, WIDTH - 1))
        else:
            snake.pop()

    def on_press(key):
        nonlocal direction
        try:
            if key == keyboard.Key.up and direction != (1, 0):
                direction = (-1, 0)
            elif key == keyboard.Key.down and direction != (-1, 0):
                direction = (1, 0)
            elif key == keyboard.Key.left and direction != (0, 1):
                direction = (0, -1)
            elif key == keyboard.Key.right and direction != (0, -1):
                direction = (0, 1)
        except AttributeError:
            pass

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    while not game_over:
        draw_board()
        move_snake()
        time.sleep(0.2)
    print('Game Over!')
    print('Your final score was: ' + str(score))
    listener.stop()

def tetris_game():
    WIDTH, HEIGHT = 10, 20
    board = [[0] * WIDTH for _ in range(HEIGHT)]
    tetrominoes = [
        [[1, 1, 1, 1]],
        [[1, 1], [1, 1]],
        [[0, 1, 0], [1, 1, 1]],
        [[1, 1, 0], [0, 1, 1]],
        [[0, 1, 1], [1, 1, 0]],
        [[1, 0, 0], [1, 1, 1]],
        [[0, 0, 1], [1, 1, 1]]
    ]
    current_piece = random.choice(tetrominoes)
    piece_x, piece_y = 3, 0
    game_over = False
    score = 0

    def draw_board():
        full_clear()
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if (y - piece_y >= 0 and y - piece_y < len(current_piece) and
                        x - piece_x >= 0 and x - piece_x < len(current_piece[0]) and
                        current_piece[y - piece_y][x - piece_x]):
                    print('X', end='')
                elif board[y][x]:
                    print('#', end='')
                else:
                    print('.', end='')
            print()
        print('Score: ' + str(score))
        print('Arrows to control, spacebar to rotate')

    def check_collision(x_offset, y_offset):
        for y, row in enumerate(current_piece):
            for x, cell in enumerate(row):
                if cell:
                    nx = x + piece_x + x_offset
                    ny = y + piece_y + y_offset
                    if nx < 0 or nx >= WIDTH or ny >= HEIGHT or board[ny][nx]:
                        return True
        return False

    def merge_piece():
        for y, row in enumerate(current_piece):
            for x, cell in enumerate(row):
                if cell:
                    board[y + piece_y][x + piece_x] = 1

    def clear_lines():
        nonlocal score
        new_board = [row for row in board if not all(row)]
        lines_cleared = HEIGHT - len(new_board)
        board[:lines_cleared] = [[0] * WIDTH for _ in range(lines_cleared)]
        score += lines_cleared * 10

    def rotate_piece():
        nonlocal current_piece
        rotated = list(zip(*current_piece[::-1]))
        if not check_collision(0, 0):
            current_piece = rotated

    def move_piece(dx, dy):
        nonlocal piece_x, piece_y, game_over
        if not check_collision(dx, dy):
            piece_x += dx
            piece_y += dy
        elif dy > 0:
            merge_piece()
            clear_lines()
            spawn_new_piece()

    def spawn_new_piece():
        nonlocal current_piece, piece_x, piece_y, game_over
        current_piece = random.choice(tetrominoes)
        piece_x, piece_y = 3, 0
        if check_collision(0, 0):
            game_over = True

    def on_press(key):
        try:
            if key == keyboard.Key.left:
                move_piece(-1, 0)
            elif key == keyboard.Key.right:
                move_piece(1, 0)
            elif key == keyboard.Key.down:
                move_piece(0, 1)
            elif key == keyboard.Key.space:
                rotate_piece()
        except AttributeError:
            pass

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    while not game_over:
        draw_board()
        move_piece(0, 1)
        time.sleep(0.5)
    print('Game Over!')
    print('Your final score was: ' + str(score))
    listener.stop()

def rock_paper_scissors():
    print('\nWelcome to Rock, Paper, Scissors!')
    options = ['rock', 'paper', 'scissors']
    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'exit'): ").strip().lower()
        if user_choice == 'exit':
            break
        if user_choice not in options:
            print('Invalid choice.')
            continue
        computer_choice = random.choice(options)
        print('Computer chose: ' + computer_choice)
        if user_choice == computer_choice:
            print("It's a tie!")
        elif ((user_choice == 'rock' and computer_choice == 'scissors') or
              (user_choice == 'paper' and computer_choice == 'rock') or
              (user_choice == 'scissors' and computer_choice == 'paper')):
            print(f'{C.GREEN}You win!{C.RESET}')
        else:
            print(f'{C.RED}You lose!{C.RESET}')

def tic_tac_toe():
    board = [' ' for _ in range(9)]
    player_marker = 'X'
    computer_marker = 'O'

    def display_board():
        print('\n ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
        print('---+---+---')
        print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
        print('---+---+---')
        print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

    def check_winner(marker):
        wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        return any(all(board[i] == marker for i in w) for w in wins)

    def player_move():
        while True:
            try:
                move = int(input('Enter position (1-9): ')) - 1
                if board[move] == ' ':
                    board[move] = player_marker
                    break
                else:
                    print('Spot taken, try again.')
            except (ValueError, IndexError):
                print('Invalid input.')

    def computer_move():
        available = [i for i, x in enumerate(board) if x == ' ']
        board[random.choice(available)] = computer_marker

    game_over = False
    while not game_over:
        display_board()
        player_move()
        if check_winner(player_marker):
            display_board()
            print(f'{C.GREEN}Congratulations, you win!{C.RESET}')
            break
        if ' ' not in board:
            display_board()
            print("It's a tie!")
            break
        computer_move()
        if check_winner(computer_marker):
            display_board()
            print(f'{C.RED}Computer wins! Better luck next time.{C.RESET}')
            break
        if ' ' not in board:
            display_board()
            print("It's a tie!")
            break

def sapper_game():
    def create_board(size, mines):
        board = [[' ' for _ in range(size)] for _ in range(size)]
        mine_positions = set()
        while len(mine_positions) < mines:
            mine = (random.randint(0, size-1), random.randint(0, size-1))
            mine_positions.add(mine)
        for (x, y) in mine_positions:
            board[x][y] = '*'
        return board, mine_positions

    def print_board(board, revealed):
        size = len(board)
        print('  ' + ' '.join(str(i) for i in range(size)))
        for x in range(size):
            row = str(x) + ' '
            for y in range(size):
                row += (board[x][y] if revealed[x][y] else '.') + ' '
            print(row)

    def count_adjacent(x, y, size, mines):
        return sum(1 for dx, dy in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
                   if 0 <= x+dx < size and 0 <= y+dy < size and (x+dx, y+dy) in mines)

    def reveal(x, y, size, board, revealed, mines):
        if revealed[x][y] or board[x][y] == '*':
            return
        adj = count_adjacent(x, y, size, mines)
        board[x][y] = str(adj) if adj > 0 else ' '
        revealed[x][y] = True
        if adj == 0:
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < size and 0 <= ny < size:
                    reveal(nx, ny, size, board, revealed, mines)

    size, mines_count = 8, 10
    board, mine_positions = create_board(size, mines_count)
    revealed = [[False]*size for _ in range(size)]
    game_over = False

    while not game_over:
        print_board(board, revealed)
        try:
            x, y = map(int, input('Enter coordinates (x y): ').split())
        except ValueError:
            print('Invalid input.')
            continue
        if not (0 <= x < size and 0 <= y < size):
            print('Out of bounds.')
            continue
        if (x, y) in mine_positions:
            print(f'{C.RED}BOOM! You hit a mine!{C.RESET}')
            game_over = True
        else:
            reveal(x, y, size, board, revealed, mine_positions)
            if all(revealed[x][y] or board[x][y] == '*' for x in range(size) for y in range(size)):
                print(f'{C.GREEN}Congratulations, you won!{C.RESET}')
                game_over = True

def type_test():
    sentences = [
        'The quick brown fox jumps over the lazy dog.',
        'Python is an amazing programming language.',
        'I love coding in my free time.',
        'Never stop learning, because life never stops teaching.',
        'Type tests can improve your typing speed over time.',
        'Python OS .PY Edition is the best MS-DOS clone.',
    ]
    sentence = random.choice(sentences)
    print('\nType the following sentence as fast as you can:\n')
    print("'" + sentence + "'\n")
    input('Press Enter to start...')
    start_time = time.time()
    typed = input('\nStart typing: ').strip()
    end_time = time.time()
    elapsed = end_time - start_time
    wpm = len(typed.split()) / (elapsed / 60)
    if typed == sentence:
        print('\nWell done! Correct in ' + str(round(elapsed, 2)) + 's. Speed: ' + str(round(wpm, 1)) + ' WPM')
    else:
        print('\nNot quite right.')
        print('Expected: ' + sentence)
        print('You typed: ' + typed)
        print('Time: ' + str(round(elapsed, 2)) + 's | Speed: ' + str(round(wpm, 1)) + ' WPM')

def blackjack_game():
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    RANKS = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    VALUES = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,
              'Jack':10,'Queen':10,'King':10,'Ace':11}

    def create_deck():
        deck = [(r, s) for s in SUITS for r in RANKS]
        random.shuffle(deck)
        return deck

    def score(hand):
        s = sum(VALUES[c[0]] for c in hand)
        aces = sum(1 for c in hand if c[0] == 'Ace')
        while s > 21 and aces:
            s -= 10
            aces -= 1
        return s

    def show_hand(name, hand):
        print(name + "'s Hand: " + ', '.join(c[0] + ' of ' + c[1] for c in hand))
        print(name + "'s Score: " + str(score(hand)) + '\n')

    while True:
        deck = create_deck()
        ph = [deck.pop(), deck.pop()]
        dh = [deck.pop(), deck.pop()]
        show_hand('Player', ph)
        print("Dealer's Hand: " + dh[0][0] + ' of ' + dh[0][1] + ' and [Hidden]\n')
        while score(ph) < 21:
            action = input('[h]it or [s]tand? ').lower()
            if action == 'h':
                ph.append(deck.pop())
                show_hand('Player', ph)
            elif action == 's':
                break
        if score(ph) > 21:
            print(f'{C.RED}Bust! Dealer wins.{C.RESET}')
        else:
            show_hand('Dealer', dh)
            while score(dh) < 17:
                dh.append(deck.pop())
                show_hand('Dealer', dh)
            ps, ds = score(ph), score(dh)
            if ds > 21 or ps > ds:
                print(f'{C.GREEN}Player wins!{C.RESET}')
            elif ps < ds:
                print(f'{C.RED}Dealer wins!{C.RESET}')
            else:
                print("It's a tie!")
        if input('\nPlay again? [y/n]: ').lower() != 'y':
            break

def maze_game():
    WIDTH, HEIGHT = 23, 13
    player_x, player_y = 1, 1
    exit_x, exit_y = WIDTH - 2, HEIGHT - 2
    maze = []
    running = True

    def create_empty_maze():
        return [['#' for _ in range(WIDTH)] for _ in range(HEIGHT)]

    def generate_maze(x, y):
        directions = [(0,-2),(0,2),(-2,0),(2,0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 1 <= nx < WIDTH-1 and 1 <= ny < HEIGHT-1 and maze[ny][nx] == '#':
                maze[ny][nx] = ' '
                maze[y+dy//2][x+dx//2] = ' '
                generate_maze(nx, ny)

    def print_maze():
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in maze:
            print(''.join(row))
        print()

    def init_game():
        nonlocal player_x, player_y, maze
        player_x, player_y = 1, 1
        maze = create_empty_maze()
        maze[player_y][player_x] = ' '
        generate_maze(player_x, player_y)
        maze[player_y][player_x] = 'P'
        maze[exit_y][exit_x] = 'E'

    def move(dx, dy):
        nonlocal player_x, player_y, running
        nx, ny = player_x+dx, player_y+dy
        if maze[ny][nx] in (' ', 'E'):
            maze[player_y][player_x] = ' '
            maze[ny][nx] = 'P'
            player_x, player_y = nx, ny
            print_maze()
            if (player_x, player_y) == (exit_x, exit_y):
                print(f'{C.GREEN}Congratulations! You reached the exit!{C.RESET}')
                running = False

    def on_press(key):
        nonlocal running
        try:
            if key == keyboard.Key.up: move(0, -1)
            elif key == keyboard.Key.down: move(0, 1)
            elif key == keyboard.Key.left: move(-1, 0)
            elif key == keyboard.Key.right: move(1, 0)
        except AttributeError:
            pass
        if not running:
            return False

    while True:
        init_game()
        print_maze()
        running = True
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
        if input('Play again? [y/n]: ').lower() != 'y':
            break

def weather(city):
    import urllib.request
    if not city:
        city = input('Enter city name: ').strip()
    if not city:
        print('No city given.')
        return
    url = 'https://wttr.in/' + city.replace(' ', '+') + '?A'
    print('Fetching weather for: ' + city + '...')
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'curl/7.68.0'})
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = resp.read().decode('utf-8')
        print(data)
    except urllib.error.URLError as e:
        print(f'{C.RED}Connection error: {e.reason}{C.RESET}')
    except Exception as e:
        print(f'{C.RED}Error: {e}{C.RESET}')

def browser():
    try:
        from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit,
            QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QProgressBar, QLabel)
        from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings, QWebEnginePage
        from PyQt5.QtCore import QUrl, Qt
        from PyQt5.QtGui import QIcon
        import sys

        app = QApplication.instance() or QApplication(sys.argv)

        class BrowserWindow(QMainWindow):
            def __init__(self):
                super().__init__()
                self.setWindowTitle('PythonOS Browser 0.1')
                self.setGeometry(100, 100, 1280, 800)
                self.setStyleSheet("""
                    QMainWindow { background: #1e1e1e; }
                    QWidget#toolbar { background: #2d2d2d; padding: 4px; }
                    QLineEdit {
                        background: #3a3a3a; color: #ffffff;
                        border: 1px solid #555; border-radius: 12px;
                        padding: 4px 12px; font-size: 13px;
                    }
                    QLineEdit:focus { border: 1px solid #4fc3f7; }
                    QPushButton {
                        background: #3a3a3a; color: #ffffff;
                        border: 1px solid #555; border-radius: 6px;
                        padding: 4px 10px; font-size: 14px; min-width: 30px;
                    }
                    QPushButton:hover { background: #4a4a4a; }
                    QPushButton:pressed { background: #222; }
                    QProgressBar {
                        background: #2d2d2d; border: none; height: 3px;
                        text-align: center;
                    }
                    QProgressBar::chunk { background: #4fc3f7; }
                    QLabel { color: #aaaaaa; font-size: 11px; padding: 0 6px; }
                """)

                class SilentPage(QWebEnginePage):
                    def javaScriptConsoleMessage(self, level, msg, line, src):
                        pass  # suppress all JS console output

                self.view = QWebEngineView()
                self.view.setPage(SilentPage(self.view))
                self.view.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
                self.view.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
                self.view.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)

                # Toolbar
                self.url_bar = QLineEdit()
                self.url_bar.setPlaceholderText('Enter URL or search...')
                self.url_bar.returnPressed.connect(self.navigate)

                btn_back    = QPushButton('◀')
                btn_forward = QPushButton('▶')
                btn_reload  = QPushButton('↻')
                btn_home    = QPushButton('⌂')
                btn_back.clicked.connect(self.view.back)
                btn_forward.clicked.connect(self.view.forward)
                btn_reload.clicked.connect(self.view.reload)
                btn_home.clicked.connect(lambda: self.load_url('https://google.com'))

                self.status = QLabel('Ready')

                self.progress = QProgressBar()
                self.progress.setMaximumHeight(3)
                self.progress.setTextVisible(False)
                self.progress.hide()

                nav = QHBoxLayout()
                nav.setSpacing(4)
                for btn in (btn_back, btn_forward, btn_reload, btn_home):
                    nav.addWidget(btn)
                nav.addWidget(self.url_bar)

                toolbar_widget = QWidget()
                toolbar_widget.setObjectName('toolbar')
                toolbar_widget.setLayout(nav)

                layout = QVBoxLayout()
                layout.setSpacing(0)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.addWidget(toolbar_widget)
                layout.addWidget(self.progress)
                layout.addWidget(self.view)
                layout.addWidget(self.status)

                container = QWidget()
                container.setLayout(layout)
                self.setCentralWidget(container)

                self.view.urlChanged.connect(self.on_url_change)
                self.view.loadStarted.connect(self.on_load_start)
                self.view.loadProgress.connect(self.on_load_progress)
                self.view.loadFinished.connect(self.on_load_finished)
                self.view.titleChanged.connect(lambda t: self.setWindowTitle(t + ' — PythonOS Browser'))

                self.load_url('https://google.com')

            def load_url(self, url):
                if not url.startswith('http'):
                    url = 'https://www.google.com/search?q=' + url.replace(' ', '+')
                self.view.setUrl(QUrl(url))

            def navigate(self):
                self.load_url(self.url_bar.text().strip())

            def on_url_change(self, url):
                self.url_bar.setText(url.toString())

            def on_load_start(self):
                self.progress.show()
                self.progress.setValue(0)
                self.status.setText('Loading...')

            def on_load_progress(self, val):
                self.progress.setValue(val)

            def on_load_finished(self, ok):
                self.progress.hide()
                self.status.setText('Done' if ok else 'Failed to load page')

        win = BrowserWindow()
        win.show()
        app.exec_()

    except ImportError:
        print(f'{C.RED}PyQt5 not installed.{C.RESET}')
        print('Run: pip install PyQt5 PyQtWebEngine')


# ─── BOOT ─────────────────────────────────────────────────────────────────────
user = input('Username: ')
time.sleep(1)
print('\n')
print('                  //,')
print('           /////(((((((((((/')
print('          ///   ((((((((((((')
print('         /(((((((((((((((((')
print('     ,///((((((((((((((((((@  ,,,,')
print('  /////((((((((((((((((((@@@  ,,,,,,,')
print(' ////((((((((((((((((((@@@@@ ,,,,,,,,,')
print(' //((((((((((((((((((@@@@@@ ,,,,,,,,,,')
print(',((((((((((   ,,,,,,,,,,,,,,,,,,,,&&&&&&&&&&&&&')
print(' ((((((((  ,,,,,,,,,,,,,,,,,,,,/&&&&&*      &&&&&.')
print(' (((((((( ,,,,,,,,,,,,,,,,,,,,,/&&&&&       &&&&&.    *&&&&&&&&&&&&')
print('   (((((( ,,,,,,,,,,,,,,,,,,***/&&&&&       &&&&&.  &&&&&')
print('          ,,,,,,,,,,,,,,,***   .&&&&&       &&&&&.    *&&&&&&&&&&&&')
print('          ,,,,,,,,,,,,*  ,**   .&&&&&       &&&&&.               &&&&&')
print('           ,,,,,,,*****   **      &&&&&&&&&&&&&     &&&&&&&&&&&&&&&')
print('             ,,**********')
print('\n')
time.sleep(1)
print('PYTHON OS .PY EDITION 0.1\n')
time.sleep(1.5)
print("Python and the Python logo are copyrighted by the Python Software Foundation © 2001-2026")
time.sleep(3)
print('LOADING DATA FROM FILE. PLEASE WAIT')
time.sleep(1.57)
print('\nWelcome in Py-Dos mode! Please wait! we need to install and load some resources')
time.sleep(0.5)
print('.')
time.sleep(0.5)
print('.')
time.sleep(0.5)
print('.')
time.sleep(0.25)

# ─── MAIN LOOP ────────────────────────────────────────────────────────────────
while True:
    try:
        raw_command = input(f'\n{C.GREEN}C:\\PythonOS\\> {C.RESET}').strip()
    except (KeyboardInterrupt, EOFError):
        print('\nUse EXIT to quit.')
        continue

    command = raw_command.upper()

    if command == 'HELP':
        display_help()
    elif command == 'ASCII':
        display_ascii()
    elif command == 'KNEE':
        knee()
    elif command == 'PYVER':
        display_pyver()
    elif command == 'LICENSE':
        display_license()
    elif command == 'CLEAR':
        clear_screen()
    elif command == 'WHOAMI':
        whoami()
    elif command in ('DATE', 'TIME'):
        show_datetime()
    elif command == 'TASKMGR':
        taskmgr()
    elif command == 'NOTEPAD':
        notepad()
    elif command == 'DIR':
        file_dir()
    elif command.startswith('TYPE '):
        type_file(raw_command[5:].strip())
    elif command.startswith('DEL '):
        del_file(raw_command[4:].strip())
    elif command == 'BROWSER':
        browser()
    elif command.startswith('WEATHER'):
        weather(raw_command[7:].strip())
    elif command == 'BLACKJACK':
        blackjack_game()
    elif command == 'CALC':
        calculator()
    elif command == 'TYPETEST':
        type_test()
    elif command == 'SNAKE':
        snake_game()
    elif command == 'TETRIS':
        tetris_game()
    elif command == 'RPS':
        rock_paper_scissors()
    elif command == 'TICTACTOE':
        tic_tac_toe()
    elif command == 'MINESWEEPER':
        sapper_game()
    elif command == 'MAZE':
        maze_game()
    elif command == 'MYGITHUB':
        print('Redirecting...')
        webbrowser.open('https://github.com/soSoWhatevering')
    elif command == 'GITHUB':
        print('Redirecting...')
        webbrowser.open('https://github.com/')
    elif command == 'EXIT':
        time.sleep(0.8)
        print(f'{C.CYAN}Exiting Py-Dos mode. Goodbye!{C.RESET}')
        time.sleep(0.5)
        break
    else:
        print(f"{C.RED}Unknown command. Type 'HELP' for a list of commands.{C.RESET}")
