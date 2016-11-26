import pygame
import math
from http.client import HTTPConnection
import http.client
from joi import CreateBoard
from http.server import BaseHTTPRequestHandler,HTTPServer
import os
global board_array=CreateBoard()

#_____________________________THE SERVER HANDLER_______________________________
class ClientHandler(BaseHTTPRequestHandler):
    user_name = input("Please enter your username: ")#your computer name
    #handle a GET request
    def do_GET(self):
        #file location
        rootdir = 'C:/Users/'+self.user_name+'/Desktop/'
        try:
            if self.path.endswith('.txt'):
                f = open(rootdir + self.path)#opens the requested file

                #packing the header files together
                self.send_response(200)#ok
                #specify the type you are handling
                self.send_header("Content-type", "text/txt")
                self.end_headers()

                #send the file contents to client
                self.wfile.write(bytes(f.readline(),"utf-8"))
                f.close()
                return
        except IOError:
            self.send_error(404,'file not found')

    #Handle a POST request
    def do_POST(self):
        rootdir = 'C:/Users/'+self.user_name+'/Desktop/
        try:
            if self.path.endswith('.txt'):
                with open(rootdir + self.path,"w") as f:
                    f.writeline()
                f.close()
                #packing the header files together
                self.send_response(200)#ok
                #specify the type you are handling
                self.send_header("Content-type", "text/txt")
                self.end_headers()
                return
        except IOError:
            self.send_error(404,'file not found')

#___________________________THE SERVER____________________________________
#this is how you create and run the server
def run(server_class = HTTPServer, handler_class = ClientHandler):
    print("http server is starting...")
    server_address = ('192.168.0.4',6000)#connect to this location
    httpd = server_class(server_address,handler_class)
    print("http is running...")
    httpd.serve_forever()

class GomokuGame():
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
        self.turn = True
        self.owner=[[0 for x in range(6)] for y in range(6)]
        self.me=0
        self.otherplayer=0
        self.didiwin=False
        self.running=False

    def Send_get_req():
       #request command to server
       conn.request('GET','game state.txt')

       #get response from server
       response = conn.getresponse()

       #print server response and data
       print("printing response...")
       print(int(response.status), response.reason)
       data_recieved = response.read()
       board_array = data_recieved
       conn.close()

    def Send_post_req():
        #create a connection
        conn = http.client.HTTPConnection("localhost",80)#192.168.0.24:6000

        #request command to server
        conn.request('POST','game state.txt')
        #get response from server
        response = conn.getresponse()

        #print server response and data
        print("printing response...")
        print(int(response.status), response.reason)
        data_recieved = response.read()
        print(data_recieved)
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
        #sleep to make the game 60 fps
        self.clock.tick(60)

        #clear the screen
        self.screen.fill(0)

        #draw the board
        self.drawBoard()
        self.drawHUD()

        for event in pygame.event.get():
            #quit if the quit button was pressed
            if event.type == pygame.QUIT:
                exit()

        #get mouse position
        mouse = pygame.mouse.get_pos()

        #get x and y positions -- will output from(x,y):  (0,0) --> (18,18)
        xpos = int(math.ceil((mouse[0]-32)/30.0))
        ypos = int(math.ceil((mouse[1]-32)/30.0))

        if pygame.mouse.get_pressed()[0]:
            self.screen.blit(self.orangecircle, [(xpos)*30, (ypos)*30+5])
            Send_post_resp()

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
    http.client.HTTPConnection("localhost",80)


bg=GomokuGame() #__init__ is called right here
if(__name__ == '__main__'):
   run()

while 1:
    bg.update()
