from turtle import pos


class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    # methods
    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')

class Shark(Monster):
    def __init__(self, speed, health, energy):
        # Monster.__init__(self, health, energy)
        super().__init__(health, energy)
        self.speed = speed

    def bite(self):
        print('The shark as bitten')

    def move(self):
        print('The shark has moved')
        print(f'The speed of the shark is {self.speed}')
class Scorpion(Monster):
    def __init__(self, poison_damage, s_health, s_energy):
        super().__init__(health = s_health, energy = s_energy)
        self.poison_damage = poison_damage
    def attack(self, amount):
        print('The Scorpion has attacked!')
        print(f'{self.poison_damage} damage was dealt')
        self.energy -= 20

class Fish:
    def __init__(self, speed, has_scales):
        self.speed = speed
        self.has_scales = has_scales

    def swim(self):
        print(f'The fish is swimming at a speed of {self.speed}')

shark = Shark(speed = 120, health = 100, energy = 80)
# print(shark.speed)

scorpion = Scorpion(poison_damage = 50, s_health = 20, s_energy = 10)
# sc = Scorpion(poison_damage=5, s_health= 22, s_energy=33)
# print(scorpion.health)
# print(scorpion.energy)

