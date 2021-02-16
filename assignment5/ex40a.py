mystuff = {'apple': "I AM APPLES!",
           'tangerine': "Living a reflection of a dream"}
print(mystuff['apple'])
print(mystuff['tangerine'])


import mystuff
mystuff.apple()

def apple():
  print("I AM APPLES!")

# This is just a variable
#tangerine = "Living reflection of a dream"

import mystuff

mystuff.apple()
print(mystuff.tangerine)

mystuff['apple']# I get apple from the dictionary
mystuff.apple() #get apple from the module
mystuff.tangerine # same thing. It's just variable

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES")

thing = MyStuff()
thing.apple()
print(thing.tangerine)

#Getting things
#dict style
#mystuff['apple']

#module style
mystuff.apple()
print(mystuff.tangerine)

#class style
thing = MyStuff()
thing.apple()
print(thing.tangerine)
