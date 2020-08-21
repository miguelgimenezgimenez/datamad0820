import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):

        self.health = self.health - damage


# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return 'Odin Owns You All!'

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"
# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
        
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
        
    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        out = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            index_of_saxon = self.saxonArmy.index(saxon)
            self.saxonArmy.pop(index_of_saxon)
        return out
        
    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        out = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            index_of_viking = self.vikingArmy.index(viking)
            self.vikingArmy.pop(index_of_viking)
        return out
    def showStatus(self):
        vikings= len(self.vikingArmy)
        saxons= len(self.saxonArmy)
        if not vikings:
            return "Saxons have fought for their lives and survive another day..."
        if not saxons:
            return "Vikings have won the war of the century!"
        return "Vikings and Saxons are still in the thick of battle."