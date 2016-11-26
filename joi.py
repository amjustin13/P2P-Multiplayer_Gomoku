import sys
import The_Client

def print_board(CreateBoard):
    for row in CreateBoard:
        result1 = " ".join(row)
        print(result1)

def get_input():
    print ("enter row number: ")
    row_num = int(input())
    print ("enter column number: ")
    col_num = int(input())
    return row_num,col_num

def player1(CreateBoard):
    print("Player 1")
    row_num,col_num = get_input()
    #changed logic to 'or' it can never be both choices
    if(CreateBoard[row_num][col_num] != '%' and CreateBoard[row_num][col_num] != '*'):
        CreateBoard[row_num][col_num] = '*'
        print_board(CreateBoard)
        turn = 1
        with open("game state.txt","w") as file:
            file.write(str(CreateBoard))
        send_post_resp()

    else:
        print("You cannot go there")
        turn = 0
    return turn

def player2(CreateBoard):
    print("player2")
    row_num,col_num = get_input()

    if(CreateBoard[row_num][col_num] != '%' and CreateBoard[row_num][col_num] != '*'):
        CreateBoard[row_num][col_num] = '%'
        print_board(CreateBoard)
        turn = 0
        with open("game state.txt","w") as file:
            file.write(str(CreateBoard))
    else:
        print("You cannot go there")
        turn = 1
    return turn

def CreateBoard():
    CreateBoardArr = []
    for x in range(0,18):
        CreateBoardArr.append(['O'] * 19)
        with open("game state.txt","w") as file:
            file.write(str(CreateBoard))
    return CreateBoardArr
