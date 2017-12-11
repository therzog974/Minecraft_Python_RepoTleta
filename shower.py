from mcpi.minecraft import Minecraft

mc = Minecraft.create()

shwrX = -60
shwrY = 10
shwrZ = 52

width = 2
height = 2
length = 2

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

if shwrX <= z < shwrX + width and shwr <= y < shwrY + height and shwrZ <= z < shwrZ + length:
    mc.setBlocks(x, x-1, y, z, z+1 , 8)

    
mc.postToChat("Minecraft doesn't have any soap")
