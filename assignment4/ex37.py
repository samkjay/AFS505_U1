print("This is a program to use \"symbols\" in the exercise")
print("\tInput a number between 1 and 10")
number = input(">")

if number == "5":
    print("This would be good place to start")
    print(f"If you add 5 more to the number, the total would be {int(number) + 5}")
elif number <= "5":
    print(f"If you divide the number by 2 the answer is {int(number)/2}")
else:
    print(f"Your number is {number}")


print("Now let's input another number less than 10")
n_number = input(">")
print(f"Your number is {n_number}")

numbers = []
print("Let's see all the numbers from 0 to your number")
for i in range (0, int(n_number)):
    print(f"There is {i}")
    numbers.append(i)

print(f"All the numbers upto your number is {numbers}")
