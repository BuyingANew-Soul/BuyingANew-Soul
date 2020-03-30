def print_board(numbers):
    print(20*" " + numbers[6] + "|" + numbers[7] + "|" + numbers[8])
    print(20*" " + numbers[3] + "|" + numbers[4] + "|" + numbers[5])
    print(20*" " + numbers[0] + "|" + numbers[1] + "|" + numbers[2])


def result_check(board, mark):

    if ((board[0] == mark and board[4] == mark and board[8] == mark) or
            (board[0] == mark and board[1] == mark and board[2] == mark) or
            (board[3] == mark and board[4] == mark and board[5] == mark) or
            (board[6] == mark and board[7] == mark and board[8] == mark) or
            (board[2] == mark and board[4] == mark and board[6] == mark) or
            (board[0] == mark and board[3] == mark and board[6] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark)):
        return "{} wins".format(mark)
    else:
        return "continue"


def tie_checker(board, mark, turn_counter):
    if turn_counter == 8:
        position_of_void = board.index('.')
        temp = board  # I am using a temporary list here to check the tie..
        temp[position_of_void] = mark
        draw_check = result_check(temp, mark)
        if draw_check == "continue":
            return "tie"
        else:
            print("..........You fool! {} is going to win now".format(mark))


def game_play():

    while True:
        board = [".", ".", ".", ".", ".", ".", ".", ".", "."]
        print_board(board)
        print("Who plays first will have 'X' as marker. Other will have 'O' ")
        player1 = "X"
        player2 = "O"
        turn = 1
        mark = None
        turn_counter = 0     # this variable is needed to check draw before the last turn..

        # this while loop is for continuous turn change, it'll not break until we have a result
        while True:
            if turn == 1:
                mark = player1
            elif turn == 2:
                mark = player2

            # Calling the tie_checker to check if it's a draw or not....
            tie_check = tie_checker(board, mark, turn_counter)
            if tie_check == "tie":
                print(".................It's a Tie! .................")
                break

            # putting in a while loop for handling the unexpected errors...
            while True:
                try:
                    i = int(input("{}'s turn- ".format(mark)))  # taking value form player
                    position = i - 1  # as list index starts from 0
                    board[position] = mark
                except ValueError:
                    print("Please put a number from your number-pad to specify a position!")
                    continue
                except IndexError:
                    print("you accidentally pressed more keys on the number-pad! Put again- ")
                    continue
                else:
                    break

            print_board(board)

            # calling the result_check function ..
            result = result_check(board, mark)

            # changing turn..
            if turn == 1:
                turn = 2
            else:
                turn = 1
            turn_counter += 1

            # showing result based on the output of result_check function
            if result != "continue":
                print(20 * " " + result)
                break

        # asking user if the want to play more or not..
        play = input("do you want to play again? Type : y or n")
        if play == "n":
            break


game_play()






