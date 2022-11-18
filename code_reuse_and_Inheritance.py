""" Calculates number of animals in the zoo and reptiles specifically"""
# Define new class
class Animal:
    name = ""
    category = ""
    def __init__(self, name):
        self.name = name
    def set_category(self, category):
        self.category = category
# Classes Turtle and Snake inherited from Animal class
class Turtle(Animal):
    category="reptile"

class Snake(Animal):
    category="reptile"

class Zoo:
    def __init__(self):
        self.current_animals = {}
    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category
    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if "reptile" == category:
                result += 1
        return result
zoo = Zoo()

turtle = Turtle("Turtle")
snake = Snake("Snake")
zoo.add_animal(turtle)
print(turtle.name+" "+turtle.category)
print(snake.name+" "+snake.category)
zoo.add_animal(snake)
print(zoo.current_animals)
print(zoo.total_of_category("reptile"))