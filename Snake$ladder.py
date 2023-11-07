def temp_board():
    global board
    board = {key: ' ' for key in range(1, 101)}
    print(board)

def board():
    global a
    board[1]='Start'
    board[100]='End'
    for i in a:
        if i=='Start':
            break
        elif i=='End':
            continue
        else:

            try:
                i = int(i)
            except ValueError:
                snake_ladder(i)

def snake_ladder(x):
    n=x.split("")
    if n[0]=="S":
        snaketo = int(x[x.find("(") + 1 : x.find(")")])
        snaketogo=snaketogo+snaketo
        snakelist=snakelist+x

    elif n[0]=="L":
        ladderto = int(x[x.find("(") + 1 : x.find(")")])
        laddertogo=laddertogo+ladderto
        ladderlist=ladderlist+x

def solution(x):
    global ladderlist, snakelist
    if x==100:
        print("Possible",len(ladderlist),len(snakelist))
        return False
    else:
        print("Not Possible",len(ladderlist),len(snakelist))
        return False
        



def play():
    
    a=input().split()
    temp_board()
    ladderlist=[]
    snakelist=[]
    laddertogo=[]
    snaketogo=[]

    board()
    position=0
    counter=101
    ladder=dict(zip(ladderlist,laddertogo))
    snake=dict(zip(snakelist,snaketogo))
    ladder.update(snake)
    for i in range(101,len(a)+1):
        if counter in ladderlist and counter in snakelist:
            position=int(ladder[counter])
        else:
            position=position+int(a[counter])
    
    solution(position)


play()

        

    
    















