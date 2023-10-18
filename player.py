######################
### SPILLER KLASSE ###
######################
import random

class Hero:
    def __init__(self, name, max_health):
        self.name = name
        self.max_health = max_health
        self.health = max_health

        # Definerer angrep og skade
        self.attacks = {
            "slå": (5, 10),         # Damage range: 5 til 10
            "spark": (8, 12),       # Damage range: 8 til 12
            "reflekter angrep": (10, 15)  # Damage range: 10 til 15
        }

    def display_status(self):
        print(f"{self.name}'s helse: {self.health}/{self.max_health}")

    def attack(self, enemy, chosen_attack):
        if chosen_attack not in self.attacks:
            print("Ugyldig angrep. Vennligst velg et gyldig angrep.")
            return

        attack_name = chosen_attack
        damage_range = self.attacks[chosen_attack]
        min_damage, max_damage = damage_range

        damage = random.randint(min_damage, max_damage)
        enemy.receive_damage(damage)
        print(f"{self.name} angriper med {attack_name} og tar {damage} skade på fienden.")

    def receive_damage(self, damage):
        self.health = max(0, self.health - damage)
        if self.health == 0:
            print(f"{self.name} har blitt slått!")


# Puttet koden inn i denne sånn at det ikke kjører på import
if __name__ == "__main__":
    # Example usage
    hero1 = Hero("Harald Helt", 100)
    hero2 = Hero("Evil Villain", 80)

    while hero1.health > 0 and hero2.health > 0:
        print("Gyldige angrep:")
        for attack in hero1.attacks:
            print(attack)

        chosen_attack = input("Velg et angrep: ").lower()
        hero1.attack(hero2, chosen_attack)
        hero2.display_status()

        if hero2.health > 0:
            # Velger et tilfeldig angrep for motstanderen
            enemy_attack = random.choice(list(hero2.attacks.keys()))
            hero2.attack(hero1, enemy_attack)
            hero1.display_status()