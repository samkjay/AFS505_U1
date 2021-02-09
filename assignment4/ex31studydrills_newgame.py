print("A farmer brings you a potato with an unknown disease.")
print("What do you do?")
print("1. Observe the sample under the microscope.")
print("2. Culture a piece of the sample in PDA.")

step1 = input(">")

if step1 == "1":
    print("Do you see pathogen structures?")
    print("1. Yes")
    print("2. No")

    structures = input(">")

    if structures == "1":
       print("Do you see mycelia?")
       print("1. Yes")
       print("2. No")

       mycelia = input(">")

       if mycelia == "1":
             print("Your pathogen is a fungus!")
       else:
             print("Your pathogen may be a bacteria or virus.")

else:
    print("Do you see a growth?")
    print("1. Yes")
    print("2. No")

    growth  = input(">")

    if growth  == "1":
        print("You may have fungi or bacteria!")
    else:
        print("You may have a protist or virus. Try extracting DNA and sequencing.")
