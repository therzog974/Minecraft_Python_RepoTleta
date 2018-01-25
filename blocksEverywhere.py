from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

def randomBlockLocations(blockType, repeates):
    count = 0
    while count < 10:
        x = random.randint(-127,127)
        z = random.randint(-127,127)
        y = mc.getHeight(x ,z)
        mc.setBlock(x,y,z, blockType)
        count += 1
    while count < 35:
        x = random.randint(-127,127)
        z = random.randint(-127,127)
        y = mc.getHeight(x ,z)
        mc.setBlock(x,y,z, blockType)
        count += 1
    while count < 102:
        x = random.randint(-127,127)
        z = random.randint(-127,127)
        y = mc.getHeight(x ,z)
        mc.setBlock(x,y,z, blockType)
        count += 1
