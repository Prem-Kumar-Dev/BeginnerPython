def clearBoard():
    global temBoard
    temBoard = {'7': ' ', '8': ' ', '9': ' ', '4': ' ', '5': ' ', '6': ' ', '1': ' ',
                '2': ' ', '3': ' '}


def board():

    print(temBoard['7']+'|'+temBoard['8']+'|'+temBoard['9']+'\n' +
          '-+-+-\n' +
          temBoard['4']+'|'+temBoard['5']+'|'+temBoard['6']+'\n' +
          '-+-+-\n' +
          temBoard['1']+'|'+temBoard['2']+'|'+temBoard['3']+'\n')


def compare(a, b, c):
    if temBoard[a] == 'X' and temBoard[b] == 'X' and temBoard[c] == 'X' or temBoard[a] == 'O' and temBoard[b] == 'O' and temBoard[c] == 'O':
        return True


def win():
    global m
    if compare('7', '8', '9'):
        return True
    elif compare('4', '5', '6'):
        return True
    elif compare('1', '2', '3'):
        return True
    elif compare('7', '5', '3'):
        return True
    elif compare('1', '5', '9'):
        return True
    elif compare('7', '4', '1'):
        return True
    elif compare('9', '6', '3'):
        return True
    elif compare('8', '5', '2'):
        return True


def computer():
    global turn

    def winmove():
        global i, n, copy, lst
        i, n = None, None
        lst = ['O', 'X']
        for i in (lst):
            for n in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if temBoard[n] == ' ':
                    copy = temBoard[n]
                    temBoard[n] = i
                    if win():
                        temBoard[n] = 'O'
                        return True
                    else:
                        temBoard[n] = copy

    def mid():
        if temBoard['5'] == ' ':
            temBoard['5'] = 'O'
            return True

    def corner():
        global i
        i = None
        for i in ['7', '9', '1', '3']:
            if temBoard[i] == ' ':
                temBoard[i] = 'O'
                return True

    def mid_cor():
        global i
        i = None
        for i in ['4', '6', '2', '8']:
            if temBoard[i] == ' ':
                temBoard[i] == 'O'
                return True

    if winmove():
        pass
    elif mid():
        pass
    elif corner():
        pass
    elif mid_cor():
        pass
    turnChanger()


def draw():
    if temBoard['1'] != ' ' and temBoard['2'] != ' ' and temBoard['3'] != ' ' and temBoard['4'] != ' ' and temBoard['5'] != ' ' and temBoard['6'] != ' ' and temBoard['7'] != ' ' and temBoard['8'] != ' ' and temBoard['9'] != ' ':
        print('Match draw')
        return True


def turnChanger():
    global turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'


def play():
    global turn, mode
    turn = 'X'
    clearBoard()
    board()

    def singleplayer():
        global user_input
        while True:
            user_input = input('Enter the block you want to play on:\n(1-9)')
            if temBoard[user_input] == ' ':
                temBoard[user_input] = turn
                board()
                computer()
                board()
                if win():
                    print('Winner:{}'.format(turn))
                    break
                elif draw():
                    break
                turnChanger()

            else:
                print('Block has been use:\n')

    def multiplayer():
        global user_input
        while True:
            user_input = input('Enter the block you want to play on:\n(1-9)')
            if temBoard[user_input] == ' ':
                temBoard[user_input] = turn
                board()
                if win() or draw():
                    print('Winner:{}'.format(turn))
                    break
                turnChanger()

            else:
                print('Block has been use:\n')

    if mode == 'S':
        singleplayer()
    else:
        multiplayer()


mode = input('SinglePlayer(S)\nMultiplayer(M)\n')
while True:
    play()
    play_again = input('Play again:(P) or Exit:(E)')
    if play_again == "E":
        break
