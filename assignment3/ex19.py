#define the function cheese_and_crackers and it's arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

#directly assigning numbers to the function
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

#using numbers from the script to assign value to the function
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#assigning numbers to the function by doing math
print("We can even do math inside too:")

cheese_and_crackers(10+20, 5+6)

#assigning numbers by variables and math
print("and we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)


#my own function

def fruits_and_vegetables(fruit_types, veggie_types):
    print(f"I ate {fruit_types} differnt fruits this week")
    print(f"I try to eat atleast {veggie_types} vegetables a week\n")

#by assigning numbers thrugh script
fruits = 3
vegetables = 5
fruits_and_vegetables(fruits, vegetables)

#by doing math
fruits_and_vegetables (3+4, 5+1)

#directly assiging numbers
fruits_and_vegetables(3, 4)

# script and math
fruits_and_vegetables(fruits+3, vegetables+5)
