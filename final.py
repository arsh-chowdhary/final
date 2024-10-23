# Tic Tac Toe - Arsh, Nathaly, Isaac



#Board - Group
board = "1 2 3\n4 5 6\n7 8 9"
print(board)

#Player 1 input - Arsh

X = int(input("Player 1's turn\nChoose a slot 1-9:\n"))
if X == 1:
    board = "X 2 3\n4 5 6\n7 8 9"
elif board == 2:
    board = "1 X 3\n4 5 6\n7 8 9"
elif X == 3:
     board = "1 2 X\n4 5 6\n7 8 9"
elif X == 4:
     board = "1 2 3\nX 5 6\n7 8 9"
elif X == 5:
     board = "1 2 3\n4 X 6\n7 8 9"
elif X == 6:
     board = "1 2 3\n4 5 X\n7 8 9"
elif X == 7:
     board = "1 2 3\n4 5 6\nX 8 9"
elif X == 8:
     board = "1 2 3\n4 5 6\n7 X 9"
elif X == 9:
    board = "1 2 3\n4 5 6\n7 8 X"
else:
    print("You cannot input that")
print(board)



#Player 2 input - Nathaly
#O = input("Where would you like to go?")
#if O is X:
#    print("Already taken")

#Keep going - I

#Check who wins
