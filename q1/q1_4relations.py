# AGGREGATION
"""
class Sauce:
    def __init__(self, name, taste):
        self.name = name; self.taste = taste
        print(self.name, "is ready.")
    def __del__(self):
        print(self.name, "is ubos na.")

class Tusoktusok:
    def __init__(self, name, sauce):
        self.name = name
        self.sauce = sauce
        print(self.name, "is cooked and has", self.sauce.name)
    def eat(self):
        print("I am eating", self.name, "and it tastes", self.sauce.taste)
    def __del__(self):
        print(self.name, "was thrown in the trash can.")

hotsauce = Sauce("Hot Sauce", "spicy")
fishball = Tusoktusok("fishball", hotsauce)
fishball.eat()
del fishball
print(hotsauce.name)
"""

# DEPENDENCY
"""
class Sauce:
    def __init__(self, name, taste):
        self.name = name
        self.taste = taste
        print(self.name, "is ready.")
        
    def __del__(self):
        print(self.name, "is ubos na.")

class Tusoktusok:
    def __init__(self, name, sauce = None):
        self.name = name
        self.sauce = sauce
        print(self.name, "is cooked")
        if self.sauce != None:
            print("It is dipped in", self.sauce.name)
            
    def eat(self):
        print("I am eating", self.name)
        if self.sauce != None:
            print("It tastes", self.sauce.taste)
            
    def dip(self, sauce):
        self.sauce = sauce
        print(self.name, "was dipped in", self.sauce.name)
        
    def __del__(self):
        print(self.name, "was thrown as trash...")


hotsauce = Sauce("Hot Sauce", "spicy")
fishball = Tusoktusok("fishball", hotsauce)
fishball.eat()

kikiam = Tusoktusok("kikiam")
kikiam.eat()

kikiam.eat()
kikiam.dip(hotsauce)
kikiam.eat()
"""

# Composition
"""
class Nucleus:
    def __init__(self):
        print("Nucleus is created.")
    def __del__(self):
        print("Nucleus is gone.")

class Mitochondria:
    def __init__(self):
        print("Mitochondria is created.")
    def providePower(self):
        print("Mitochondria is powering the cell.")
    def __del__(self):
        print("Mitochondria is gone.")

class Cell:
    def __init__(self):
        print("Cell is created.")
        self.nucleus = Nucleus()
        self.mitochondria = Mitochondria()
        
    def exist(self):
        print("Cell is existing.")
        self.mitochondria.providePower()
        
    def __del__(self):
        del self.nucleus
        del self.mitochondria
        print("Cell is gone.")

cellAtWork = Cell()
cellAtWork.exist()
del cellAtWork
"""

# Ineritance
"""
class Vehicle:
    def __init__(self, kindofvehicle):
        self.kindofvehicle = kindofvehicle
        print(self.kindofvehicle, "created")
    def move(self, distance):
        print(self.kindofvehicle, "moved", distance, end=" ")

class Car(Vehicle):
    def __init__(self, kindofvehicle, brand, model):
        self.brand = brand; self.model = model
        super().__init__(kindofvehicle)
        print("I have a", self.brand, self.model)
    def move(self, distance):
        super().move(distance)
        print("KM")

class Boat(Vehicle):
    def __init__(self, kindofvehicle, model):
        self.model = model
        super().__init__(kindofvehicle)
        print("I have a", self.model)
    def move(self, distance):
        super().move(distance)
        print("Nm")

vios = Car("car", "Toyota", "Vios")
vios.move(67)
ferry = Boat("ferry", "SS Trisha Paytas")
ferry.move(15)
yacht = Boat("yacht", "Ocean Gate")
yacht.move(17)
"""
