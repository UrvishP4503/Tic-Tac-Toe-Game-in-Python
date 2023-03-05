import random


def display_board(board):
    print(f" {board[1]} | {board[2]} | {board[3]}\n"
          f"---+---+---\n"
          f" {board[4]} | {board[5]} | {board[6]}\n"
          f"---+---+---\n"
          f" {board[7]} | {board[8]} | {board[9]}\n")


def player_input():
    user_input = ""

    while not (user_input == "X" or user_input == "O"):
        user_input = input("Player 1 what you want X or O").upper()

    if user_input == "X":
        return "X", "O"
    else:
        return "O", "X"


def place_marker(board, marker, position_):
    if board[position_] == "_":
        board[position_] = marker
    else:
        posi = player_choice(board)
        place_marker(board, marker, posi)


def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark))


def choose_first():
    if random.randint(1, 2) == 1:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position_):
    return board[position_] == '_'


def full_board_check(board):
    if "_" in board:
        return False
    else:
        return True


def player_choice(board):
    position_of_mark = 0
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while position_of_mark not in x and not space_check(board, position_of_mark):
        try:
            position_of_mark = int(input("Enter a number in range of 1-9 : "))
        except ValueError:
            print("Please enter an valid number")
            continue
        else:
            break
    return position_of_mark


def replay():
    ans = input("Wanna play again:").upper()
    anslist = ["Y", "YES", "YA"]
    if ans in anslist:
        return True
    else:
        return False


if __name__ == '__main__':
    print('Welcome to Tic Tac Toe!')

    while True:
        game_on = False
        theBoard = ['_'] * 10
        theBoard[0] = "#"
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first.')

        play_game = input('Are you ready to play? Enter Yes or No.')
        if play_game.lower() == 'y':
            game_on = True
        else:
            break

        while game_on:
            if turn == 'Player 1':

                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player1_marker, position)

                if win_check(theBoard, player1_marker):
                    display_board(theBoard)
                    print(f'Congratulations! You have won the game {turn}')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                    else:
                        turn = 'Player 2'

            else:

                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player2_marker, position)
                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print(f'Congratulations! You have won the game {turn}')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                    else:
                        turn = 'Player 1'

        if not replay():
            break
