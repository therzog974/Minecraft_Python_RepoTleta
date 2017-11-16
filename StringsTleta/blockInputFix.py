from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
try:
    blockType = int(input("Enter a block type:"))
    mc.setBlock(x,y,z,blockType)
except:
    mc.postToChat("You didn't type a number. Ya might want to enter a number the next time around")
    
