# This program simulates Tic-Tac-Toe game
def game_board(b):  # Define function for board
    for i in range(len(b)):
        print('   '.join(b[i]))


def player_move(b):  # Define function for player move
    valid_column = [0, 1, 2]
    while True:
        row, col = eval(input("Enter the row (0,1,2) and column (0,1,2): "))
        if (row not in valid_column) or (col not in valid_column):
            print("Invalid Move. Please enter again")
        elif b[row][col] != '-':
            print("Already Filled. Please enter again")
        else:
            return row, col


def check_winner(b):  # Define function to check for winner
    # Check for Row
    for row in b:
        if all(cell == 'X' for cell in row):
            return 'X'
        elif all(cell == 'O' for cell in row):
            return 'O'

    # Check for Column
    for col in range(3):
        if all(b[row][col] == 'X' for row in range(3)):
            return 'X'
        elif all(b[row][col] == 'O' for row in range(3)):
            return 'O'

    # Check for Diagonal
    if all(b[i][i] == 'X' for i in range(3)) or all(b[i][2 - i] == 'X' for i in range(3)):
        return 'X'
    elif all(b[i][i] == 'O' for i in range(3)) or all(b[i][2 - i] == 'O' for i in range(3)):
        return 'O'

    return None  # No winner


def check_draw(b):  # Define function for draw game
    return all(cell != '-' for row in b for cell in row)


def update_board(row, col, player, b):  # Define function to update the board
    b[row][col] = player


def main():  # Define main function
    b = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    print("Game: Tic-Tac-Toe")
    max_moves = 9  # Maximum move for a 3x3 board
    player_turn = True
    for move in range(max_moves):
        # Call player's turn
        player = 'X' if player_turn else 'O'
        print(f"Player {player}'s turn")
        # Call the input and display function
        row, col = player_move(b)
        update_board(row, col, player, b)
        game_board(b)
        # Call the validate function
        if check_winner(b) == player:
            print(f"Game Over. {player} won")
            break
        elif check_draw(b):
            print("Game Over. It is a Draw")
            break
        # Switch the player's turn
        player_turn = not player_turn


main()  # Define main function
