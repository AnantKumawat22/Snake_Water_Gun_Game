import random


def match(comp, you):
    if(comp == you):
        return None
    if(comp == "Snake"):
        if(you == "Water"):
            return False
        elif(you == "Gun"):
            return True
    elif(comp == "Water"):
        if(you == "Gun"):
            return False
        elif(you == "Snake"):
            return True
    elif(comp == "Gun"):
        if(you == "Snake"):
            return False
        elif(you == "Water"):
            return True


comp = random.randint(1,3)
print()
print("----- Snake, Water and gun Game.-----")
print()
print("Rules of the Game :-")
print(" ->Snake win over Water.")
print(" ->Water win over Gun.")
print(" ->Gun win over Snake.")
print("**Enter x for exit.")
print()

while(True):
    you = input("Enter (s)->Snake , (w)->Water and (g)->Gun.")

    if(comp == 1):
        comp = "Snake"
    if(comp == 2):
        comp = "Water"
    if(comp == 3):
        comp = "Gun"

    if(you == "s"):
        you = "Snake"
    if(you == "w"):
        you = "Water"
    if(you == "g"):
        you = "Gun"

    result = match(comp,you)
    if(result == None):
        print("Match tie :|")
        print()
        print(f"Computer Choose {comp}.")
        print(f"You Choose {you}.")
    elif(result == False):
        print("Opps...You Loose :(")
        print()
        print(f"Computer Choose {comp}.")
        print(f"You Choose {you}.")
    else:
        print("Congrats...You Win :)")
        print()
        print(f"Computer Choose {comp}.")
        print(f"You Choose {you}.")

    print()
    ch = input("Press Enter for continue")
    if(ch == "x"):
        break