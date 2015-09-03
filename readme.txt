Yanshan Guo
CS 111: Introduction to Computer Science 
Professor David Musicant
Final Project

1. Description and Feature:
My program is designed for user to play Reversi with the computer on a 8 * 8 game board.
The user can choose the type of the tile he or she likes and always starts the game first.
Each round, the user places a new tile on an empty spot on the board. After the user inputs his move, the board will be updated. User’s new tile will be placed on the board and the computer’s tiles in between will be reversed.The updated board will be displayed. Then the user will have to wait for the computer to think and decide which move it wants. 

After the computer decides, the updated board with computer’s new tile and reversed user’s tiles will be displayed.Each round, the score of both the user and the computer will appear at the bottom of the board so that the user knows who is at lead. The program repeats above process till the end of the game.

The feature of this program is the design of the AI. Each round, computer will have to decide its move by itself. It first looks at its current tiles on the board. For each of its tiles on the board, it searches for possible positions where if its new tile is placed, user’s tiles can be reversed. Then it counts the number of user’s tiles being reversed and puts its new tile on the spot which gives largest number. If no user’s tiles can be reversed, computer will decide to put its new tile on one of the four corners on the board. If all the corners have already been occupied, the computer will randomly pick up an available spot on the board to put its tile on.


2. How the program is constructed:
The program consists of 12 functions with a main. 

Function:	            Purpose:

drawboard(board):	     draws the game board when a new tile is placed on the board.

assigntile(usertile):	     takes the type of the tile chosen by the user as the parameter      
                            and assign the other type of tile to be computer's.

initiateboard(board):	     clears all the spots on the board and places the initial four        
                            tiles on the board.

onboard(x, y):	            checks if the position a new tile is on the board.

getcorner(board):	     returns any of the four corners that is still empty.

getemptyspot(board):	     gets a list of empty spots on the board and return the first
                           item in the list.

getxy(board,spot):	     takes user's input of the position of the tile and returns the
                            index of it. If the user chooses an occupied position or a  
                            position outside the board, the function returns negative 
                            numbers.

corner(board):	             checks if the four corners on the board have already been 
                            occupied.

updateboard(board,x,y,tile):	takes the index of the position of a new tile and the type
                               of the tile and returns a new board.

searchbestmoves(board, tile, oppositetile):	AI of this program. It helps the computer 
                                             decide which move can maximize its score.

getscore(board,usertile,computertile):  counts the number of user’s tiles and the number 
                                        of computer’s tiles on the board and returns them 
                                        to the main.

reverse(board,initx,inity,tile,oppositetile):	reverses tiles

3. Current Status:
This program achieves all goals set in the previous design project. However, it still can be improved. Designing interactive graphics can certainly makes this program more intriguing.


Things to Do to improve:

1. Create a user Interface
2. Improve AI such that it becomes more difficult to win computer. 