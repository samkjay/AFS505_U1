people = 30
cars = 40
trucks = 15

# test if cars are greater than people and if it's true print the statement
if cars > people:
    print("We should take the cars.")
# if the above argument is false, then test if cars are less than people, and if it's true print the statement
elif cars < people:
    print("We should not take the cars.")
# if the above argument is false, then print the statement
else:
    print("We can't decide.")

# test if trucks are greater than cras and if it's true print the statement
if trucks > cars:
    print("That's too may trucks.")
# if the above argument is false, then test if trucks are less than cars, and if it's true print the statement
elif trucks < cars:
    print("Maybe we could take the trucks.")
# if the above argument is false, then print the statement
else:
    print("WE still can't decide.")

#test if people are greater than trucks, an dif it's true print the statement
if people > trucks:
    print("Alright, let's just take the trucks.")
#if the above test is falsem then print the statement.
else:
    print("Fine, lets' stay home then.")

if cars > people:
    print("Too many cars!")
elif cars < people:
    print("Not enough cars.")
else:
    print("We can all drive today!")
