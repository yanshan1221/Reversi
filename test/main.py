

       # The initiateboard function clears all the spots on the board and places initial four tiles on the board.

class Reversi:

    def _init_(self):

        self.board = []
        self.computer = '0'
        self.player = 'X'

    def initiateboard(self):

        for i in range(8):
            self.board.append([" "]*8)
        for i in range(8):
            for j in range(8):
                self.board[i][j] = " "
        self.board[3][3] = self.player 
        self.board[3][4] = self.computer
        self.board[4][3] = self.computer 
        self.board[4][4] = self.player 


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

        #  The getxy function takes user's input of the position of his tile and returns the index of it. If the user chooses an occupied position or a position outside the board, the function returns negative numbers.

    def getxy(self,spot):
        position = spot
        x = int(position[0]) - 1
        y = int(position[1]) - 1
        if onboard(x,y) and self.board[y][x] == " ":
            return x, y
        else:
            return -2, -2
        #  The updateboard function takes the index of the position of a new tile and the type of the tile and returns a new board.

    def updateboard(self,x,y,tile):
        self.board[y][x] = tile
        return self.board

        #  The searchbestmoves function is the AI of this program. It helps the computer decide which move can maximize its score.

    def searchbestmoves(self, tile, oppositetile):

        # First, get a list of positions of computer's tiles on the board.
        tilelist = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == tile:
                   
                   tilelist.append([j,i])
                   #  Set the largest number of usertiles that can be flipped to zero.
                   #  Set the best move's horizontal position to be -1 and its vertical position to be -1.
        largenumflipped = 0
        bestx = -1
        besy = -1

        # for each conputer's tile on the board, search in eight directions for the possible next move.
        for i in range(len(tilelist)):
            initx = tilelist[i][0]
            inity = tilelist[i][1]
            
            for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
                x = initx
                y = inity
                x += xdirection
                y += ydirection
                # Moves that can cause user's tiles to be reversed are better than those that can't help increase the score of the computer.Hence only continuing the while
                # loop if there is user's tile around.
                while onboard(x,y) and self.board[y][x] == oppositetile :
            
                    x += xdirection
                    y += ydirection
                    
                    #  When the while loop above stops, we get the x, y of the possible moves. If its position is on the board and also unoccupied, then count the number of user's tiles that can be flipped.   
                if onboard(x,y) and self.board[y][x] == " ":
                
                    if abs(x -  tilelist[i][0]) > 1 or abs(y - tilelist[i][1]) > 1:
                    
                        differencex = abs(x -  tilelist[i][0])
                        differencey = abs(y - tilelist[i][1])
                        if differencex == differencey:
                            flippednumber = differencex - 1
                        else:
                            flippednumber = abs(differencex - differencey) - 1
                            # Get the position of the move which can cause the largest number of user's tiles to be reversed.
                            if flippednumber > largenumflipped:
                                largenumflipped = flippednumber
                                bestx = x
                                besty = y
        # if the computer does not excute the above loop, which means that there is no user's tile around the current computer tiles, the computer will put its tile on any of the four corners.
        
        if bestx == -1 and corner():
            besty, bestx = getcorner()
            print bestx, besty
            # if all the corners on the board are already occupied by user's tiles, the computer will put its new tile on any of the empty spot on the board.
        elif bestx == -1 and not corner():
            bestx, besty = getemptyspot()
            # Returns the computer's move.   
        return  bestx, besty

    # The reverse function is designed to reverse tiles. The parameters are the board, the position of a new tile which is just placed on the board, the type of it and the type of the other tile.
    def reverse(self,initx,inity,tile,oppositetile):

        # for the new tile, search in eight directions for its oppositetile.
        
        for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            x = initx
            y = inity
            x += xdirection
            y += ydirection
        
            while onboard(x,y) and self.board[y][x] == oppositetile:
                    x += xdirection
                    y += ydirection
                    # keep incrementing both the x and y position of the new tile till it meets the tile of its own type.
            if onboard(x,y) and self.board[y][x] == tile:
                x -= xdirection
                y -= ydirection
                # going backwards and reverse all the opposite tiles in between.
                while onboard(x,y) and self.board[y][x] == oppositetile:
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
        print "Your score is" + str(countusertile), "Computer's score is" + str(countcomputertile)
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

    def assigntile(usertile):
        tile = " "
        if usertile == "X":
            tile = "0"
        elif usertile == "0":
            tile = "X"
        return tile



from string import *
import time 


def main():
    # create the 8 * 8 grid.(variable:board)
    
    

        # aske the user to input the tile he chooses to play and also assign computer the other tile.
    usertile = raw_input("Welcome to the Rerversi Game! Do you want to play X(black tile) or 0(white tile)?Please enter X or 0.")
    usertile = usertile.upper()
    computertile = assigntile(usertile)
       # print the initial board with four tiles in the center.
    board = initiateboard(board)
    drawboard(board)
       # Set the sum of the number of computer's tiles and the number of user's tiles on the board to be zero.
    sumscore = 0

    # While there is still empty spot on the board, the loop continues. When every spot on the board has been occupied, the loop stops.
    while sumscore < 64:
        print
        # ask the user to input the position on the board where he wants to place his tile.
        userspot = raw_input("Where do you want to place your tile? Please enter in format like this: 34(horizontal position: 3, vertical position: 4)[Enter a negative number if you want to quit the game.]")
        # If the user chooses to quit the game, print byebye and break the while loop by setting the sumscore to be a number larger than 64.
        if int(userspot) < 0:
            print "byebye!"
            sumscore = 67
            # If the user chooses to continue the game, get the x, y index. If the user chooses a spot that has been occupied or outside the board, ask the user to input again.
        elif int(userspot) > 0:

            userx, usery =  getxy(board,userspot)

            while userx == -2 or usery == -2:
                print "Sorry. Invalid Move. Please try again."
                userspot = raw_input("Where do you want to place your tile? Please enter in format like this: 34(horizontal position: 3, vertical position: 4)[Enter a negative number if you want to quit the game.]")
                
                userx, usery =  getxy(board,userspot)

                # update the board according to user's input.

            update = updateboard(board,userx,usery,usertile)

                # get a newboard on which new tile has been placed and tiles of the other type have been reversed.

            newboard = reverse(update,userx,usery,usertile,computertile)
            print 
            print "Here is your move!" + str(userx + 1) + str(usery + 1)
            print
            # draw the board so that user can see the new board.

            drawboard(newboard)

            # get the x, y index of the computer's move.

            compx, compy = searchbestmoves(newboard, computertile, usertile)

            # update the board according to computer's move.

            update = updateboard(board,compx,compy,computertile)

            # get a new board on which computer's new tile has been placed and user's tiles are reversed.

            newboard = reverse(update,compx,compy,computertile,usertile)

            print
            print
            print "wait for computer to decide its move!"
            # make sure that there is a pause between showing the two board.
            time.sleep(4)
            print 
            print "This is computer's move!" + str(compx + 1) + str(compy + 1)
            print 

            drawboard(newboard)

            # Each round, count the number of computer's tiles on the board and the number of user's tiles on the board.
            userscore, computerscore = getscore(newboard, usertile, computertile)
            # Each round, count the sum of the number of computer's tiles and the number of user's tiles on the board.
            sumscore = userscore + computerscore
            # update the board.
            board = newboard

            # At the end of the game, if there are more user's tiles on the board, user wins the game. If there are more computer's tiles on the board, computer wins the game.
            # If there are equal numner of computer's tiles and user's tiles on the board, print no one wins the game.
    
    if userscore > computerscore:
        print"You win the game!ByeBye"
    elif userscore < computerscore:
        print"Computer win the game!ByeBye"
    else:
        print"No one wins. ByeBye"
    
    
main()
       

    
