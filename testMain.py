from string import *
import time 
from Reversi import Reversi

def main():
    # create the 8 * 8 grid.(variable:board)
    reversi = Reversi()
        # aske the user to input the tile he chooses to play and also assign computer the other tile.
    usertile = raw_input("Welcome to the Rerversi Game! Do you want to play X(black tile) or 0(white tile)?Please enter X or 0.")
    
    usertile = usertile.upper()
    
    computertile = reversi.assigntile(usertile)
       # print the initial board with four tiles in the center.
    reversi.initiateboard()
  
    reversi.drawboard()
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

            userx, usery =  reversi.getxy(userspot)

            while userx == -2 or usery == -2:
                print "Sorry. Invalid Move. Please try again."
                userspot = raw_input("Where do you want to place your tile? Please enter in format like this: 34(horizontal position: 3, vertical position: 4)[Enter a negative number if you want to quit the game.]")
                
                userx, usery =  reversi.getxy(userspot)

                # update the board according to user's input.

            update = reversi.updateboard(userx,usery,usertile)

                # get a newboard on which new tile has been placed and tiles of the other type have been reversed.

            newboard = reversi.reverse(userx,usery,usertile,computertile)
            print 
            print "Here is your move!" + str(userx + 1) + str(usery + 1)
            print
            # draw the board so that user can see the new board.

            reversi.drawboard()

            # get the x, y index of the computer's move.

            compx, compy = reversi.searchbestmoves(computertile, usertile)

            # update the board according to computer's move.

            update = reversi.updateboard(compx,compy,computertile)

            # get a new board on which computer's new tile has been placed and user's tiles are reversed.

            newboard = reversi.reverse(compx,compy,computertile,usertile)

            print
            print
            print "wait for computer to decide its move!"
            # make sure that there is a pause between showing the two board.
            time.sleep(4)
            print 
            print "This is computer's move!" + str(compx + 1) + str(compy + 1)
            print 

            reversi.drawboard()

            # Each round, count the number of computer's tiles on the board and the number of user's tiles on the board.
            userscore, computerscore = reversi.getscore(usertile, computertile)
            # Each round, count the sum of the number of computer's tiles and the number of user's tiles on the board.
            sumscore = userscore + computerscore
            # update the board.
            

            # At the end of the game, if there are more user's tiles on the board, user wins the game. If there are more computer's tiles on the board, computer wins the game.
            # If there are equal numner of computer's tiles and user's tiles on the board, print no one wins the game.
    
    if userscore > computerscore:
        print"You win the game!ByeBye"
    elif userscore < computerscore:
        print"Computer win the game!ByeBye"
    else:
        print"No one wins. ByeBye"
    
    
main()
       

    
