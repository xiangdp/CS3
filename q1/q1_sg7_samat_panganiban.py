class Glassware:
    def __init__(self, brand):
        self.brand = brand

class Beaker(Glassware):
    def __init__(self, brand, volume, unitused):
        super().__init__(brand)
        self.volume = volume; self.unitused = unitused

    def __del__(self):
        print(f"The {self.brand} beaker with a capacity of {self.volume} {self.unitused} is lost.")

class Tray:
    def __init__(self, name, bbrand, bvolume, bunitused):
        self.name = name
        self.beaker = [Beaker(brand = bbrand, volume = bvolume, unitused = bunitused) for i in range(5)]

    def check_beakers(self):
        for beaker in self.beaker:
            print(f"There is a {beaker.brand} beaker with a capacity of {beaker.volume} {beaker.unitused} here.")

    def __del__(self):
        print(f"{self.name} has been removed from inventory.")


tray1 = Tray("Beaker Tray", "Pyrex", "250", "mL")

tray1.check_beakers()

input("Press [enter] to delete tray:")

del tray1
