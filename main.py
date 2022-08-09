from classes.zoo import Zoo

zoo1 = Zoo("Robert's Zoo")

zoo1.add_bear("Winnie")
zoo1.add_lion("Poppy")

for animal in zoo1.animals:
    if animal.name == "Winnie":
        animal.birthday()

zoo1.print_all_info()