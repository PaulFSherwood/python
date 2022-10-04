class Player:
  def __init__(self, name, typed, total, hp, attack, defense, spatk, spdef, speed):
    self.name = name
    self.typed = typed
    self.total = total
    self.hp = hp
    self.attack = attack
    self.defense = defense
    self.spatk = spatk
    self.spdef = spdef
    self.speed = speed
  
  def getName(self):
      return self.name
  def getTyped(self):
      return self.typed
  def getTotal(self):
      return self.total
  def getHP(self):
      return self.hp
  
  def getAttack(self):
      return self.attack
  def getDefense(self):
      return self.defense
  def getSpatk(self):
      return self.spatk
  def getSpdef(self):
      return self.spdef
  def getSpeed(self):
      return self.speed
  
  def setHP(self, dmg):
    self.hp -= dmg
  def attack(self, enemy, dmg):
    enemy.setHP(dmg)
  