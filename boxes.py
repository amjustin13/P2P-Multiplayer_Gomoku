import pygame

class GomokuGame():
    def __init__(self):
        pass
        #1
        pygame.init()
        pygame.font.init()

        width, height = 520, 680

        #2
        #initialize the screen
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Gomoku")
        #3
        #initialize pygame clock
        self.clock=pygame.time.Clock()

        # define two arrays for placement of the Boxes
        self.boardh = [[False for x in range(19)] for y in range(20)]
        self.boardv = [[False for x in range(20)] for y in range(19)]

        #initialize the graphics
        self.initGraphics()

    def drawBoard(self):
        for x in range(19):
            for y in range(20):
                if not self.boardh[y][x]:
                    self.screen.blit(self.normallineh, [(x)*25+5, (y)*27])
                else:
                    self.screen.blit(self.bar_doneh, [(x)*25+5, (y)*27])
        for x in range(20):
            for y in range(19):
                if not self.boardv[y][x]:
                    self.screen.blit(self.normallinev, [(x)*27, (y)*25+5])
                else:
                    self.screen.blit(self.bar_donev, [(x)*27, (y)*25+5])

    def update(self):
        #sleep to make the game 60 fps
        self.clock.tick(60)

        #clear the screen
        self.screen.fill(0)

        #draw the board
        self.drawBoard()

        for event in pygame.event.get():
            #quit if the quit button was pressed
            if event.type == pygame.QUIT:
                exit()

        #update the screen
        pygame.display.flip()

    def initGraphics(self):
        self.normallinev=pygame.image.load("normalline.png")
        self.normallineh=pygame.transform.rotate(pygame.image.load("normalline.png"), -90)
        self.bar_donev=pygame.image.load("bar_done.png")
        self.bar_doneh=pygame.transform.rotate(pygame.image.load("bar_done.png"), -90)
        self.hoverlinev=pygame.image.load("hoverline.png")
        self.hoverlineh=pygame.transform.rotate(pygame.image.load("hoverline.png"), -90)


bg=GomokuGame() #__init__ is called right here
while 1:
    bg.update()
