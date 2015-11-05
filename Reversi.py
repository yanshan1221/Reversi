from string import *
from Reversi_AI import Reversi_AI

class Reversi:
    """ 
    Class Reversi creates Reversi objects that contain all necessary methods for running the Reversi game.
    Yet, some of its functions are never used in this reversi game but they are helpful in terms of testing and debugging.

    Attributes:
        board(int[][]): a 2-D array that stores the board configuration
        computer(str): a string that represents the computer
        player(str): a string that represents the user
    """

    def __init__(self):
        self.board = []
        self.computer = '0'
        self.player = 'X'

    def initiateboard(self):
    """
        initiateboard initializes the configuration of the board with four tiles already placed in the middle of the board
    """
        for i in range(8):
            self.board.append([" "]*8)
     
        for i in range(8):
            for j in range(8):
                self.board[i][j] = " "
        self.board[3][3] = 'X'
        self.board[3][4] = '0'
        self.board[4][3] = '0' 
        self.board[4][4] = 'X'

    def onboard(self,x, y):
    """
    onboard checks if a move x,y is on the board

    Args:
        x(int): the x coordinate of the move
        y(int): the y coordinate of the move

    Returns:
         true if the move is on the board and false otherwise
    """     
        return x >= 0 and x <= 7 and y >= 0 and y <=7

    def corner(self):
    """
    corner checks if the four corners of the board are empty

    Returns: 
        true if one of the four corners of the board is empty
    """
        if self.board[0][0] == " " or self.board[0][7] == " " or self.board[7][0] == "" or self.board[7][7] == " ":
            return True
        return False
         
    def getcorner(self):
    """
    get corner that is unoccupied

    Returns:
        the x,y coordinates of any one of the unoccupied corners
    """
        if self.board[0][0] == " ":
            return 0, 0
        elif self.board[0][7] == " ":
            return 0, 7
        elif self.board[7][0] == " ":
            return 7, 0
        elif self.board[7][7] == " ":
            return 7, 7

    def getemptyspot(self):
    """
    getemptyspot gets the first empty spot found on the board

    Returns:
        the x,y coordinates of the first empty spot found on the board
    """
        emptyspotlist = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == " ":
                    emptyspotlist.append([i,j])
        
        bestx = emptyspotlist[0][1]
        besty = emptyspotlist[0][0]
        return bestx, besty

        
    def getBoard(self):
    """
    returns the 2-D array that stores the board configuration
    """
        return self.board

    def updateboard(self,x,y,tile):
    """
      updateboard takes a move and returns board updated with the move

      Args:
        x(int): x coordinate of the move
        y(int): y coordinate of the move
        tile(str): type of the move

      Returns:
        updated board with tile placed on the move position
    """
        self.board[y][x] = tile
        return self.board

        
    def searchbestmoves(self, playerTile, opponentTile):
    """
    search for the best moves using min-max algorithms with alpha-beta pruning implemented in the Reversi_AI.py

    Args:
        playerTile(str): a string that represents player's tile
        opponentTile(str): a string that represents player's opponent's tile
    
    Returns:
        suggestMove((x,y)): best move for player 

    """
        AI = Reversi_AI()
        suggestMove = AI.getBestMove(self.board,3,playerTile,opponentTile)
        return suggestMove


    
    def reverse(self,initx,inity,tile,oppositetile):
    """
    reverse tiles in between two of player's tiles 
    """    
        for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:# for the new tile, search in eight directions for its oppositetile
            x = initx
            y = inity
            x += xdirection
            y += ydirection
        
            while self.onboard(x,y) and self.board[y][x] == oppositetile:
                    x += xdirection
                    y += ydirection
                    
            if self.onboard(x,y) and self.board[y][x] == tile:
                x -= xdirection
                y -= ydirection
                
                while self.onboard(x,y) and self.board[y][x] == oppositetile: # going backwards and reverse all the opposite tiles in between.
                    print x,y
                    self.board[y][x] = tile
                    x -= xdirection
                    y -= ydirection
                   
                     
        return self.board

    
    def getscore(self,usertile,computertile):
    """
    get scores for both the user and computer
    """
        countusertile = 0
        countcomputertile = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == usertile:
                    countusertile = countusertile + 1
                elif self.board[i][j] == computertile:
                    countcomputertile = countcomputertile + 1
        
        return countusertile, countcomputertile
    
     

    def drawboard(self):
    """
    draw the game board in the terminal, used for testing
    """
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
    """
        assign tile to user and computer
    """
        tile = " "
        if usertile == "X":
            tile = "0"
        elif usertile == "0":
            tile = "X"
        return tile



