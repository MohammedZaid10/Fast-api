from Zombie import *
from Ogre import *

# big_zombie = Enemy("Big Zombie", 100, 10)
# print(big_zombie.health_points)
# print(big_zombie.attack())

zombie = Zombie(10, 1)
ogre = Ogre(20, 3)

zombie.spread_disease()
ogre.talk()
