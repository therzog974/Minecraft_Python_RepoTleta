from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from time import sleep
flower = 38

while True:
    x,y,z = mc.player.getPos()
    block_beneath = mc.getBlock(x,y,z)
    print(block_beneath)
    
