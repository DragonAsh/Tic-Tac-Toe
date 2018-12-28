import random
import sys

board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
game_state = 1  # game_state=1 means game is still going on


def win_condition():
    if board[0] == board[1] == board[2] == 1 \
            or board[3] == board[4] == board[5] == 1 \
            or board[6] == board[7] == board[8] == 1:
        print("Win!")
        sys.exit()


while 1:
    # player's turn
    person_move = int(input("Your Turn! A number from 1~9: "))
    if board[person_move - 1] == 0:
        board[person_move - 1] = 1
    else:
        print("You cannot place there!")
        continue
    win_condition()

    print(board)

    # computer's turn
    cpu_move = random.randrange(0, 9)
    while board[cpu_move] != 0:
        cpu_move = random.randrange(0, 9)
    board[cpu_move] = 2

    print(board)
