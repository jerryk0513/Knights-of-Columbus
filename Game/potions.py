class Potion:
    def __init__(self, name, damage, weight, potion_type):
        self.name = name
        self.damage = damage
        self.weight = weight
        self.potion_type = potion_type
    def info(self):
        return f"{self.name}: {self.damage} damage, {self.weight} weight, {self.potion_type}"

Potion_data = [
    ("Health", 10, 1, "healing"),
    ("Mana", 15, 1, "mana"),
    ("Strength", 20, 2, "buff"),
    ("Speed", 25, 2, "buff"),
]
