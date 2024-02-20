from datetime import date

class Horse:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.location = "The Petting Zoo"
        self.walking = True
        self.date_added = date.today()