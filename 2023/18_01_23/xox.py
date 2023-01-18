xox = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

x_player = input("Enter X player name")
o_player = input("Enter O player name")


def show():
    for i in range(len(xox)):
        if (i % 3 == 0 and i != 0):
            print()
        print(xox[i], end=" ")


def winner(player):
    if (xox[0] == player and xox[1] == player and xox[2] == player):
        return "Winner☻"
    elif (xox[3] == player and xox[4] == player and xox[5] == player):
        return "Winner☻"
    elif (xox[6] == player and xox[7] == player and xox[8] == player):
        return "Winner☻"
    elif (xox[0] == player and xox[3] == player and xox[6] == player):
        return "Winner☻"
    elif (xox[1] == player and xox[4] == player and xox[7] == player):
        return "Winner☻"
    elif (xox[2] == player and xox[5] == player and xox[8] == player):
        return "Winner☻"
    elif (xox[0] == player and xox[4] == player and xox[8] == player):
        return "Winner☻"
    elif (xox[2] == player and xox[4] == player and xox[6] == player):
        return "Winner☻"
    # elif (xox[0] != "-" and xox[1] != "-" and xox[1] != "-" and xox[2] != "-" and xox[3] != "-" and xox[4] != "-" and xox[5] != "-" and xox[6] != "-" and xox[7] != "-" and xox[8] != "-"):
    #     return "Draw"


gameEnd = True

while (gameEnd):
    x = int(input(f"Your Turn {x_player} => "))
    xox[x-1] = "X"
    show()
    if (winner("X") == "Winner☻"):
        break
    o = int(input(f"Your Turn {o_player} => "))
    xox[o-1] = "O"
    show()
    if (winner("O") == "Winner☻"):
        break
