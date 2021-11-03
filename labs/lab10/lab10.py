"""
Name: Benjamin Roth
lab 10.py
"""


def build():
    return list(range(1, 10))


def display(board):
    for i in range(3):
        n = i * 3
        print(board[n], "|", board[n + 1], "|", board[n + 2])
        print(10 * "-")


def place(board, pos, piece):
    if piece == "x" or piece == "o":
        board[pos - 1] = piece
    else:
        print("not valid piece")


def legal(board, pos):
    if 1 <= pos <= 9 and board[pos - 1] == pos:
        return True
    else:
        return False


def is_won(board, piece):
    for i in range(3):
        n = i * 3
        if board[n] != piece:
            continue
        if board[n + 1] != piece:
            continue
        if board[n + 2] != piece:
            continue
        return True

    for i in range(3):
        if board[i] != piece:
            continue
        if board[i + 3] != piece:
            continue
        if board[i + 6] != piece:
            continue
        return True

    if board[0] == piece:
        if board[4] == piece:
            if board[8] == piece:
                return True

    if board[3] == piece:
        if board[4] == piece:
            if board[6] == piece:
                return True


def is_over(board):
    if is_won(board,"x"):
        return True
    elif is_won(board, "o"):
        return True
    else:
        for i in range(9):
            if board[i] == i + 1:
                return False
        return True


def play():
    board = build()

    while True:
        display(board)
        pos_x = eval(input("X - Enter a position 1 through 9: "))
        if legal(board, pos_x):
            place(board, pos_x, "x")
        if is_over(board):
            if is_won(board, "x"):
                display(board)
                print("The winner is X")
                break
            else:
                display(board)
                print("It is a tie")
                break

        display(board)
        pos_o = eval(input("O - Enter a position 1 through 9: "))
        if legal(board, pos_o):
            place(board, pos_o, "o")
        if is_over(board):
            if is_won(board,"o"):
                display(board)
                print("The winner is O")
                break


def main():
    play()
    pass


if __name__ == '__main__':
    main()
