# Reversi
This program is a simple Reversi game whose AI uses the Min_Max_Search algorithm implemented with Alpha_Beta_Pruning.
It allows user to play Reversi with the computer. For details about the game, consult the following
wikipedia page https://en.wikipedia.org/wiki/Reversi. For details about the AI, consult the papers in the papers folder in the 
repository. 

![](https://github.com/yanshan1221/Reversi/blob/master/reversi_game.gif)

## Play the game

To run this Reversi game, simply download the repository and run the main file Reversi_GUI.py. This program is built with python 2.7
and has been successfully tested on Mac 10.8.5, 32 bits. Once you run the Reversi_GUI.py file on your computer, the game starts with 
four tiles on the board already. As user, you can click on positions on the board to place tiles.

## Design of the Game

### - AI
The Aritificial Intelligence algorithm for this game uses the classic Min-Max-Search algoirthm implemented by Alpha-Beta Pruning.
The maximal depth of search for Min_Max_Search is set to be 4 in this program. Even though setting the depth to be a larger number
will enhance the performance of this AI, due to the speed of this program, 4 is the optimal number. 
In order to let the computer choose a best move, the program will compute the value of every valid move of computer by evaluating 
the value of the resulting configuration of the game board. The value of a specific configuration of the game board is evaluated as the sum of the number of player's tiles on board minus 
the sum of his opponent's total number of tiles on board. For Reversi, some positions on board have special roles in the game and 
thus are given weight different from other positions. In this program, X-positions, C-positions, and corner positions are considered
to be special positions and are given weights as the following: -5, -3, 3. For details about special positions in Reversi and how
they affect the game, please consult http://www.samsoft.org.uk/reversi/strategy.html.

## - Interface

This program comes with a simple interface. On the right hand side of the screen shows current scores of both computer and the player and
the placement of new tiles on the board. 
Notice that this program follows rules of Reversi strictly, meaning that both player and computer can only place tiles on places
on the board that can lead to a flip of the opponent's tile. When user clicks on invalid positions on the board, the terminal will show
an "invalid move" warning to user. 

## Further Improvement

This program still represents the game board as a two-dimensional array, which slows down the computation. A further improvement
of the effciency of the AI computation is to use bit strings to represent the game board and implement the transiposition table,
which is dicussed in the papers. These improvements can significantly increase the efficiency of the program. 
