from classes.animals import *

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name):
        self.animals.append( Lion(name) )

    def add_tiger(self, name):
        self.animals.append( Tiger(name) )

    def add_bear(self, name):
        self.animals.append( Bear(name) )

    def print_all_info(self):
        for animal in self.animals:
            animal.display_info()