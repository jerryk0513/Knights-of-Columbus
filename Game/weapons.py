class Weapon:
    def __init__(self, name, damage, weight, weapon_type):
        self.name = name
        self.damage = damage
        self.weight = weight
        self.weapon_type = weapon_type

    def info(self):
        return f"{self.name}: {self.damage} damage, {self.weight} weight, {self.weapon_type}"

weapon_data = [
    ("Sword", 20, 5, "melee"),
    ("Axe", 35, 8, "melee"),
    ("Bow", 25, 4, "ranged"),
    ("Spear", 30, 6, "melee"),
    ("Dagger", 15, 2, "melee"),
    ("Crossbow", 40, 7, "ranged"),
    ("Mace", 30, 9, "melee"),
    ("Halberd", 45, 12, "melee"),
    ("Flail", 25, 6, "melee"),
    ("Warhammer", 50, 10, "melee"),
]

weapons = []

for name, damage, weight, weapon_type in weapon_data:
    weapons.append(Weapon(name, damage, weight, weapon_type))

for weapon in weapons:
    print(weapon.info())