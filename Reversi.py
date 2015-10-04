from string import *
from Reversi_AI import Reversi_AI

class Reversi:

    def __init__(self):

        self.board = []
        self.computer = '0'
        self.player = 'X'

    def initiateboard(self):

        for i in range(8):
            self.board.append([" "]*8)
     
        for i in range(8):
            for j in range(8):
                self.board[i][j] = " "
        self.board[3][3] = 'X'
        self.board[3][4] = '0'
        self.board[4][3] = '0' 
        self.board[4][4] = 'X'


       # The onboard function checks if both the horizontal position and the vertical position of a new tile are on the range of the board.

    def onboard(self,x, y):
       
        return x >= 0 and x <= 7 and y >= 0 and y <=7
           # The corner function checks if the four corners on the board have already been occupied.

    def corner(self):

        if self.board[0][0] == " " or self.board[0][7] == " " or self.board[7][0] == "" or self.board[7][7] == " ":
            return True
          # The getcorner function returns any of the four corners that is still empty.

    def getcorner(self):
        if self.board[0][0] == " ":
            return 0, 0
        elif self.board[0][7] == " ":
            return 0, 7
        elif self.board[7][0] == " ":
            return 7, 0
        elif self.board[7][7] == " ":
            return 7, 7
        #  The getemptyspot function gets a list of empty spots on the board and return the first item in the list.

    def getemptyspot(self):
        emptyspotlist = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == " ":
                    emptyspotlist.append([i,j])
        
        bestx = emptyspotlist[0][1]
        besty = emptyspotlist[0][0]
        return bestx, besty

        
    def getBoard(self):
        return self.board
#  The getxy function takes user's input of the position of his tile and returns the index of it. If the user chooses an occupied position or a position outside the board, the function returns negative numbers.
    def getxy(self,spot):
        position = spot
        x = int(position[0]) - 1
        y = int(position[1]) - 1
        if self.onboard(x,y) and self.board[y][x] == " ":
            return x, y
        else:
            return -2, -2
        #  The updateboard function takes the index of the position of a new tile and the type of the tile and returns a new board.

    def updateboard(self,x,y,tile):
        self.board[y][x] = tile
        return self.board

        #  The searchbestmoves function is the AI of this program. It helps the computer decide which move can maximize its score.

    def searchbestmoves(self, tile, oppositetile):
        AI = Reversi_AI()
        suggestMove = AI.getBestMove(self.board,3,tile,oppositetile)
        return suggestMove


    # The reverse function is designed to reverse tiles. The parameters are the board, the position of a new tile which is just placed on the board, the type of it and the type of the other tile.
    def reverse(self,initx,inity,tile,oppositetile):

        # for the new tile, search in eight directions for its oppositetile.
        
        for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            x = initx
            y = inity
            x += xdirection
            y += ydirection
        
            while self.onboard(x,y) and self.board[y][x] == oppositetile:
                    x += xdirection
                    y += ydirection
                    # keep incrementing both the x and y position of the new tile till it meets the tile of its own type.
            if self.onboard(x,y) and self.board[y][x] == tile:
                x -= xdirection
                y -= ydirection
                # going backwards and reverse all the opposite tiles in between.
                while self.onboard(x,y) and self.board[y][x] == oppositetile:
                    print x,y
                    self.board[y][x] = tile
                    x -= xdirection
                    y -= ydirection
                    # return the new board.
                     
        return self.board

    # The getscore function counts the number of usertiles and the number of computertiles on the board and the reutrn them to the main.
    def getscore(self,usertile,computertile):
        countusertile = 0
        countcomputertile = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == usertile:
                    countusertile = countusertile + 1
                elif self.board[i][j] == computertile:
                    countcomputertile = countcomputertile + 1
        
        return countusertile, countcomputertile
    
       # The drawboard function draws the game board every time a new tile is placed on the board.

    def drawboard(self):
        print "   1   2   3   4   5   6   7   8"
        horline = " .___.___.___.___.___.___.___.___."
        verline = "|   |   |   |   |   |   |   |   | "
        print horline 
        for i in range(8):
            print " %s" %verline  
            print str(i + 1) + verline
            for j in range(8):
                print " |%s"% self.board[i][j],
            print " |"
            print horline

    def assigntile(self,usertile):
        tile = " "
        if usertile == "X":
            tile = "0"
        elif usertile == "0":
            tile = "X"
        return tile



