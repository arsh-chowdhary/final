# Tic Tac Toe - Arsh, Nathaly, Isaac

#Board - Group
board1 = ["1", "2", "3"]
board2 = ["4", "5", "6"]
board3 = ["7", "8", "9"]
print("", board1,"\n", board2,"\n", board3)

#Player 1 input - Arsh
def playing(player):
     return(int(input(f"{player} turn\nChoose a slot 1-9 that has not been taken: ")))

X = playing("Player 1's")
if X == 1:
     board1[0]="X"
elif X == 2:
     board1[1]="X"
elif X == 3:
     board1[2]="X"
elif X == 4:
     board2[3]="X"
elif X == 5:
     board2[4]="X"
elif X == 6:
     board2[5]="X"
elif X == 7:
     board3[6]="X" 
elif X == 8:
     board3[7]="X"
elif X == 9:
     board3[8]="X"
else:
    print("You cannot input that")
print("", board1,"\n", board2,"\n", board3)


#Player 2 input - Nathaly
def slot(number):
     return(int(input(f"{number} has already been taken!")))

O = playing("Player 2's")
if O==X:
     print(slot(X))
     O = input("Player 2's turn\nChoose a slot 1-9 that has not been taken: ")
elif O == 1:
     board1[0]="O"
elif O == 2:
     board1[1]="O"
elif O == 3:
     board1[2]="O"
elif O == 4:
     board2[3]="O"
elif O == 5:
     board2[4]="O"
elif O == 6:
     board2[5]="O"
elif O == 7:
     board3[6]="O" 
elif O == 8:
     board3[7]="O"
elif O == 9:
     board3[8]="O"
else:
    print("You cannot input that")
print("", board1,"\n", board2,"\n", board3)

#Keep going - Isaac





#Check who wins - 
