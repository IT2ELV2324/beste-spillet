#################################
### ALLE FORSKJELLIGE FIENDER ###
#################################

import random

class EnemyAttack: #definerer skade av angrep
    def __init__(self, name, min_damage, max_damage):
        self.name = name
        self.min_damage = min_damage #minimun skade for angrepet
        self.max_damage = max_damage #max skade for angrepet

    def perform_attack(self): 
        damage = random.randint(self.min_damage, self.max_damage) #skade-verdi random mellom minimum og max skade
        return damage

class Enemy: #definerer navn på enemies
    def __init__(self, name,hp):
        self.name = name
        self.hp = hp
        self.attacks = [ #ulike angrep med minimum og max skade
            EnemyAttack("beit", 20, 25),
            EnemyAttack("slo", 2, 10),
            EnemyAttack("sparket", 30, 35),
            EnemyAttack("klorte", 3, 10)
        ]

    def velg_attack(self): #velger random angrep
        return random.choice(self.attacks)

enemy1 = Enemy("Slemsing",20)
enemy2 = Enemy("Goblin",35)
enemy3 = Enemy("Spøkelse",50)
enemy4 = Enemy("Vamp",80)

print(f"{enemy1.name} {enemy1.velg_attack().name} deg og gjorde {enemy1.velg_attack().perform_attack()} skade.")
print(f"{enemy1.name} {enemy1.velg_attack().name} deg og gjorde {enemy1.velg_attack().perform_attack()} skade.")