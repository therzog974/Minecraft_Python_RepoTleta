from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
print("Wave your flow'r, wave your flow'r, it's a flower - waving parade - o! To the enchanting world c'mon let's go! Join your hands, your hands make a cirle, spin and it's the world, with my lovely flowers I'm in the best condition! ")
while True:
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y, pos.z, 38)
    time.sleep(0.2)
 
