import pygame
import math
from http.client import HTTPConnection
import http.client
from The_Server import ClientHandler

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
        self.turn = input("[1] or [2]")
        self.owner=[[0 for x in range(6)] for y in range(6)]
        self.me=0
        self.otherplayer=0
        self.didiwin=False
        self.running=False
        self.board_array = self.CreateBoard()

    def CreateBoard(self):
        self.CreateBoardArr = []
        for x in range(0,19):
            self.CreateBoardArr.append(['O'] * 19)
            with open("game state.txt","w") as file:
                file.write(str(self.CreateBoardArr))
        print("board value: ",self.CreateBoardArr[0][8])
        return self.CreateBoardArr

#___________________________PLAYER FUNCTION____________________________________
    def player1(self,row_num,col_num):
        print("Player 1:")
        if(self.board_array[row_num][col_num] != '%' and self.board_array[row_num][col_num] != '*'):
            self.board_array[row_num][col_num] = '*'
            with open("game state.txt","w") as file:
                file.write(str(self.board_array))
            self.Send_post_req()
        else:
            print("You cannot go there")

    def player2(self,row_num,col_num):
        print("player2:")
        if(self.board_array[row_num][col_num] != '%' and self.board_array[row_num][col_num] != '*'):
            self.board_array[row_num][col_num] = '%'
            with open("game state.txt","w") as file:
                file.write(str(self.board_array))
            self.Send_post_req()
        else:
            print("You cannot go there")

#___________________________THE CLIENT________________________________________
    def Send_get_req(self):
       conn = http.client.HTTPConnection("149.162.139.182",6000)
       #request command to server
       conn.request("GET","he.txt")

       #get response from server
       response = conn.getresponse()
       print("this is message",response.msg)
       self.otherplayer = response.msg
       print("this is all of response: ",response)
       #print server response and data
       print("printing response...")
       print(int(response.status), response.reason)
       data_recieved = response.read()
       board_array = data_recieved
       conn.close()

    def Send_post_req(self):
        conn = http.client.HTTPConnection("149.162.139.182",6000)
        #request command to server
        conn.request("POST","he.txt")

        #get response from server
        response = conn.getresponse()
        print("this is message",response.msg)
        self.otherplayer = response.msg
        print("this is all of response: ",response)
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

    def update(self):
        global wait

        #sleep to make the game 60 fps
        self.clock.tick(60)
        if(self.otherplayer == 1):#only do ths if it is not my turn
            wait = wait + 1

            if(wait == 30):#waits for about 3 sec
                self.Send_get_req()
                wait = 0
        else:
            pass

        #clear the screen
        self.screen.fill(0)

        #draw the board
        self.drawBoard()
        self.drawHUD()

        for event in pygame.event.get():
            #quit if the quit button was pressed
            if event.type == pygame.QUIT:
                exit()

#NEED TO ASK THE PLAYER TO PICK 1 OR 0 SO WE CAN DETERMINE WHO GOES FIRST

        if(self.otherplayer == 0):#if it is my turn
            #get mouse position
            mouse = pygame.mouse.get_pos()

            #get x and y positions -- will output from(x,y):  (0,0) --> (18,18)
            xpos = int(math.ceil((mouse[0]-32)/30.0))
            ypos = int(math.ceil((mouse[1]-32)/30.0))

            if pygame.mouse.get_pressed()[0]:
                if(self.turn == '1'):
                    self.screen.blit(self.orangecircle, [(xpos)*30+8, (ypos)*30+14])
                    self.player1(ypos,xpos)
                elif(self.turn == '2'):
                    self.screen.blit(self.bluecircle, [(xpos)*30+8, (ypos)*30+14])
                    self.player2(ypos,xpos)
                else:
                    print("no players found")
                    exit()
                self.otherplayer = 1#it is the other players turn now
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
