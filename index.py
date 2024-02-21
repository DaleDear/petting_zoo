# import the python datetime module to help us create a timestamp
""" from datetime import date """

from Slithering import PoisonousSnake, NonPoisonousSnake, TriColorSnake, BlackSnake, AlbinoSnake
from Swimming import Duck, Fish, Swan, Frog, Turtle
from Walking import Donkey, Llama, Goat, Horse, Cow

painful_perry = PoisonousSnake("Painful Perry", "copperhead", "snake chow")
pleasant_paula = NonPoisonousSnake("Pleasant Paula", "common king snake", "snake chow")
robert = BlackSnake("Robert", "rat snake", "snake chow")
tammy = TriColorSnake("Tammy", "tricolor hognose", "snake chow")
albert = AlbinoSnake("Albert", "albino python", "snake chow")
dolly = Donkey("Dolly", "miniature donkey", "afternoon", "donkey chow")
miss_fuzz = Llama("Miss Fuzz", "domestic llama", "midday", "llama chow")
miss_georgia = Goat("Miss Georgia", "nanny goat", "afternoon", "goat chow")
gus = Horse("Gus", "american quarter horse", "morning", "horse chow")
clara = Cow("Clara", "miniature scottish highland", "morning", "cow chow")
mama = Duck("Mama", "mallard", "duck chow")
goldie = Fish("Goldie", "goldfish", "goldfish chow")
princess_tiffany = Swan("Princess Tiffany", "black-necked swan", "swan chow")
fred = Frog("Fred", "bullfrog", "frog chow")
lord_heathrow = Turtle("Lord Heathrow", "snapping turtle", "turtle chow")

print(miss_fuzz.name)
print(miss_fuzz.species)

print(fred.name)
print(fred.species)

print(f"{dolly.name} the {dolly.species} is available to pet during the {dolly.shift} shift.")

print(miss_fuzz.feed())
print(tammy.feed())
print(fred.feed())

print(miss_fuzz)
print(painful_perry)
print(pleasant_paula)
print(miss_georgia)
print(princess_tiffany)
print(lord_heathrow)

