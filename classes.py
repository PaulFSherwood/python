class Hero(object):
    '''
    A hero who is allergic to apples
    '''
    def __init__(self, name):
        self.name = name
        self.health = 100

    def eat(self, food):
        if(food == 'apple'):
            self.health -= 100
        elif(food == 'ham'):
            self.health += 20

class Enemy(object):
    life = 3

    def attack(self):
        print("ouch")
        self.life -= 1

    def checkLife(self):
        print("life: %s" % (self.life))
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + " life left")

class Tuna:
    def __init__(self):
        print("blrrblrblrblr")
    def swim(self):
        print("I am swimming")

Bob = Hero("Bob")
Bob.eat('ham')
print(Bob.health)

enemy1 = Enemy()
enemy1.attack()
enemy1.checkLife()

flipper = Tuna()
