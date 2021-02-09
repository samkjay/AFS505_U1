all_numbers = []
end_number = 6

for i in range (0, end_number):
    all_numbers.append(i)
    print(f"At the top i is {i}")
    print("Numbers now: ", all_numbers)
    i = i + 1
    print(f"At the bottom i is {i}")


print(f"The numbers {all_numbers}")
