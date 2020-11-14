File(s) included: tictactoe.py

This program allows the user to play tic-tac-toe with the computer at three different levels: 
1.Easy
2.Intermediate 
3.Difficult

The player plays 'X' and the computer plays 'O'

1. At the easy level, it always chooses the center if that is a legal move, else it generates
random numbers between 1 and 9 and returns the first legal move generated

2. At the intermediate level, first, it checks if there is an imminent possibility of the opponent
winning. If the possibility exists, if places 'O' in a spot that will prevent the player from 
winning.If there is no imminent possibility of the player winning, it chooses one of the outer corners.
If no corners are available, it chooses any empty spot available

2. At the difficult level, a minimax algorithm is utilized to return the best possible action against an
optimal human player. To simplify, it does so by creating all the possible states for a certain state passed.
The maximum payoff possible is a tie. When it's the computer i.e the max player's turn to play, all the 
possible actions are passed to the minValue function and the action giving the maximum payoff is returned. 
Similarly, when it is the min player's turn to play, minValue function will return the action with the 
lowest payoff. This is because minimax algorithm anticipates the human to be an optimum player, therefore 
the min player would be minimizing the max player's playoff. The payoff is calculated using an eval function
which returns the utility value of any given state. 

                                    --------ENJOY THE GAME!--------
