print("""You enter a dark room with three doors.
Do you go through door #1, #2 or #3?""")

door = input(">")

if door == "1":
    print("There's a giant beat here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear")

    bear = input(">")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats you legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door =="2":
    print("You stare in to the endless abyss at Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input(">")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("You stumble around and fall on a knife and die. Good job!")

elif door == "3":
    print("You have two pills on a table")
    print("1. You take the red pill")
    print("2. You take the blue pill")
    print("what do you do?")

    pill = input(">")

    if pill == "1":
         print("welcome to the matrix!")
    elif pill == "2":
         print("You escaped a horrible tragedy!")
         print("You are in a field of flowers")
         print("Good job!")
    else:
        print("That is not an option. You have to take a pill!")
