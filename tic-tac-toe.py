import random

print("=" * 40)
print("      TIC TAC TOE GAME")
print("=" * 40)
print("You are X")
print("Computer is O")
print()

board = [" " for i in range(9)]


def show_board():

    print()

    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")

    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")

    print(board[6] + " | " + board[7] + " | " + board[8])

    print()


def check_winner(symbol):

    winning_positions = [

        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]

    ]

    for position in winning_positions:

        if board[position[0]] == symbol and \
           board[position[1]] == symbol and \
           board[position[2]] == symbol:

            return True

    return False


def board_full():

    if " " not in board:
        return True

    return False


def player_move():

    while True:

        try:

            move = int(input("Enter position (1-9): "))

            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9.")

            elif board[move - 1] != " ":
                print("That position is already taken.")

            else:
                board[move - 1] = "X"
                break

        except:
            print("Invalid input. Enter a number.")


def computer_move():

    empty_positions = []

    for i in range(9):

        if board[i] == " ":
            empty_positions.append(i)

    if len(empty_positions) > 0:

        move = random.choice(empty_positions)

        board[move] = "O"

        print("Computer played.")


while True:

    show_board()

    player_move()

    if check_winner("X"):

        show_board()

        print("Congratulations! You won the game 🎉")

        break

    if board_full():

        show_board()

        print("Match Draw!")

        break

    computer_move()

    if check_winner("O"):

        show_board()

        print("Computer won the game.")

        break

    if board_full():

        show_board()

        print("Match Draw!")

        break