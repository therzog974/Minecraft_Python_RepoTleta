from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import math
import time
import random
X = random.randint(-127, 127)
Z = random.randint(-127, 127)
Y = mc.getHeight(X, Z)
block = 57
mc.setBlock(X, Y, Z, block)
mc.postToChat("Block set")
time.sleep(5)
while True:
    pos = mc.player.getPos()
    distance = math.sqrt((pos.x - X) ** 2 + (pos.z - Z) ** 2)
    if distance > 100:
        mc.postToChat("Freezing")
    elif distance > 50:
        mc.postToChat("Cold")
    elif distance > 25:
        mc.postToChat("Warm")
    elif distance > 12:
        mc.postSToChat("Boiling")
    elif distance > 6:
        mc.postToChat("On Fire")
    elif distance <= 1 and distance >= 0:
       
        break
mc.postToChat("Ya found it. Have a cookie, I guess.")
