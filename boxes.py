import pygame
import math
from http.client import HTTPConnection
import http.client
from The_Server import ClientHandler
import json
import os
global board_array
global wait

wait = 0

class GomokuGame(ClientHandler):
    def __init__(self):
        pass
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
            self.otherplayer = '0'
        else:
            self.otherplayer = '1'

    def CreateBoard(self):
        self.CreateBoardArr = []
        for x in range(0,19):
            self.CreateBoardArr.append(['O'] * 19)
        return self.CreateBoardArr

#___________________________PLAYER FUNCTION____________________________________
    def player1(self,row_num,col_num):
        print("Player 1:")
        if(self.board_array[row_num][col_num] != '%' and self.board_array[row_num][col_num] != '*'):
            if(self.otherplayer == '1'):
                self.board_array[row_num][col_num] = '%'
            else:
                self.board_array[row_num][col_num] = '*'
        else:
            print("You cannot go there player 1")

    def player2(self,row_num,col_num):
        print("player2:")
        if(self.board_array[row_num][col_num] != '%' and self.board_array[row_num][col_num] != '*'):
            if(self.otherplayer == '1'):
                self.board_array[row_num][col_num] = '*'
            else:
                self.board_array[row_num][col_num] = '%'
        else:
            print("You cannot go there player 2")

#___________________________THE CLIENT________________________________________
    def Send_get_req(self):
       conn = http.client.HTTPConnection("149.162.139.182",6000)
       #request command to server
       conn.request("GET","he.txt")

       #get response from server
       response = conn.getresponse()
       print("message value from get req: ",response.reason)
       #print server response and data
       print("printing response...")
       print(int(response.status), response.reason)

       if(self.otherplayer == self.turn):
            temp = str(response.read(),"utf-8")
            #temp = temp.split(",")
            print("temp: ",temp)


    #    if(self.turn == '0'):#if you are player 1 go here
    #        #print(self.data_recieved,"\n\n\n\n",self.board_array)
    #        if(self.data_recieved == self.board_array):#if the board updated
    #             #self.data_recieved = response.read()
    #             self.board_array = self.data_recieved
    #             self.otherplayer = response.reason
       #
    #    if(self.turn == '1'):#if you are player 2 go here
    #         #print(self.data_recieved,"\n\n\n\n",self.board_array)
    #         if(self.data_recieved != self.board_array):#if the board updated
    #              #self.data_recieved = response.read()
    #              self.board_array = self.data_recieved
    #              self.otherplayer = response.reason


       conn.close()

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

            if(self.otherplayer == '1' and self.turn == '0'):#if player 1 cannot make a move
                print(self.board_array[int(temp[1])][int(temp[0])])
                if(self.board_array[int(temp[1])][int(temp[0])] == '%' and self.data_recieved[int(temp[0])][int(temp[1])] == 'O'):
                    self.otherplayer = '0'
                    self.data_recieved[int(temp[0])][int(temp[1])] = '1'
                    temp = 0
            elif(self.otherplayer =='1' and self.turn == '1'):#if player 2 cannot make a move
                if(self.board_array[int(temp[1])][int(temp[0])] == '*' and self.data_recieved[int(temp[1])][int(temp[0])] == 'O'):
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
        # if(self.otherplayer == '1'):#only do ths if it is not my turn
        #     wait = wait + 1
        #
        #     if(wait == 30):#waits for about 3 sec
        #         # self.Send_get_req()
        #         wait = 0
        # else:
        #     pass

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

#NEED TO ASK THE PLAYER TO PICK 1 OR 0 SO WE CAN DETERMINE WHO GOES FIRST

        if(self.otherplayer == '0'):#if it is my turn
            #get mouse position
            mouse = pygame.mouse.get_pos()

            #get x and y positions -- will output from(x,y):  (0,0) --> (18,18)
            xpos = int(math.ceil((mouse[0]-32)/30.0))
            ypos = int(math.ceil((mouse[1]-32)/30.0))

            if pygame.mouse.get_pressed()[0]:
                # with open("C:/Users/marquies/Desktop/he.txt","w+") as file:
                #     file.write(str(xpos)+","+str(ypos))
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
                #self.otherplayer = 1#it is the other players turn now
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

bg=GomokuGame() #__init__ is called right here

while 1:
    bg.update()
