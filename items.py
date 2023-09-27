#############
### ITEMS ###
#############
class armor:
    def __init__(self, dfc):
        self.dfc = dfc

class weapon:
    def __inint__(self, atk):
        self.atk = atk

class consumable:
    def __init__(self, effect):
        self.effect = effect

class healing_potions(consumable):
    def __init__(self, effect):
        super().__init__(effect)