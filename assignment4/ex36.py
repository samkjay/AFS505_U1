from sys import exit

def gift_room():
    print("you have won the game, you escaped!")
    print("You get a gift! do you want the big one or the small one?")

    gift = input(">")

    if gift == "big":
        print("Wrong choice! it's just an empty box!")
        exit(0)
    else:
        dead("Good for you! it's a gold watch!")

def clue_1():
    print("There are four chairs in the room.")
    print("and three cats.")
    print("And five crows")
    print("How many total legs are in the room? Type in a number. ")

    choice  = input(">")

    if choice < 42:
        dead("A door opens and a lion eats you.")
    elif choice == 42:
        print("A door opens. You can go through it now.")
        gift_room()
    else:
        print("Wrong answer. try again.")
        clue_1()


def clue_2():
    print("Who has more eyes? a spider or an octopus?")

    eyes = input(">")

    if eyes == "spider":
        print("You are right. you escaped!")
        gift_room()
    elif eyes == "octopus":
        dead("A giant spider eats you!")
    else:
        clue_2()

def dead(why):
    print(why)
    exit(0)

def start():
    print("This is an escape room game. you have to solve clues to get out. do you want clue 1 or 2 first?")

    choice = input(">")

    if choice =="1":
        clue_1()
    elif choice == "2":
        clue_2()
    else:
        dead("You stumble around the room until you starve.")

start()
