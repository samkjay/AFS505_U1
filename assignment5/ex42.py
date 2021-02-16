#Animal is-a object(yes, sort of confusing)look at the extra credit
class Animal(object):
    pass

##Dog is-a animal
class Dog(Animal):
    def __init__(self, name):
        #Dog has a name
        self.name = name

#Cat is-a animal
class Cat(Animal):
    def __init__(self, name):
        #Cat has a name
        self.name = name

#Person is-a object
class Person(object):
    def __init__(self, name, pet):
        #Persom has a name
        self.name = name

        #Person has a pet of some kind
        self.pet = pet

    def write_name(self):
        print(self.name)

    def write_pet(self):
        print(self.pet)


#Employee is a person
class Employee(Person):
    def __init__(self, name, salary, pet):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name, pet)
        #Employee has a salary
        self.salary = salary

    def write_salary(self):
        print(self.salary)

#Fish is an object
class Fish(object):
    pass

#Salmon is a fish
class Salmon(Fish):
    pass

#Halibut is a fish
class Halibut(Fish):
    pass

#rover is-a Dog
rover = Dog("Rover")

##satan is a Cat
satan = Cat("Satan")
tabby = Cat("Garfeild")


#mary is a person
mary = Person("Mary", tabby)

mary.write_name()

#mary's has a cat named saten
mary.pet = satan

#frank is an employee who has a salary of 120000
frank = Employee("Frank", 120000, rover.name)

frank.write_name()
frank.write_pet()
frank.write_salary()

print(f"{frank.name} is an employee who has a ${frank.salary}")
print(f"{frank.name} has a pet dog named {frank.pet}")

#frank has a pet named rover
frank.pet = rover

#Flipper is a fish
flipper = Fish()

#crouse is a Salmon
crouse = Salmon()

#harry is a Halibut
harry = Halibut()

gus = Cat("Gus")



My_name = Person("Sam", gus.name)


My_name.write_name()

My_name.write_pet()

print(f"My name is {My_name.name} and I have a orange tabby cat named {My_name.pet}")
