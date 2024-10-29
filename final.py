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
     XOne = playing("X's")
     if XOne == 1:     #Conditionals
          board1[0]="X"
     elif XOne == 2:
          board1[1]="X"
     elif XOne == 3:
          board1[2]="X"
     elif XOne == 4:
          board2[0]="X"
     elif XOne == 5:
          board2[1]="X"
     elif XOne == 6:
          board2[2]="X"
     elif XOne == 7:
          board3[0]="X" 
     elif XOne == 8:
          board3[1]="X"
     elif XOne == 9:
          board3[2]="X"
     else:
          print("You cannot input that")
     print("", board1,"\n", board2,"\n", board3)

#Player 2 input - Nathaly
#Function 2
     OOne = playing("O's")
     if OOne==XOne:
          print("You can't input that")
     elif OOne == 1:
          board1[0]="O"
     elif OOne == 2:
          board1[1]="O"
     elif OOne == 3:
          board1[2]="O"
     elif OOne == 4:
          board2[0]="O"
     elif OOne == 5:
          board2[1]="O"
     elif OOne == 6:
          board2[2]="O"
     elif OOne == 7:
          board3[0]="O" 
     elif OOne == 8:
          board3[1]="O"
     elif OOne == 9:
          board3[2]="O"
     else:
          print("You cannot input that")
     print("", board1,"\n", board2,"\n", board3)

#Keep going - Isaac
     XTwo = playing("X's")
     if XTwo==OOne or XTwo==XOne:
          print("You can't input that")
     elif XTwo == 1:
          board1[0]="X"
     elif XTwo == 2:
          board1[1]="X"
     elif XTwo == 3:
          board1[2]="X"
     elif XTwo == 4:
          board2[0]="X"
     elif XTwo == 5:
          board2[1]="X"
     elif XTwo == 6:
          board2[2]="X"
     elif XTwo == 7:
          board3[0]="X" 
     elif XTwo == 8:
          board3[1]="X"
     elif XTwo == 9:
          board3[2]="X"
     else:
          print("You cannot input that")
     print("", board1,"\n", board2,"\n", board3)

     OTwo = playing("O's")
     if OTwo==XOne or OTwo==OOne:
          print("You cannot input that")
     elif OTwo == 1:
          board1[0]="O"
     elif OTwo == 2:
          board1[1]="O"
     elif OTwo == 3:
          board1[2]="O"
     elif OTwo == 4:
          board2[0]="O"
     elif OTwo == 5:
          board2[1]="O"
     elif OTwo == 6:
          board2[2]="O"
     elif OTwo == 7:
          board3[0]="O" 
     elif OTwo == 8:
          board3[1]="O"
     elif OTwo == 9:
          board3[2]="O"
     else:
          print("You cannot input that")
     print("", board1,"\n", board2,"\n", board3)

     XThree = playing("X's")
     if XThree==OOne or XThree==OTwo or XThree==XOne or XThree==XTwo:
          print(("You can't input that"))
     elif XThree == 1:
          board1[0]="X"
     elif XThree == 2:
          board1[1]="X"
     elif XThree == 3:
          board1[2]="X"
     elif XThree == 4:
          board2[0]="X"
     elif XThree == 5:
          board2[1]="X"
     elif XThree == 6:
          board2[2]="X"
     elif XThree == 7:
          board3[0]="X" 
     elif XThree == 8:
          board3[1]="X"
     elif XThree == 9:
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

     OThree = playing("O's")
     if OThree==XOne or OThree==XTwo or OThree==XThree or OThree==OOne or OThree==OTwo:
          print("You can't input that")
     elif OThree == 1:
          board1[0]="O"
     elif OThree == 2:
          board1[1]="O"
     elif OThree == 3:
          board1[2]="O"
     elif OThree == 4:
          board2[0]="O"
     elif OThree == 5:
          board2[1]="O"
     elif OThree == 6:
          board2[2]="O"
     elif OThree == 7:
          board3[0]="O" 
     elif OThree == 8:
          board3[1]="O"
     elif OThree == 9:
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

     XFour = playing("X's")
     if XFour==OOne or XFour==OTwo or XFour==OThree or XFour==XOne or XFour==XTwo or XFour==XThree:
          print("You can't input that")
     elif XFour == 1:
          board1[0]="X"
     elif XFour == 2:
          board1[1]="X"
     elif XFour == 3:
          board1[2]="X"
     elif XFour == 4:
          board2[0]="X"
     elif XFour == 5:
          board2[1]="X"
     elif XFour == 6:
          board2[2]="X"
     elif XFour == 7:
          board3[0]="X" 
     elif XFour == 8:
          board3[1]="X"
     elif XFour == 9:
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

     OFour = playing("O's")
     if OFour==XOne or OFour==XTwo or OFour==XThree or OFour==XFour or OFour==OOne or OFour==OTwo or OFour==OThree:
          print("You cannot input that")
     elif OFour == 1:
          board1[0]="O"
     elif OFour == 2:
          board1[1]="O"
     elif OFour == 3:
          board1[2]="O"
     elif OFour == 4:
          board2[0]="O"
     elif OFour == 5:
          board2[1]="O"
     elif OFour == 6:
          board2[2]="O"
     elif OFour == 7:
          board3[0]="O" 
     elif OFour == 8:
          board3[1]="O"
     elif OFour == 9:
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

     XFive = playing("X's")
     if XFive==OOne or XFive==OTwo or XFive==OThree or XFive==OFour or XFive==OFour or XFive==XOne or XFive==XTwo or XFive==XThree or XFive==XFour:
          print(slot(X))
     elif XFive == 1:
          board1[0]="X"
     elif XFive == 2:
          board1[1]="X"
     elif XFive == 3:
          board1[2]="X"
     elif XFive == 4:
          board2[0]="X"
     elif XFive == 5:
          board2[1]="X"
     elif XFive == 6:
          board2[2]="X"
     elif XFive == 7:
          board3[0]="X" 
     elif XFive == 8:
          board3[1]="X"
     elif XFive == 9:
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

#Add one O Turn