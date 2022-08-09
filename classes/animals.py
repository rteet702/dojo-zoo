class Animal:
    instances = []

    def __init__(self, name, health, happiness, animal_type):
        self.name = name
        self.age = 0
        self.health = health
        self.happiness = happiness
        self.animal_type = animal_type

        # Store new instances in the list.
        Animal.instances.append(self)

    def display_info(self):
        print(f'Name: {self.name}, Type: {self.animal_type}, Health: {self.health}%, Happiness: {self.happiness}%')
        return self

    def feed(self):
        self.health = self.health + 10 if self.health + 10 <= 100 else 100
        self.happiness = self.happiness + 10 if self.happiness + 10 <= 100 else 100
        return self

    def birthday(self):
        self.age += 1


class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, health = 100, happiness = 100, animal_type = "Lion")


class Tiger(Animal):
    def __init__(self, name):
        super().__init__(name, health = 50, happiness = 75, animal_type = "Tiger")


class Bear(Animal):
    def __init__(self, name):
        super().__init__(name, health = 30, happiness = 50, animal_type = "Bear")