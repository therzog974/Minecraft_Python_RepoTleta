from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.postToChat ("Hello!")
pos = mc.player.getPos()
x,y,z=mc.player.getPos()


x, y, z = mc.player.getPos()
mc.setBlock(x, y+4, z, 2)
mc.setBlock(x, y+5, z, 2)
mc.setBlock(x, y+6, z, 2)
mc.setBlock(x, y+7, z, 2)
mc.setBlock(x, y+8, z, 2)
from mcpi import block
mc.setBlock(x+3,y,z, block.STONE.id)

dirt = 3
mc.setBlock(x,y,z, dirt)

grass = 2

wool = 35
mc.setBlock(x,y,z, wool, 1)
stone=1
x,y,z=mc.player.getPos()
mc.setBlocks(x+1,y+1,z+1,x+11,y+11,z+11,stone)

from time import sleep
flower = 38

while True:
    x,y,z = mc.player.getPos()
    block_beneath = mc.getBlock(x,y,z)

if block_beneath == grass:
    mc.setBlock(x,y,z, flower)
else
    mc.setBlock(x,y-1,z, grass)
