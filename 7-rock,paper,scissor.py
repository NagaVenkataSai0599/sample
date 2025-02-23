import random
totalTrails=int(input("Total trails:"))
i=1
yourPoints=compPoints=0
while i<=totalTrails:
    yourChoice=int(input("0-Rock\n1-Paper\n2-Scissor\nEnter your choice:"))
    if yourChoice not in [0,1,2] :
        print("Please enter an valid choice")
        yourChoice=int(input("0-Rock\n1-Paper\n2-Scissor\nEnter your choice:"))
    compChoice=random.randint(0,2)
    print("Oppenent Choice is:",compChoice)
    if(yourChoice==compChoice):
        print("Draw")
    elif(yourChoice==0 and compChoice==2):
        print("You Won")
        yourPoints+=1
    elif(yourChoice==2 and compChoice==0):
        print("You Loss")
        compPoints+=1
    elif(yourChoice>compChoice):
        print("You Won")
        yourPoints+=1
    elif(compChoice>yourChoice):
        print("You Lose")
        compPoints+=1
    else:
        print("Enter an valid input")
    i+=1
if yourPoints>compPoints:
    print("Yours points: ",yourPoints,"\t Opponents Points: ",compPoints)
    print("CONGRACTULATIONS!!!!\n\tYOU WON!!!")
elif yourPoints==compPoints:
    print("Yours points: ",yourPoints,"\t Opponents Points: ",compPoints)
    print("Match Drawn")
else:
    print("Yours points: ",yourPoints,"\t Opponents Points: ",compPoints)
    print("You Lost....\nBetter Luck Next Time")

