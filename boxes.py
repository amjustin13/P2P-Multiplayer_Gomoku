import pygame
import math
from http.client import HTTPConnection
import http.client
from The_Server import ClientHandler
import os

global board_array
global wait

wait = 0

class GomokuGame(ClientHandler):
    def __init__(self):
        pass
        #Welcome Message
        print("Welcome to Gomoku. The object of the game is to get 5 in a row.")
        print("You can win horizantall, vertically, or diagonally. Have fun!")

        pygame.init()
        pygame.font.init()
        width, height = 580, 680

        #initialize the screen
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Gomoku")
        self.clock=pygame.time.Clock()

        # define array for placement of the boxes
        self.board = [[False for x in range(19)] for y in range(19)]
        self.initGraphics()
        self.initSound()
        self.turn = input("[0] or [1]")
        self.me=0
        self.didiwin=False
        self.running=False
        self.board_array = self.CreateBoard()
        self.data_recieved = self.CreateBoard()
        self.temp = ["20","20"]

        if(self.turn == '0'):
            self.Player1 = str(input('Player 1, Enter your name: '))
            print('Hello',self.Player1)
            self.otherplayer = '0'
        else:
            self.Player2 = str(input('Player 2, Enter your name: '))
            print('Hello', self.Player2)
            self.otherplayer = '1'

    def CreateBoard(self):
        self.CreateBoardArr = []
        for x in range(0,19):
            self.CreateBoardArr.append(['O'] * 19)
        return self.CreateBoardArr

#___________________________PLAYER FUNCTION____________________________________
    def player1(self,row_num,col_num):
        if(self.board_array[row_num][col_num] != '%' and
           self.board_array[row_num][col_num] != '*'):
            if(self.otherplayer == '1'):
                self.board_array[row_num][col_num] = '%'
            else:
                self.board_array[row_num][col_num] = '*'
                self.Check_Operating_Area(self.board_array,row_num,col_num)
        else:
            pass

    def player2(self,row_num,col_num):
        if(self.board_array[row_num][col_num] != '%' and
           self.board_array[row_num][col_num] != '*'):
            if(self.otherplayer == '1'):
                self.board_array[row_num][col_num] = '*'

            else:
                self.board_array[row_num][col_num] = '%'
                self.Check_Operating_Area(self.board_array,row_num,col_num)
        else:
            pass

#___________________________THE CLIENT________________________________________
    def Send_post_req(self, temp):
        conn = http.client.HTTPConnection("149.162.138.211",6000)
        #request command to server
        conn.request("POST","he.txt", temp)

        #get response from server
        response = conn.getresponse()
        print("message value from POST req: ",response.reason)
        self.otherplayer = response.reason
        #print server response and data
        print("printing response...")
        print(int(response.status), response.reason)
        conn.close()

    # --------------------------------
    # Build and update the board!
    # --------------------------------
    def drawBoard(self):
        for x in range(19):
            for y in range(19):
                    self.screen.blit(self.bluesquare, [(x)*30, (y)*30+5])
    def drawHUD(self):
        #draw the background for the bottom and draw text:
        self.screen.blit(self.scorepanel, [0, 580])

        #define fonts
        myfont32 = pygame.font.SysFont(None, 32)
        myfont64 = pygame.font.SysFont(None, 64)
        myfont20 = pygame.font.SysFont(None, 20)

        label = myfont32.render("Your Turn:", 1, (255,255,255))
        scoreme = myfont64.render(str(self.me), 1, (255,255,255))
        scoreother = myfont64.render(str(self.otherplayer), 1, (255,255,255))
        scoretextme = myfont20.render("You", 1, (255,255,255))
        scoretextother = myfont20.render("Other Player", 1, (255,255,255))

        #draw surface
        self.screen.blit(label, (10, 590))
        self.screen.blit(self.greenindicator if self.turn else self.redindicator, (130, 585))
        self.screen.blit(scoretextme, (10, 625))
        self.screen.blit(scoreme, (10, 635))
        self.screen.blit(scoretextother, (280, 625))
        self.screen.blit(scoreother, (340, 635))

    def updateBoard(self):
        if os.stat("C:/Users/marquies/Desktop/he.txt").st_size != 0:

            temp = open("C:/Users/marquies/Desktop/he.txt").read()
            temp = temp.split("b")
            temp = temp[1].split("'")
            temp = temp[1].split(",")

            if(self.turn == '0'):
                self.player1(int(temp[1]), int(temp[0]))
            elif(self.turn == '1'):
                self.player2(int(temp[1]), int(temp[0]))
            #if player 1 cannot make a move,then check for turn
            if(self.otherplayer == '1' and self.turn == '0'):
                if(self.board_array[int(temp[1])][int(temp[0])] == '%' and
                   self.data_recieved[int(temp[0])][int(temp[1])] == 'O'):
                   self.otherplayer = '0'
                   self.data_recieved[int(temp[0])][int(temp[1])] = '1'
                   temp = 0
           #if player 2 cannot make a move, then chekc for turn
            elif(self.otherplayer =='1' and self.turn == '1'):
                if(self.board_array[int(temp[1])][int(temp[0])] == '*' and
                   self.data_recieved[int(temp[1])][int(temp[0])] == 'O'):
                   self.otherplayer = '0'
                   self.data_recieved[int(temp[1])][int(temp[0])] = '1'
                   temp = 0

    def drawPlayerBoard(self):
        for x in range(19):
            for y in range(19):
                if self.board_array[y][x] == '*':
                    self.screen.blit(self.orangecircle, [(x)*30+8, (y)*30+14])
                elif self.board_array[y][x] == '%':
                    self.screen.blit(self.bluecircle, [(x)*30+8, (y)*30+14])
    def update(self):
        global wait
        #sleep to make the game 60 fps
        self.clock.tick(60)

        #clear the screen
        self.screen.fill(0)

        #draw the board
        self.drawBoard()
        self.drawHUD()
        self.updateBoard()
        self.drawPlayerBoard()

        for event in pygame.event.get():
            #quit if the quit button was pressed
            if event.type == pygame.QUIT:
                exit()

        if(self.otherplayer == '0'):#if it is my turn
            #get mouse position
            mouse = pygame.mouse.get_pos()

            #get x and y positions -- will output from(x,y):  (0,0) --> (18,18)
            xpos = int(math.ceil((mouse[0]-32)/30.0))
            ypos = int(math.ceil((mouse[1]-32)/30.0))

            if pygame.mouse.get_pressed()[0]:
                colrowStr = str(xpos) + "," + str(ypos)

                if(self.turn == '0'):
                    self.player1(ypos,xpos)
                    self.Send_post_req(colrowStr)
                    self.otherplayer = '1'
                elif(self.turn == '1'):
                    self.player2(ypos,xpos)
                    self.Send_post_req(colrowStr)
                    self.otherplayer = '1'
                else:
                    print("no players found")
                    exit()
        else:
            pass

        #update the screen
        pygame.display.flip()

    # --------------------------------
    # Initialize Graphics and Sounds!
    # --------------------------------
    def initSound(self):
        pygame.mixer.music.load("music.wav")
        self.winSound = pygame.mixer.Sound('win.wav')
        self.loseSound = pygame.mixer.Sound('lose.wav')
        self.placeSound = pygame.mixer.Sound('place.wav')
        pygame.mixer.music.play()

    def initGraphics(self):
        self.bluesquare=pygame.image.load("square-frame-png-25171.png")
        self.blackcircle=pygame.image.load("blackcircle.png")
        self.bluecircle=pygame.image.load("bluecircle.png")
        self.orangecircle=pygame.image.load("orangecircle.png")
        self.redcircle=pygame.image.load("redcircle.png")
        self.scorepanel=pygame.image.load("score_panel.png")
        self.greenindicator=pygame.image.load("greenindicator.png")
        self.redindicator=pygame.image.load("redindicator.png")

#_______________________________CHECKING FOR A WINNER________________________
    def Check_Operating_Area(self,CreateBoard,row_num,col_num):
        if row_num <= 3 and col_num <= 3: #region 1
            self.col_down(CreateBoard,row_num,col_num)
            self.row_right(CreateBoard,row_num,col_num)
            self.diag_down_right(CreateBoard,row_num,col_num)
        elif row_num >= 15 and col_num <= 3: #region 7
            self.row_right(CreateBoard,row_num,col_num)
            self.col_up(CreateBoard,row_num,col_num)
            self.diag_up_right(CreateBoard,row_num,col_num)
        elif row_num <= 3 and col_num >= 15: #region 3
            self.row_left(CreateBoard,row_num,col_num)
            self.col_down(CreateBoard,row_num,col_num)
            self.diag_down_left(CreateBoard,row_num,col_num)
        elif row_num >= 15 and col_num >= 15: #region 9
            self.diag_up_left(CreateBoard,row_num,col_num)
            self.row_left(CreateBoard,row_num,col_num)
            self.col_up(CreateBoard,row_num,col_num)
        elif row_num  >= 3 and row_num <= 15 and col_num <= 3: #region 4
            self.row_right(CreateBoard,row_num,col_num)
            self.diag_down_right(CreateBoard,row_num,col_num)
            self.diag_up_right(CreateBoard,row_num,col_num)
            self.col_up(CreateBoard,row_num,col_num)
            self.col_down(CreateBoard,row_num,col_num)
        elif row_num >= 3 and row_num <= 15 and col_num >= 15: #region 6
            self.row_left(CreateBoard,row_num,col_num)
            self.col_up(CreateBoard,row_num,col_num)
            self.col_down(CreateBoard,row_num,col_num)
            self.diag_up_left(CreateBoard,row_num,col_num)
            self.diag_down_left(CreateBoard,row_num,col_num)
        elif col_num >= 3 and col_num <= 15 and row_num <= 3: #region 2
            self.col_down(CreateBoard,row_num,col_num)
            self.row_right(CreateBoard,row_num,col_num)
            self.row_left(CreateBoard,row_num,col_num)
            self.diag_down_right(CreateBoard,row_num,col_num)
            self.diag_down_left(CreateBoard,row_num,col_num)
        elif col_num >= 3 and col_num <= 15 and row_num >= 15: #region 8
            self.col_up(CreateBoard,row_num,col_num)
            self.row_right(CreateBoard,row_num,col_num)
            self.row_left(CreateBoard,row_num,col_num)
            self.diag_up_right(CreateBoard,row_num,col_num)
            self.diag_up_left(CreateBoard,row_num,col_num)
        elif col_num >= 3 and col_num <= 15 and row_num >= 3 and row_num <= 15: #region 5
            self.col_up(CreateBoard,row_num,col_num)
            self.col_down(CreateBoard,row_num,col_num)
            self.row_right(CreateBoard,row_num,col_num)
            self.row_left(CreateBoard,row_num,col_num)
            self.diag_up_right(CreateBoard,row_num,col_num)
            self.diag_up_left(CreateBoard,row_num,col_num)
            self.diag_down_left(CreateBoard,row_num,col_num)
            self.diag_down_right(CreateBoard,row_num,col_num)

    def col_down(self,CreateBoard,row_num,col_num):
        marker = '*'
        marker2 = '%'
        if(self.turn == '0'):
            if(CreateBoard[row_num][col_num] == marker and
               CreateBoard[row_num+1][col_num] == marker and
               CreateBoard[row_num+2][col_num]==marker and
               CreateBoard[row_num+3][col_num]==marker and
               CreateBoard[row_num+4][col_num] == marker):
               print(self.Player1, "You are a WINNER!")
               self.didiwin = True
        elif(self.turn == '1'):
            if(CreateBoard[row_num][col_num] == marker2 and
                 CreateBoard[row_num+1][col_num] == marker2 and
                 CreateBoard[row_num+2][col_num]==marker2 and
                 CreateBoard[row_num+3][col_num]==marker2 and
                 CreateBoard[row_num+4][col_num] == marker2):
                 print(self.Player2, "You are a WINNER!")
                 self.didiwin = True

    def col_up(self,CreateBoard,row_num,col_num):
        marker = '*'
        marker2 = '%'
        if(self.turn == '0'):
            if(CreateBoard[row_num][col_num] == marker and
               CreateBoard[row_num-1][col_num] == marker and
               CreateBoard[row_num-2][col_num]==marker and
               CreateBoard[row_num-3][col_num]==marker and
               CreateBoard[row_num-4][col_num] == marker):
               print(self.Player1, "You are a winner!")
               self.didiwin = True
       elif(self.turn == '1'):
            if(CreateBoard[row_num][col_num] == marker2 and
               CreateBoard[row_num-1][col_num] == marker2 and
               CreateBoard[row_num-2][col_num]==marker2 and
               CreateBoard[row_num-3][col_num]==marker2 and
               CreateBoard[row_num-4][col_num] == marker2):
               print(self.Player2, "You are a winner!")
               self.didiwin = True

    def row_right(self,CreateBoard,row_num,col_num):
        marker = '*'
        marker2 = '%'
        if(self.turn == '0'):
            if(CreateBoard[row_num][col_num] == marker and
               CreateBoard[row_num][col_num+1] == marker and
               CreateBoard[row_num][col_num+2]==marker and
               CreateBoard[row_num][col_num+3]==marker and
               CreateBoard[row_num][col_num+4] == marker):
               print(self.Player1, "You are a winner1!")
               self.didiwin = True
       elif(self.turn == '1'):
            if(CreateBoard[row_num][col_num] == marker2 and
               CreateBoard[row_num][col_num+1] == marker2 and
               CreateBoard[row_num][col_num+2]==marker2 and
               CreateBoard[row_num][col_num+3]==marker2 and
               CreateBoard[row_num][col_num+4] == marker2):
               print(self.Player2, "You are a winner1!")
               self.didiwin = True

    def row_left(self,CreateBoard,row_num,col_num):
        marker = '*'
        marker2 = '%'
        if(self.turn == '0'):
            if(CreateBoard[row_num][col_num] == marker and
               CreateBoard[row_num][col_num-1] == marker and
               CreateBoard[row_num][col_num-2]==marker and
               CreateBoard[row_num][col_num-3]==marker and
               CreateBoard[row_num][col_num-4] == marker):
               print(self.Player1, "You are a winner1!")
               self.didiwin = True
        elif(self.turn == '1'):
            if(CreateBoard[row_num][col_num] == marker2 and
               CreateBoard[row_num][col_num-1] == marker2 and
               CreateBoard[row_num][col_num-2]==marker2 and
               CreateBoard[row_num][col_num-3]==marker2 and
               CreateBoard[row_num][col_num-4] == marker2):
               print(self.Player2, "You are a winner1!")
               self.didiwin = True


    def diag_down_right(self,CreateBoard,row_num,col_num):
        marker = '*'
        marker2 = '%'
        if(self.turn == '0'):
            if(CreateBoard[row_num][col_num] == marker and
               CreateBoard[row_num+1][col_num+1] == marker and
               CreateBoard[row_num+2][col_num+2]==marker and
               CreateBoard[row_num+3][col_num+3]==marker and
               CreateBoard[row_num+4][col_num+4] == marker):
               print(self.Player1, "You are a winner2!")
               self.didiwin = True
       elif(self.turn == '1'):
            if(CreateBoard[row_num][col_num] == marker2 and
                 CreateBoard[row_num+1][col_num+1] == marker2 and
                 CreateBoard[row_num+2][col_num+2]==marker2 and
                 CreateBoard[row_num+3][col_num+3]==marker2 and
                 CreateBoard[row_num+4][col_num+4] == marker2):
                 print(self.Player2, "You are a winner2!")
                 self.didiwin = True

    def diag_up_left(self,CreateBoard,row_num,col_num):
        marker = '*'
        marker2 = '%'
        if(self.turn == '0'):
            if(CreateBoard[row_num][col_num] == marker and
               CreateBoard[row_num-1][col_num-1] == marker and
               CreateBoard[row_num-2][col_num-2]==marker and
               CreateBoard[row_num-3][col_num-3]==marker and
               CreateBoard[row_num-4][col_num-4] == marker):
               print(self.Player1, "You are a winner2!")
               self.didiwin = True
       elif(self.turn == '1'):
            if(CreateBoard[row_num][col_num] == marker2 and
               CreateBoard[row_num-1][col_num-1] == marker2 and
               CreateBoard[row_num-2][col_num-2]==marker2 and
               CreateBoard[row_num-3][col_num-3]==marker2 and
               CreateBoard[row_num-4][col_num-4] == marker2):
               print(self.Player2, "You are a winner2!")
               self.didiwin = True

    def diag_up_right(self,CreateBoard,row_num,col_num):
        marker = '*'
        marker2 = '%'
        if(self.turn == '0'):
            if(CreateBoard[row_num][col_num] == marker and
               CreateBoard[row_num-1][col_num+1] == marker and
               CreateBoard[row_num-2][col_num+2]==marker and
               CreateBoard[row_num-3][col_num+3]==marker and
               CreateBoard[row_num-4][col_num+4] == marker):
               print(self.Player1, "You are a winner2!")
               self.didiwin = True
       elif(self.turn == '1'):
            if(CreateBoard[row_num][col_num] == marker2 and
               CreateBoard[row_num-1][col_num+1] == marker2 and
               CreateBoard[row_num-2][col_num+2]==marker2 and
               CreateBoard[row_num-3][col_num+3]==marker2 and
               CreateBoard[row_num-4][col_num+4] == marker2):
               print(self.Player2, "You are a winner2!")
               self.didiwin = True

    def diag_down_left(self,CreateBoard,row_num,col_num):
        marker = '*'
        marker2 = '%'
        if(self. turn == '0'):
            if(CreateBoard[row_num][col_num] == marker and
               CreateBoard[row_num+1][col_num-1] == marker and
               CreateBoard[row_num+2][col_num-2]==marker and
               CreateBoard[row_num+3][col_num-3]==marker and
               CreateBoard[row_num+4][col_num-4] == marker):
               print(self.Player1, "You are a winner3!")
               self.didiwin = True
       elif(self.turn == '1'):
            if(CreateBoard[row_num][col_num] == marker2 and
               CreateBoard[row_num+1][col_num-1] == marker2 and
               CreateBoard[row_num+2][col_num-2]==marker2 and
               CreateBoard[row_num+3][col_num-3]==marker2 and
               CreateBoard[row_num+4][col_num-4] == marker2):
               print(self.Player2, "You are a winner3!")
               self.didiwin = True

bg=GomokuGame() #__init__ is called right here

while 1:
    bg.update()
