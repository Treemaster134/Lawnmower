import os
import time
import keyboard
import random
mole_cords_y = []
mole_cords_x = []
joe_mama = ['#', '#']
board = []
p1x = 0
p1y = 0
oldp1x = 0
oldp1y = 0

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\u001b[33m'
    OKRED = '\u001b[31m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

for row in range(15):
    board.append([])
    for column in range(30):
        num = bcolors.OKGREEN + '#' + bcolors.ENDC
        board[row].append(num)
board[0][0] = bcolors.OKRED + '凸' + bcolors.ENDC
for _ in range(30):
    sus = random.randrange(1, 14)
    sus2 = random.randrange(1, 29)
    board[sus][sus2] = bcolors.OKBLUE + '✿' + bcolors.ENDC

for _ in range(16):
    sus = random.randrange(1, 14)
    sus2 = random.randrange(1, 29)
    board[sus][sus2] = '●'

for _ in range(2):
    greg = random.randrange(1, 14)
    greg2 = random.randrange(1, 29)
    mole_cords_x.append(greg2)
    mole_cords_y.append(greg)
    
#player = 凸
#rock = ●
#annoying = ☻
#fuel have = ■
#fuel not = □
#flower = ✿

def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)
print('凸●☻■□✿')

def playermove():
    global jeff
    global joe_mama
    global mole_cords_x
    global mole_cords_y
    global p1y
    global p1x
    global oldp1y
    global oldp1x
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('w'):  # if key 'q' is pressed 
                print('You Pressed W Key!')
                key = 'w'
                time.sleep(0.075)
                break  # finishing the loop
            elif keyboard.is_pressed('a'):  # if key 'q' is pressed 
                print('You Pressed A Key!')
                key = 'a'
                time.sleep(0.075)
                break  # finishing the loop
            elif keyboard.is_pressed('s'):  # if key 'q' is pressed 
                print('You Pressed S Key!')
                key = 's'
                time.sleep(0.075)
                break  # finishing the loop
            elif keyboard.is_pressed('d'):  # if key 'q' is pressed 
                print('You Pressed D Key!')
                key = 'd'
                time.sleep(0.075)
                break  # finishing the loop
        except:
            playermove()
    if key == 'w' and p1y != 0:
        p1y -= 1
    elif key == 's' and p1y != 14:
        p1y += 1
    elif key == 'a' and p1x != 0:
        p1x -= 1
    elif key == 'd' and p1x != 29:
        p1x += 1
    
    
    board[oldp1y][oldp1x] = ' '
    oldp1x = p1x
    oldp1y = p1y
    #if board[p1y][p1x] == '☻' or board[p1y][p1x] == '●':


    board[p1y][p1x] = bcolors.OKRED + '凸' + bcolors.ENDC
    eggo = 0
    if p1x == 0 and p1y == 0:
        eggo += 1
    if eggo == 0:
        board[0][0] = '▣'
    
    pleasegodhelp = random.randrange(1, 3)
    if pleasegodhelp == 2:
        jeff = 0
        for _ in range(2):
            pannkakor = mole_cords_y[jeff]
            pannkakor2 = mole_cords_x[jeff]
            if board[pannkakor][pannkakor2] == '\x1b[33m☻\x1b[0m':
                if joe_mama[jeff] == ' ':
                    board[pannkakor][pannkakor2] = ' '
                elif joe_mama[jeff] == '#':
                    board[pannkakor][pannkakor2] = '#'
                elif joe_mama[jeff] == '✿':
                    board[pannkakor][pannkakor2] = '✿'
                elif joe_mama[jeff] == '●':
                    board[pannkakor][pannkakor2] = '●'
            else:
                board[pannkakor][pannkakor2] == ' '
            jeff += 1

        mole_cords_y = []
        mole_cords_x = []
        joe_mama = []
        for _ in range(2):
            greg = random.randrange(1, 14)
            greg2 = random.randrange(1, 29)
            mole_cords_x.append(greg2)
            mole_cords_y.append(greg)
        greg3 = 0
        for _ in range(2):
            hhhhhh = mole_cords_y[greg3]
            hhhhhh2 = mole_cords_x[greg3]
            joe_mama.append(board[hhhhhh][hhhhhh2])
            board[hhhhhh][hhhhhh2] = bcolors.OKYELLOW + '☻' + bcolors.ENDC
            greg += 1


    os.system('cls' if os.name == 'nt' else 'clear')
    print_board(board)
    playermove()

playermove()