class Animal:
    def __init__(self, name, age, health=50, happiness=50):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def feed(self):
        self.health += 10
        self.happiness += 10
        return self

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Health: {self.health}")
        print(f"Happiness: {self.happiness}")


class Lion(Animal):
    def __init__(self, name, age, mane_size):
        super().__init__(name, age)
        self.mane_size = mane_size

    def feed(self):
        self.health += 15
        self.happiness += 10
        return self

    def display_info(self):
        super().display_info()
        print(f"Mane Size: {self.mane_size}")
        print("-" * 30)


class Monkey(Animal):
    def __init__(self, name, age, favorite_food):
        super().__init__(name, age)
        self.favorite_food = favorite_food

    def feed(self):
        self.health += 10
        self.happiness += 20
        return self

    def display_info(self):
        super().display_info()
        print(f"Favorite Food: {self.favorite_food}")
        print("-" * 30)


class Bear(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def feed(self):
        self.health += 20
        self.happiness += 5
        return self

    def display_info(self):
        super().display_info()
        print(f"Fur Color: {self.fur_color}")
        print("-" * 30)


class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        return self

    def feed_all_animals(self):
        for animal in self.animals:
            animal.feed()
        return self

    def print_all_info(self):
        print("-" * 20, self.name, "-" * 20)
        for animal in self.animals:
            animal.display_info()
        return self


# Create animal objects
lion1 = Lion("Simba", 5, "Large")
monkey1 = Monkey("George", 3, "Banana")
bear1 = Bear("Baloo", 7, "Brown")

# Create zoo object
zoo1 = Zoo("Abdallah's Zoo")

# Add animals to zoo
zoo1.add_animal(lion1).add_animal(monkey1).add_animal(bear1)

# Feed all animals and display info
zoo1.feed_all_animals().print_all_info()