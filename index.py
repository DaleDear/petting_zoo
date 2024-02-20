# import the python datetime module to help us create a timestamp
""" from datetime import date """

from Slithering import PoisonousSnake, NonPoisonousSnake, TriColorSnake, BlackSnake, AlbinoSnake
from Swimming import Duck, Fish, Swan, Frog, Turtle
from Walking import Donkey, Llama, Goat, Horse, Cow

painful_perry = PoisonousSnake("Painful Perry", "copperhead")
pleasant_paula = NonPoisonousSnake("Pleasant Paula", "common king snake")
robert = BlackSnake("Robert", "rat snake")
tammy = TriColorSnake("Tammy", "tricolor hognose")
albert = AlbinoSnake("Albert", "albino python")
dolly = Donkey("Dolly", "miniature donkey")
miss_fuzz = Llama("Miss Fuzz", "domestic llama")
miss_georgia = Goat("Miss Georgia", "nanny goat")
gus = Horse("Gus", "american quarter horse")
clara = Cow("Clara", "miniature scottish highland")
mama = Duck("Mama", "mallard")
goldie = Fish("Goldie", "goldfish")
princess_tiffany = Swan("Princess Tiffany", "black-necked swan")
fred = Frog("Fred", "bullfrog")
lord_heathrow = Turtle("Lord Heathrow", "snapping turtle")

print(miss_fuzz.name)
print(miss_fuzz.species)

print(fred.name)
print(fred.species)
