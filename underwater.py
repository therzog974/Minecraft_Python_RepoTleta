from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
blockType = mc.getBlock(x,y,z)
mc.postToChat(blockType == 0)
blockType2 = mc.getBlock(x,y+1,z)
if blockType2 == 9 and blockType == 9:
    mc.postToChat("The Player is Underwater: True/False")
