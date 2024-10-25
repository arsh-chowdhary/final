# Tic Tac Toe - Arsh, Nathaly, Isaac, Juan
#Loop is the whole code
#Board - Group
board1 = ["1", "2", "3"]
board2 = ["4", "5", "6"]
board3 = ["7", "8", "9"]
print("", board1,"\n", board2,"\n", board3)

#Player 1 input - Arsh
#Function 1
def playing(player):
     return(int(input(f"{player} turn\nChoose a slot 1-9 that has not been taken: ")))

def slot(number):
     return(int(input(f"{number} has already been taken!")))

#Loop
while True:
     X = playing("X's")
     if X == 1:     #Conditionals
          board1[0]="X"
     elif X == 2:
          board1[1]="X"
     elif X == 3:
          board1[2]="X"
     elif X == 4:
          board2[0]="X"
     elif X == 5:
          board2[1]="X"
     elif X == 6:
          board2[2]="X"
     elif X == 7:
          board3[0]="X" 
     elif X == 8:
          board3[1]="X"
     elif X == 9:
          board3[2]="X"
     else:
          print("You cannot input that")
     print("", board1,"\n", board2,"\n", board3)

#Player 2 input - Nathaly
#Function 2
     O = playing("O's")
     if O==X:
          print(slot(X))
     elif O == 1:
          board1[0]="O"
     elif O == 2:
          board1[1]="O"
     elif O == 3:
          board1[2]="O"
     elif O == 4:
          board2[0]="O"
     elif O == 5:
          board2[1]="O"
     elif O == 6:
          board2[2]="O"
     elif O == 7:
          board3[0]="O" 
     elif O == 8:
          board3[1]="O"
     elif O == 9:
          board3[2]="O"
     else:
          print("You cannot input that")
     print("", board1,"\n", board2,"\n", board3)

#Keep going - Isaac
     X = playing("X's")
     if X==O:
          print(slot(X))
     elif X == 1:
          board1[0]="X"
     elif X == 2:
          board1[1]="X"
     elif X == 3:
          board1[2]="X"
     elif X == 4:
          board2[0]="X"
     elif X == 5:
          board2[1]="X"
     elif X == 6:
          board2[2]="X"
     elif X == 7:
          board3[0]="X" 
     elif X == 8:
          board3[1]="X"
     elif X == 9:
          board3[2]="X"
     else:
          print("You cannot input that")
     print("", board1,"\n", board2,"\n", board3)

     O = playing("O's")
     if O==X:
          print(slot(X))
     elif O == 1:
          board1[0]="O"
     elif O == 2:
          board1[1]="O"
     elif O == 3:
          board1[2]="O"
     elif O == 4:
          board2[0]="O"
     elif O == 5:
          board2[1]="O"
     elif O == 6:
          board2[2]="O"
     elif O == 7:
          board3[0]="O" 
     elif O == 8:
          board3[1]="O"
     elif O == 9:
          board3[2]="O"
     else:
          print("You cannot input that")
     print("", board1,"\n", board2,"\n", board3)

     X = playing("X's")
     if X==O:
          print(slot(X))
     elif X == 1:
          board1[0]="X"
     elif X == 2:
          board1[1]="X"
     elif X == 3:
          board1[2]="X"
     elif X == 4:
          board2[0]="X"
     elif X == 5:
          board2[1]="X"
     elif X == 6:
          board2[2]="X"
     elif X == 7:
          board3[0]="X" 
     elif X == 8:
          board3[1]="X"
     elif X == 9:
          board3[2]="X"
     else:
          print("You cannot input that")
     print("", board1,"\n", board2,"\n", board3)

     #Check who wins - Juan
     if board1 == ["X", "X", "X"]:
          print("X Wins!")
          break
     elif board2 == ["X", "X", "X"]:
          print("X Wins!")
          break
     elif board3 == ["X", "X", "X"]:
          print("X Wins!")
          break
     elif board1[0] == board2[1] == board3[2] == "X":
          print("X Wins!")
          break
     elif board1[2] == board2[1] == board3[0] == "X":
          print("X Wins!")
          break
     elif board1[0] == board2[0] == board3[0] == "X":
          print("X Wins!")
          break
     elif board1[1] == board2[1] == board3[1] == "X":
          print("X Wins!")
          break
     elif board1[2] == board2[2] == board3[2] == "X":
          print("X Wins!")
          break

     O = playing("O's")
     if O==X:
          print(slot(X))
     elif O == 1:
          board1[0]="O"
     elif O == 2:
          board1[1]="O"
     elif O == 3:
          board1[2]="O"
     elif O == 4:
          board2[0]="O"
     elif O == 5:
          board2[1]="O"
     elif O == 6:
          board2[2]="O"
     elif O == 7:
          board3[0]="O" 
     elif O == 8:
          board3[1]="O"
     elif O == 9:
          board3[2]="O"
     else:
          print("You cannot input that")
     print("", board1,"\n", board2,"\n", board3)

     if board1 == ["O", "O", "O"]:
          print("O Wins!")
          break
     elif board2 == ["O", "O", "O"]:
          print("O Wins!")
          break
     elif board3 == ["O", "O", "O"]:
          print("O Wins!")
          break
     elif board1[0] == board2[1] == board3[2] == "O":
          print("O Wins!")
          break
     elif board1[2] == board2[1] == board3[0] == "O":
          print("O Wins!")
          break
     elif board1[0] == board2[0] == board3[0] == "O":
          print("O Wins!")
          break
     elif board1[1] == board2[1] == board3[1] == "O":
          print("O Wins!")
          break
     elif board1[2] == board2[2] == board3[2] == "O":
          print("O Wins!")
          break

     X = playing("X's")
     if X==O:
          print(slot(X))
     elif X == 1:
          board1[0]="X"
     elif X == 2:
          board1[1]="X"
     elif X == 3:
          board1[2]="X"
     elif X == 4:
          board2[0]="X"
     elif X == 5:
          board2[1]="X"
     elif X == 6:
          board2[2]="X"
     elif X == 7:
          board3[0]="X" 
     elif X == 8:
          board3[1]="X"
     elif X == 9:
          board3[2]="X"
     else:
          print("You cannot input that")
     print("", board1,"\n", board2,"\n", board3)

     if board1 == ["X", "X", "X"]:
          print("X Wins!")
          break
     elif board2 == ["X", "X", "X"]:
          print("X Wins!")
          break
     elif board3 == ["X", "X", "X"]:
          print("X Wins!")
          break
     elif board1[0] == board2[1] == board3[2] == "X":
          print("X Wins!")
          break
     elif board1[2] == board2[1] == board3[0] == "X":
          print("X Wins!")
          break
     elif board1[0] == board2[0] == board3[0] == "X":
          print("X Wins!")
          break
     elif board1[1] == board2[1] == board3[1] == "X":
          print("X Wins!")
          break
     elif board1[2] == board2[2] == board3[2] == "X":
          print("X Wins!")
          break

     O = playing("O's")
     if O==X:
          print(slot(X))
     elif O == 1:
          board1[0]="O"
     elif O == 2:
          board1[1]="O"
     elif O == 3:
          board1[2]="O"
     elif O == 4:
          board2[0]="O"
     elif O == 5:
          board2[1]="O"
     elif O == 6:
          board2[2]="O"
     elif O == 7:
          board3[0]="O" 
     elif O == 8:
          board3[1]="O"
     elif O == 9:
          board3[2]="O"
     else:
          print("You cannot input that")
     print("", board1,"\n", board2,"\n", board3)

     if board1 == ["O", "O", "O"]:
          print("O Wins!")
          break
     elif board2 == ["O", "O", "O"]:
          print("O Wins!")
          break
     elif board3 == ["O", "O", "O"]:
          print("O Wins!")
          break
     elif board1[0] == board2[1] == board3[2] == "O":
          print("O Wins!")
          break
     elif board1[2] == board2[1] == board3[0] == "O":
          print("O Wins!")
          break
     elif board1[0] == board2[0] == board3[0] == "O":
          print("O Wins!")
          break
     elif board1[1] == board2[1] == board3[1] == "O":
          print("O Wins!")
          break
     elif board1[2] == board2[2] == board3[2] == "O":
          print("O Wins!")
          break

     X = playing("X's")
     if X==O:
          print(slot(X))
     elif X == 1:
          board1[0]="X"
     elif X == 2:
          board1[1]="X"
     elif X == 3:
          board1[2]="X"
     elif X == 4:
          board2[0]="X"
     elif X == 5:
          board2[1]="X"
     elif X == 6:
          board2[2]="X"
     elif X == 7:
          board3[0]="X" 
     elif X == 8:
          board3[1]="X"
     elif X == 9:
          board3[2]="X"
     else:
          print("You cannot input that")
     print("", board1,"\n", board2,"\n", board3)

     if board1 == ["X", "X", "X"]:
          print("X Wins!")
          break
     elif board2 == ["X", "X", "X"]:
          print("X Wins!")
          break
     elif board3 == ["X", "X", "X"]:
          print("X Wins!")
          break
     elif board1[0] == board2[1] == board3[2] == "X":
          print("X Wins!")
          break
     elif board1[2] == board2[1] == board3[0] == "X":
          print("X Wins!")
          break
     elif board1[0] == board2[0] == board3[0] == "X":
          print("X Wins!")
          break
     elif board1[1] == board2[1] == board3[1] == "X":
          print("X Wins!")
          break
     elif board1[2] == board2[2] == board3[2] == "X":
          print("X Wins!")
          break
     else:
          print("Tied!")
          break