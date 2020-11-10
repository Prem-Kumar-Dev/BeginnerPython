import numpy as np


def value_assign(a, b):
    lst = temBoard[a]


a, b, c, d, e, f, g, h, i = 0, 0, 0, 0, 0, 0, 0, 0, 0

temBoard = {'Top-L': (' ', a), 'Top-M': (' ', b), 'Top-R': (' ', c), 'Mid-L': (' ', d), 'Mid-M': (' ', e), 'Mid-R': (' ', f), 'Low-L': (' ', g),
            'Low-M': (' ', h), 'Low-R': (' ', i)}


def compare(a, b, c):
    if temBoard[a] == turn and temBoard[b] == turn and temBoard[c] == turn:
        return True


'''def win():
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
        return True'''


def board():

    print(temBoard['Top-L'][0]+'|'+temBoard['Top-M'][0]+'|'+temBoard['Top-R'][0]+'\n' +
          '-+-+-\n' +
          temBoard['Mid-L'][0]+'|'+temBoard['Mid-M'][0]+'|'+temBoard['Mid-R'][0]+'\n' +
          '-+-+-\n' +
          temBoard['Low-L'][0]+'|'+temBoard['Low-M'][0]+'|'+temBoard['Low-R'][0]+'\n')


board()
turn = 'X'

for i in range(9):
    print('It is {} to play'.format(turn))
    while True:
        x = input('Name the block where you want to play:\n')
        if x in temBoard.keys():
            break
        if x not in temBoard.keys():
            print("!!Invalid Move!! Move avalable=\n{}".format(temBoard.keys()))
    if turn == 'X':
        temBoard[x][0] = turn
        temBoard[x][1] = 1
    elif turn == 'O':
        temBoard[x][0] = turn
        temBoard[x][1] = 2

    board()

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
