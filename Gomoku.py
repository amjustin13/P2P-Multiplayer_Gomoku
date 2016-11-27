#Welcome Message
print("Welcome to Gomoku. The object of the game is to get 5 in a row. ")
print("You can win horizantall, vertically, or diagonally. Have fun! ")


#Player Name
Player1 = str(input('Player 1, Enter your name: '))
print('Hello',Player1)
Player2 = str(input('Player 2, Enter your name: '))
print('Hello', Player2)


#Select Player color
ChooseColor = int(input("Please select color, 1 for black or 2 for white: "))
if ChooseColor == 1:
    print(Player1,": Black")
    print(Player2,": White")
if ChooseColor == 2:
    print(Player1," :White")
    print(Player2," :Black")


#Create Board
tracker = 0
CreateBoard = []
for x in range(0,18):
    CreateBoard.append(["O"] * 19)


def print_board(CreateBoard):
    for row in CreateBoard:
        result1 = " ".join(row)
        print(result1)


#Determine winner of game
def iswinner(CreateBoard):
    CreateBoard_h = len(CreateBoard)
    CreateBoard_w = len(CreateBoard)
    marker = '*'
    marker2 = '%'
    print(CreateBoard_w)
#Check column for winner
    for col_num in range(CreateBoard_h):
        for row_num in range(CreateBoard_w):
            if CreateBoard[row_num][col_num] == marker and CreateBoard[row_num+1][col_num] == marker and CreateBoard[row_num+2][col_num]==marker and CreateBoard[row_num+3][col_num]==marker and CreateBoard[row_num+4][col_num] == marker:
                print(Player1, "You are a winner!")
                #playagain()
            if CreateBoard[row_num][col_num] == marker2 and CreateBoard[row_num+1][col_num] == marker2 and CreateBoard[row_num+2][col_num]==marker2 and CreateBoard[row_num+3][col_num]==marker2 and CreateBoard[row_num+4][col_num] == marker2:
                print(Player2, "You are a winner!")
#Check row for winner
    for row_num in range(CreateBoard_h):
        for col_num in range(CreateBoard_w):
            if CreateBoard[row_num][col_num] == marker and CreateBoard[row_num][col_num+1] == marker and CreateBoard[row_num][col_num+2]==marker and CreateBoard[row_num][col_num+3]==marker and CreateBoard[row_num][col_num+4] == marker:
                print(Player1, "You are a winner1!")
            if CreateBoard[row_num][col_num] == marker2 and CreateBoard[row_num][col_num+1] == marker2 and CreateBoard[row_num][col_num+2]==marker2 and CreateBoard[row_num][col_num+3]==marker2 and CreateBoard[row_num][col_num+4] == marker2:
                print(Player2, "You are a winner1!")
#Check (right to left) diagonal for winner
    for col_num in range(CreateBoard_h):
        for row_num in range(CreateBoard_w):
            if CreateBoard[row_num][col_num] == marker and CreateBoard[row_num+1][col_num+1] == marker and CreateBoard[row_num+2][col_num+2]==marker and CreateBoard[row_num+3][col_num+3]==marker and CreateBoard[row_num+4][col_num+4] == markers:
                print(Player1, "You are a winner2!")
            if CreateBoard[row_num][col_num] == marker2 and CreateBoard[row_num+1][col_num+1] == marker2 and CreateBoard[row_num+2][col_num+2]==marker2 and CreateBoard[row_num+3][col_num+3]==marker2 and CreateBoard[row_num+4][col_num+4] == marker2:
                print(Player2, "You are a winner2!")
#Check (left to right) diagonal for winner
    for col_num in range(CreateBoard_h):
        for row_num in range(CreateBoard_w):
            if CreateBoard[row_num][col_num] == marker and CreateBoard[row_num-1][col_num-1] == marker and CreateBoard[row_num-2][col_num-2]==marker and CreateBoard[row_num-3][col_num-3]==marker and CreateBoard[row_num-4][col_num-4] == marker:
                print(Player1, "You are a winner3!")
            if CreateBoard[row_num][col_num] == marker2 and CreateBoard[row_num-1][col_num-1] == marker2 and CreateBoard[row_num-2][col_num-2]==marker2 and CreateBoard[row_num-3][col_num-3]==marker2 and CreateBoard[row_num-4][col_num-4] == marker2:
                print(Player2, "You are a winner3!")
    # print(row_num,col_num)
    # # for row_num in range(0,17):
    # #     for col_num in range(0,17):
    # if CreateBoard[row_num][col_num] == CreateBoard[row_num][col_num+1]== '*':
    #     print("Yes they are equal")
    # else:
    #     print("No they are not equal")
    #            count = count + 1
    #         if count == 5:
    #             print(Player1, "Wins the game! :)")
    #             break
    # for row_num in range(0,17):
    #     for col_num in range(0,17):
    #         if CreateBoard[row_num][col_num] == CreateBoard[row_num+1][col_num]:
    #             count = count + 1
    #
    #         if count == 5:
    #             print(Player2, "Wins the Game! :)")
    #             break
#    for(row_col = 0 and row_col < 18)
#        i = 0
#        for(col_num = 0 and col_num < 18)
#            i += (CreateBoard[row_col][col_num]) == '*'):
    #if (CreateBoard[row_col][col_num] == CreateBoard[row_col][col_num] == CreateBoard[row_col][col_num] == CreateBoard[row_col][col_num] == CreateBoard[row_col][col_num]):
    # == CreateBoard[7][4]==CreateBoard[7][5] == CreateBoard[7][6] =='*')
        #print ("Player 1 has won")
#print_board(CreateBoard)
#print_board(CreateBoard)

#Would you like to play again?
# def playagain():
#     print("Would you like to play again, Y/N")
#     answer = str(input())
#     if answer == 'Y':
#         main()
#     if answer == 'N':
#         print("Thank you for playing")
#         raise SystemExit()



#Main
while True:
    #print_board(CreateBoard)
    print_board(CreateBoard)
    print (Player1, "enter row number: ")
    row_num = int(input())
    print (Player1, "enter column number: ")
    col_num = int(input())

    if CreateBoard[row_num][col_num] != '*' and CreateBoard[row_num][col_num] != '%':
        CreateBoard[row_num][col_num] = '*'
        print_board(CreateBoard)
        iswinner(CreateBoard)
    else: print("Please select a different spot")
    print_board(CreateBoard)

    #Determine if the code should check for a winner
        # tracker = tracker + 1
        # print(tracker)
        # if tracker >= 9:
        #     iswinner(row_num,col_num,CreateBoard)
        #     print_board(CreateBoard)
        # if tracker < 9:
        #     print_board(CreateBoard)

    print (Player2, "enter row number: ")
    row_num = int(input())
    print (Player2, "enter column number: ")
    col_num = int(input())

    if CreateBoard[row_num][col_num] != '%' and CreateBoard[row_num][col_num] != '*':
        CreateBoard[row_num][col_num] = '%'
        print_board(CreateBoard)
        iswinner(CreateBoard)

    else: print("Please select a different spot")
    print_board(CreateBoard)

#Determine if the code should check for a winner
    # tracker = tracker + 1
    # print(tracker)
    # if tracker >= 9:
    #     iswinner(CreateBoard)
    #     print_board(CreateBoard)
    # if tracker < 9 :
    #    print_board(CreateBoard)
    #    continue


# Create board
# CreateBoard = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,
#               19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,
#               39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,
#               59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,
#               79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,
#               99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,
#               119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,
#               139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,
#               159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,
#               179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,
#               199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,
#               219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,
#               239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,
#               259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,
#               279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,
#               299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,
#               319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,
#               339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,
#               359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378]
# def DisplayBoard () :
#     print   (CreateBoard[0],CreateBoard[1],CreateBoard[2],CreateBoard[3],CreateBoard[4],CreateBoard[5],CreateBoard[6],CreateBoard[7],CreateBoard[8],CreateBoard[9],CreateBoard[10],CreateBoard[11],CreateBoard[12],CreateBoard[13],CreateBoard[14],CreateBoard[15],CreateBoard[16],CreateBoard[17],CreateBoard[18])
#     print   (CreateBoard[19],CreateBoard[20],CreateBoard[21],CreateBoard[22],CreateBoard[23],CreateBoard[24],CreateBoard[25],CreateBoard[26],CreateBoard[27],CreateBoard[28],CreateBoard[29],CreateBoard[30],CreateBoard[31],CreateBoard[32],CreateBoard[33],CreateBoard[34],CreateBoard[35],CreateBoard[36],CreateBoard[37],CreateBoard[38])
#     print   (CreateBoard[39],CreateBoard[40],CreateBoard[41],CreateBoard[42],CreateBoard[43],CreateBoard[44],CreateBoard[45],CreateBoard[46],CreateBoard[47],CreateBoard[48],CreateBoard[49],CreateBoard[50],CreateBoard[51],CreateBoard[52],CreateBoard[53],CreateBoard[54],CreateBoard[55],CreateBoard[56],CreateBoard[57],CreateBoard[58])
#     print   (CreateBoard[59],CreateBoard[60],CreateBoard[61],CreateBoard[62],CreateBoard[63],CreateBoard[64],CreateBoard[65],CreateBoard[66],CreateBoard[67],CreateBoard[68],CreateBoard[69],CreateBoard[70],CreateBoard[71],CreateBoard[72],CreateBoard[73],CreateBoard[74],CreateBoard[75],CreateBoard[76],CreateBoard[77],CreateBoard[78])
#     print   (CreateBoard[79],CreateBoard[80],CreateBoard[81],CreateBoard[82],CreateBoard[83],CreateBoard[84],CreateBoard[85],CreateBoard[86],CreateBoard[87],CreateBoard[88],CreateBoard[89],CreateBoard[90],CreateBoard[91],CreateBoard[92],CreateBoard[93],CreateBoard[94],CreateBoard[95],CreateBoard[96],CreateBoard[97],CreateBoard[98])
#     print   (CreateBoard[99],CreateBoard[100],CreateBoard[101],CreateBoard[102],CreateBoard[103],CreateBoard[104],CreateBoard[105],CreateBoard[106],CreateBoard[107],CreateBoard[108],CreateBoard[109],CreateBoard[110],CreateBoard[111],CreateBoard[112],CreateBoard[113],CreateBoard[114],CreateBoard[115],CreateBoard[116],CreateBoard[117],CreateBoard[118])
#     print   (CreateBoard[119],CreateBoard[120],CreateBoard[121],CreateBoard[122],CreateBoard[123],CreateBoard[124],CreateBoard[125],CreateBoard[126],CreateBoard[127],CreateBoard[128],CreateBoard[129],CreateBoard[130],CreateBoard[131],CreateBoard[132],CreateBoard[133],CreateBoard[134],CreateBoard[135],CreateBoard[136],CreateBoard[137],CreateBoard[138])
#     print   (CreateBoard[139],CreateBoard[140],CreateBoard[141],CreateBoard[142],CreateBoard[143],CreateBoard[144],CreateBoard[145],CreateBoard[146],CreateBoard[147],CreateBoard[148],CreateBoard[149],CreateBoard[150],CreateBoard[151],CreateBoard[152],CreateBoard[153],CreateBoard[154],CreateBoard[155],CreateBoard[156],CreateBoard[157],CreateBoard[158])
#     print   (CreateBoard[159],CreateBoard[160],CreateBoard[161],CreateBoard[162],CreateBoard[163],CreateBoard[164],CreateBoard[165],CreateBoard[166],CreateBoard[167],CreateBoard[168],CreateBoard[169],CreateBoard[170],CreateBoard[171],CreateBoard[172],CreateBoard[173],CreateBoard[174],CreateBoard[175],CreateBoard[176],CreateBoard[177],CreateBoard[178])
#     print   (CreateBoard[179],CreateBoard[180],CreateBoard[181],CreateBoard[182],CreateBoard[183],CreateBoard[184],CreateBoard[185],CreateBoard[186],CreateBoard[187],CreateBoard[188],CreateBoard[189],CreateBoard[190],CreateBoard[191],CreateBoard[192],CreateBoard[193],CreateBoard[194],CreateBoard[195],CreateBoard[196],CreateBoard[197],CreateBoard[198])
#     print   (CreateBoard[199],CreateBoard[200],CreateBoard[201],CreateBoard[202],CreateBoard[203],CreateBoard[204],CreateBoard[205],CreateBoard[206],CreateBoard[207],CreateBoard[208],CreateBoard[209],CreateBoard[210],CreateBoard[211],CreateBoard[212],CreateBoard[213],CreateBoard[214],CreateBoard[215],CreateBoard[216],CreateBoard[217],CreateBoard[218])
#     print   (CreateBoard[219],CreateBoard[220],CreateBoard[221],CreateBoard[222],CreateBoard[223],CreateBoard[224],CreateBoard[225],CreateBoard[226],CreateBoard[227],CreateBoard[228],CreateBoard[229],CreateBoard[230],CreateBoard[231],CreateBoard[232],CreateBoard[233],CreateBoard[234],CreateBoard[235],CreateBoard[236],CreateBoard[237],CreateBoard[238])
#     print   (CreateBoard[239],CreateBoard[240],CreateBoard[241],CreateBoard[242],CreateBoard[243],CreateBoard[244],CreateBoard[245],CreateBoard[246],CreateBoard[247],CreateBoard[248],CreateBoard[249],CreateBoard[250],CreateBoard[251],CreateBoard[252],CreateBoard[253],CreateBoard[254],CreateBoard[255],CreateBoard[256],CreateBoard[257],CreateBoard[258])
#     print   (CreateBoard[259],CreateBoard[260],CreateBoard[261],CreateBoard[262],CreateBoard[263],CreateBoard[264],CreateBoard[265],CreateBoard[266],CreateBoard[267],CreateBoard[268],CreateBoard[269],CreateBoard[270],CreateBoard[271],CreateBoard[272],CreateBoard[273],CreateBoard[274],CreateBoard[275],CreateBoard[176],CreateBoard[177],CreateBoard[178])
#     print   (CreateBoard[279],CreateBoard[280],CreateBoard[281],CreateBoard[282],CreateBoard[283],CreateBoard[284],CreateBoard[285],CreateBoard[286],CreateBoard[287],CreateBoard[288],CreateBoard[289],CreateBoard[290],CreateBoard[291],CreateBoard[293],CreateBoard[293],CreateBoard[294],CreateBoard[295],CreateBoard[296],CreateBoard[297],CreateBoard[298])
#     print   (CreateBoard[299],CreateBoard[300],CreateBoard[301],CreateBoard[302],CreateBoard[303],CreateBoard[304],CreateBoard[305],CreateBoard[306],CreateBoard[307],CreateBoard[308],CreateBoard[309],CreateBoard[310],CreateBoard[311],CreateBoard[312],CreateBoard[313],CreateBoard[314],CreateBoard[315],CreateBoard[316],CreateBoard[317],CreateBoard[318])
#     print   (CreateBoard[319],CreateBoard[320],CreateBoard[321],CreateBoard[322],CreateBoard[323],CreateBoard[324],CreateBoard[325],CreateBoard[326],CreateBoard[327],CreateBoard[328],CreateBoard[329],CreateBoard[330],CreateBoard[331],CreateBoard[332],CreateBoard[333],CreateBoard[334],CreateBoard[335],CreateBoard[336],CreateBoard[337],CreateBoard[338])
#     print   (CreateBoard[339],CreateBoard[340],CreateBoard[341],CreateBoard[342],CreateBoard[343],CreateBoard[344],CreateBoard[345],CreateBoard[346],CreateBoard[347],CreateBoard[348],CreateBoard[349],CreateBoard[350],CreateBoard[351],CreateBoard[352],CreateBoard[353],CreateBoard[354],CreateBoard[355],CreateBoard[356],CreateBoard[357],CreateBoard[358])
#     print   (CreateBoard[359],CreateBoard[360],CreateBoard[361],CreateBoard[362],CreateBoard[363],CreateBoard[364],CreateBoard[365],CreateBoard[366],CreateBoard[367],CreateBoard[368],CreateBoard[369],CreateBoard[370],CreateBoard[371],CreateBoard[372],CreateBoard[373],CreateBoard[374],CreateBoard[375],CreateBoard[376],CreateBoard[377],CreateBoard[378])
#
#     Position1 = int(input('Please enter'))
#     if CreateBoard[row_num][col_num] != '*' and CreateBoard[row_num][col_num] != '%':
#         CreateBoard[row_num][col_num] = '*'
#     print_board(CreateBoard)
#         #print_board(CreateBoard)
#
#     print ("enter row number: ")
#     row_num = int(input())
#     print ("enter column number: ")
#     col_num = int(input())
#
#     if CreateBoard[row_num][col_num] != '%' and CreateBoard[row_num][col_num] != '*':
#         CreateBoard[row_num][col_num] = '%'
#
#     print_board(CreateBoard)
#
