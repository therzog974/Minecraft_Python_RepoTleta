from mcpi.minecraft import Minecraft
mc = Minecraft.create()
diamond = 57
lava = 10
air = 0


x = 110
y = 7
z = 16
gift = mc.getBlock(x,y,z)
if gift == diamond:
    mc.setBlock(x-1,y,z-1,air)
    mc.setBlock(x-1,y-1,z-1,air)
    if mc.player.getTilePos = 
 
else:
    mc.postToChat("place an offering on the pedestal.")
