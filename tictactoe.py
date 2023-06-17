import random

board =[' ']*10
Player='O'
Robot='X'

def Playboard(board):
    print(f'{board[1]} | {board[2]} | {board[4]}')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print('-'*10)

def Check_winner():
    if board[1]==board[2]==board[3] and board[1]!=' ':
        return True
    elif board[4]==board[5]==board[6] and board[4]!=' ':
        return True
    elif board[7]==board[8]==board[9] and board[7]!=' ':
        return True
    elif board[1]==board[4]==board[7] and board[1]!=' ':
        return True
    elif board[2]==board[5]==board[8] and board[2]!=' ':
        return True
    elif board[3]==board[6]==board[9] and board[3]!=' ':
        return True
    elif board[1]==board[5]==board[9] and board[1]!=' ':
        return True
    elif board[7]==board[5]==board[3] and board[7]!=' ':
        return True
    else:
        return False
    
def Check_Tie():
    if board.count(' ')<2:
        return True
    else:
        return False
    
def Occupied(place):
     return True if board[place]==' 'else False
def Play_Game(symbal,place):
    if Occupied(place):
        board[place]=symbal
        Playboard(board)
        if Check_winner():
            if symbal =='X':
                print(f'Robot is Winner')
                exit()
            else:
                print(f'Player is Winner')
                exit()
        if Check_Tie():
            print(f"It's a tie!")
            exit()
    else:
        if symbal =='O':
            place=int(input('"That position is already filled. Try again'))
        else:
            place=random.randint(1,9)
        Play_Game(symbal,place)                              
def Player_Chance(symbal):
        place=int(input("Enter a position (1-9): "))
        Play_Game(symbal,place)

def Robot_Chance(symbal):
        place=random.randint(1,9)
        Play_Game(symbal,place)

while not Check_winner():
     Playboard(board)
     Player_Chance(Player)
     Robot_Chance(Robot)