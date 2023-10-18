#############
### ITEMS ###
#############
class armor:
    def __init__(self, dfc):
        self.dfc = dfc

class weapon:
    def __init__(self, atk):
        self.atk = atk

class melee(weapon): #Bare for melee angrep (sverd, spyd, klubber, økser, evt. med fortryllelser på seg).
    def __init__(self, atk):
        super().__init__(atk)

class staff(weapon): #Bare for magi-relaterte angrep (spells, o.s.v.), kan muligens sies at kan brukes som en svak klubbe.
    def __init__(self, atk):
        super().__init__(atk)

class ranged(weapon): #Bare for lang distanse angrep (buer, armbrøst)
    def __init__(self, atk):
        super().__init__(atk)

class consumable:
    def __init__(self, effect):
        self.effect = effect

class potions(consumable): #Gir enten hp eller mana ved bruk.
    def __init__(self, effect): #Effekt her henviser til hvor mye hp/mana som blir fylt.
        super().__init__(effect)

class healing_potions(potions): #Gir hp ved bruk.
    def __init__(self, effect): #Effekt her henviser til hvor mye hp som blir fylt.
        super().__init__(effect)

class mana_potions(potions): #Gir mp ved bruk.
    def __init__(self, effect): #Effekt her henviser til hvor mye mp som blir fylt.
        super().__init__(effect)

class tomes(consumable): #Brukes for å utføre et magisk angrep uten å selv bruke mana.
    def __init__(self, effect, uses): #Effekt her henviser til mengde skade.
        super().__init__(effect)
        self.uses = uses

leather_armor = armor(2)
chainmail_armor = armor(5)
iron_armor = armor(7)
mythril_armor = armor(10)

sword = melee(3)
spear = melee(5)
club = melee(2)
axe = melee(4)
the_throngler = melee(10)

grimoire = staff(3)
great_staff = staff(5)
branch_of_the_world_tree = staff(10)

shortbow = ranged(3)
crossbow = ranged(4)
longbow = ranged(5)


lesser_healing_potion = healing_potions(2)
medium_healing_potion = healing_potions(3)
greater_healing_potion = healing_potions(5)

lesser_mana_potion = mana_potions(2)
medium_mana_potion = mana_potions(3)
greater_mana_potion = mana_potions(5)

lightning_tome = tomes(5, 2)
fire_tome = tomes(5, 2)
ice_tome = tomes(5, 2)
water_tome = tomes(5, 2)
light_tome = tomes(5, 2)
dark_tome = tomes(5, 2)

#Command som skal aktiveres når en item blir brukt. Fungerer ikke helt enda.
def use(item):
    klasse = item.__class__
    if klasse == healing_potions:
        return item.effect
        #Må lage en kode som fjerner den fra bag.
    elif klasse == mana_potions:
        return item.effect
        #Må lage en kode som fjerner den fra bag.
    elif klasse == tomes:
        item.uses -= 1
        if item.uses <= 0:
            #Må lage en kode som fjerner den fra bag.
            print("Tome gone")
        return item.effect
    else:
        print("Class not defined")