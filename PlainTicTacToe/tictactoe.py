'''

3 X 3 nested arrays for board
1 board of '' if empty, else filled with value

'''
# New Game Board Creation
playing_board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]
# Board User Sees
position_board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print board

# Ask User for X or or

# Generate random number from 1 - 10 for a target then for computer guess 
#    ask user to guess. closest to number goes first(abs(player - target), abs(comp - target))

# Keep a set of 1 -9 for available spaces and pop off spaces as they're occupied, 
# verify that the users choice is in the set before accepting placement

# Computers placement is determined by random number generator of possible values 

# After set of available places is less than 5 begin checking for winners 
#   When winner found add a point to score ask player 

#   If no winner is found and available spaces len > 0 
#       continue 
#   otherwise cats game
