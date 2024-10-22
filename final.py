# Tic Tac Toe - Arsh, Nathaly, Isaac



#Board - Group
board = print("1 2 3\n4 5 6\n7 8 9")

#Player 1 input - Arsh
X = input("Where would you like to go?")
if X == 1:
    board = print("X 2 3\n4 5 6\n7 8 9")
elif X == 2:
    board = print("1 X 3\n4 5 6\n7 8 9")
elif X == 3:
    board = print("1 2 X\n4 5 6\n7 8 9")
elif X == 4:
    board = print("1 2 3\nX 5 6\n7 8 9")
elif X == 5:
    board = print("1 2 3\n4 X 6\n7 8 9")
elif X == 6:
    board = print("1 2 3\n4 5 X\n7 8 9")
elif X == 7:
    board = print("1 2 3\n4 5 6\nX 8 9")
elif X == 8:
     board = print("1 2 3\n4 5 6\n7 X 9")
elif X == 9:
    board = print("1 2 3\n4 5 6\n7 8 X")



#Player 2 input - Nathaly
#O = input("Where would you like to go?")
#if O is X:
#    print("Already taken")

#Keep going - I

#Check who wins
