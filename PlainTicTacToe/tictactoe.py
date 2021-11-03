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
def print_board(board):
    for row in board:
        for cell in row:
            print(f'| {cell} |', end='')
        print()

print_board(position_board)
print_board(playing_board)

#Possible player options
tokens = ['X', 'O']

# Ask User for X or O


def player_choice(user_token = '',tokens = tokens):
    user_token = input('Would you like to be X or O? ')
    if user_token not in tokens:
        print('Please choose a valid response: X or O ')
        return player_choice(user_token)
    else: return user_token

user_token = player_choice()
print(f'You are {user_token}\'s.')

# Generate random number from 1 - 10 for a target then for computer guess 
#    ask user to guess. closest to number goes first(abs(player - target), abs(comp - target))

# Keep a set of 1 -9 for available spaces
positions = {1, 2, 3, 4, 5, 6, 7, 8, 9}
user_position = int(input(f'Choose the location number to place your {user_token} . '))

# pop off spaces as they're occupied, 
def place_token(user_position = user_position):
    if user_position in positions:
        positions.discard(user_position)
        print(f'You placed an {user_token} in {user_position}.')
    else:
        print_board(playing_board)
        print_board(position_board)
        user_position = input('Please choose a valid position.')
        place_token()

place_token(user_position)



# verify that the users choice is in the set before accepting placement

# Computers placement is determined by random number generator of possible values 

# After set of available places is less than 5 begin checking for winners 
#   When winner found add a point to score ask player 

#   If no winner is found and available spaces len > 0 
#       continue 
#   otherwise cats game
