class Song(object):

   def __init__(self, lyrics):
       self.lyrics = lyrics

   def sing_me_a_song(self):
       for line in self.lyrics:
           print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells "])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


my_favourite_things = Song(["Rain drops on roses and",
                            "Whiskers on kittens"])

my_favourite_things.sing_me_a_song()

#putting lyrics in a variable

sound_of_music = "Rain drops on roses and,\n Whiskers on kittens"

my_favourite_things_again = Song([sound_of_music])

my_favourite_things_again.sing_me_a_song()
