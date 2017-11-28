from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y - 1
z = pos.z
blockType = mc.getBlock(x,y,z)
blockType == 18 or 11
mc.postToChat("The player is in a tree " + str(True or False))
