class Car:
    def __init__(self, brand, model, turns=10):
        self.brand = brand
        self.model = model
        self.__turns = turns

    def go(self, distance):
        self.__turns -= distance
        if self.__turns < 0:
            self.__turns = 0
        print(f"You have traveled {distance} units")
        print(f"You have {self.__turns} turns left...")

    def windup(self, turns):
        self.__turns += turns
        print(f"Winding it up by {turns} turns! Total turns: {self.__turns}.")

    def get_turns(self):
        return self.__turns


car = Car("Beeper", "3000OA")

while 0 < car.get_turns() <= 15:
    act = input("What do we do? (windup or go) ").strip().lower()
    if act == "go":
        distance = int(input("How far? "))
        car.go(distance)
    elif act == "windup":
        turns = int(input("How many turns to windup? "))
        car.windup(turns)
    else:
        print("Invalid action.")

if car.get_turns() > 15:
    print(f"uhh your toy {car.brand} {car.model} was windup too hard, it kinda jammed so u lose")
else:
    print("Game over! 0 turns left :[")