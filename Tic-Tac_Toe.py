def clearBoard():
    global temBoard
    temBoard = {'7': ' ', '8': ' ', '9': ' ', '4': ' ', '5': ' ', '6': ' ', '1': ' ',
                '2': ' ', '3': ' '}


def compare(a, b, c):
    if temBoard[a] == turn and temBoard[b] == turn and temBoard[c] == turn:
        return True


def win():
    global m
    if compare('7', '8', '9'):
        print('Winner:{}'.format(turn))
        return True
    elif compare('4', '5', '6'):
        print('Winner:{}'.format(turn))
        return True
    elif compare('1', '2', '3'):
        print('Winner:{}'.format(turn))
        return True
    elif compare('7', '5', '3'):
        print('Winner:{}'.format(turn))
        return True
    elif compare('1', '5', '9'):
        print('Winner:{}'.format(turn))
        return True
    elif compare('7', '4', '1'):
        print('Winner:{}'.format(turn))
        return True
    elif compare('9', '6', '3'):
        print('Winner:{}'.format(turn))
        return True
    elif compare('8', '5', '2'):
        print('Winner:{}'.format(turn))
        return True


def board():

    print(temBoard['7']+'|'+temBoard['8']+'|'+temBoard['9']+'\n' +
          '-+-+-\n' +
          temBoard['4']+'|'+temBoard['5']+'|'+temBoard['6']+'\n' +
          '-+-+-\n' +
          temBoard['1']+'|'+temBoard['2']+'|'+temBoard['3']+'\n')


def process():
    clearBoard()
    board()
    global turn, lst
    turn = 'X'
    lst = []
    for i in range(9):
        print('It is {} to play'.format(turn))
        while True:
            x = input('Name the block where you want to play:\n')
            if x in lst:
                print('!!!Move Already on the Board. Please choose another move.!!!')
                board()
            elif x not in temBoard.keys():
                print("!!Invalid Move!! Move avalable=\n{}".format(temBoard.keys()))
            else:
                lst.append(x)
                break
        temBoard[x] = turn
        board()
        if win() == True:
            break
        if turn == 'X':
            turn = 'O'
        elif turn == 'O':
            turn = 'X'
        else:
            print('Invalid Input')
            i = i-1
        if i == 8:
            print('Match Draw')


while True:
    process()
    confirm = input('Play Again(Y/N)\n')

    if confirm == 'N':
        print('Thanks For Playing')
        break
