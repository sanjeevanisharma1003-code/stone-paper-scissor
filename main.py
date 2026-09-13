import random
computer=random.randint(1,3)
yourchoice=input("Enter your choice:  ")

yourdict={
    "stone":1,
    "scissor":2,
    "paper":3
}
reversedict={
    1:"stone",
    2:"scissor",
    3:"paper"
}

you=yourdict[yourchoice]
print(f"you chose {yourchoice}, computer chose {reversedict[computer]}")
if(you==computer ):
    print("Draw...!!")
else:
    if(you==1 and computer==2):
        print("You win!! ")
    elif(you==1 and computer==3):
        print("You lose!!")
    elif(you==2 and computer==1):
        print("You lose!!")
    elif(you==2 and computer==3):
        print("You win!!")
    elif(you==3 and computer==1):
        print("You win!!")
    elif(you==3 and computer==2):
        print("You lose!!")
    else:
        print("Invalid input")
