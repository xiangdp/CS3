class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount
        print(f"Oh no! {self.name} took {amount} damage!")


arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)


def display_hp():
    print(f"""
{morgana.name}'s HP: {morgana.hp}
{arthur.name}'s HP: {arthur.hp}
""")

display_hp()

arthur.take_damage(10)

display_hp()
