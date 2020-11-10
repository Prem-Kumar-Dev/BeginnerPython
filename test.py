temBoard = {'Top-L': ' ', 'Top-M': ' ', 'Top-R': ' ', 'Mid-L': ' ', 'Mid-M': ' ', 'Mid-R': ' ', 'Low-L': ' ',
            'Low-M': ' ', 'Low-R': ' '}


def compare(a, b, c):
    if temBoard[a] == turn and temBoard[b] == turn and temBoard[c] == turn:
        return True


def win():
    global m
    if compare('Top-L', 'Top-M', 'Top-R'):
        print('Winner:{}'.format(turn))
        return True
    elif compare('Mid-L', 'Mid-M', 'Mid-R'):
        print('Winner:{}'.format(turn))
        return True
    elif compare('Low-L', 'Low-M', 'Low-R'):
        print('Winner:{}'.format(turn))
        return True
    elif compare('Top-L', 'Mid-M', 'Low-R'):
        print('Winner:{}'.format(turn))
        return True
    elif compare('Low-L', 'Mid-M', 'Top-R'):
        print('Winner:{}'.format(turn))
        return True
    elif compare('Top-L', 'Mid-L', 'Low-L'):
        print('Winner:{}'.format(turn))
        return True
    elif compare('Top-R', 'Mid-R', 'Low-R'):
        print('Winner:{}'.format(turn))
        return True
    elif compare('Top-M', 'Mid-M', 'Low-M'):
        print('Winner:{}'.format(turn))
        return True


def board():

    print(temBoard['Top-L']+'|'+temBoard['Top-M']+'|'+temBoard['Top-R']+'\n' +
          '-+-+-\n' +
          temBoard['Mid-L']+'|'+temBoard['Mid-M']+'|'+temBoard['Mid-R']+'\n' +
          '-+-+-\n' +
          temBoard['Low-L']+'|'+temBoard['Low-M']+'|'+temBoard['Low-R']+'\n')


board()
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

print('Play Again')
