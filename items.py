#############
### ITEMS ###
#############
class armor:
    def __init__(self, dfc):
        self.dfc = dfc

class weapon:
    def __init__(self, atk):
        self.atk = atk

class melee(weapon):
    def __init__(self, atk):
        super().__init(self, atk)

class ranged(weapon):
    def __init__(self, atk, range):
        super().__init__(self, atk)
        self.range = range

class magic_weapon(weapon):
    def __init__(self, atk):
        super().__init__(self, atk)

class staff(magic_weapon):
    def __init__(self, atk):
        super().__init__(self, atk)

class consumable:
    def __init__(self, effect):
        self.effect = effect

class healing_potions(consumable):
    def __init__(self, effect):
        super().__init__(effect)

class mana_potions(consumable):
    def __init__(self, effect):
        super().__init__(effect)