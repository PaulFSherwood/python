class Display:
  def __init__(self):
    pass
    
  def showThing(self, entity):
    print(f"/------------------------------------\\")
    print(f"| Name: {entity.getName()[:10] :<10}{' ':^5s} HP: {entity.getHP() : <6}{ ' |':>4}")
    print(f"| Atk: {entity.getAttack() :<10}{' ':^6s} Def: {entity.getDefense() : <5}{ ' |':>4}")
    print(f"| Speed: {entity.getSpeed() :<10}{' ':^4s} Total: {entity.getTotal() : <3}{ ' |':>4}")
    print(f"| Sp.Atk: {entity.getSpatk() :<10}{' ':^3s} Sp.Def: {entity.getSpdef() : <3}{ ' |':>3}")
    print(f"\\------------------------------------/")


'''


entity.getName() ###
entity.getTyped() ###
entity.getTotal()
entity.getHP() ###
  
entity.getAttack() ###
entity.getDefense() ###
entity.getSpatk()
entity.getSpdef()
entity.getSpeed()


'''