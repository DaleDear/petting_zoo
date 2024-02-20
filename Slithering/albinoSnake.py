from datetime import date

class AlbinoSnake:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.location = "The Glass Tank"
        self.slithering = True
        self.date_added = date.today()
