from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

score = 0
pos = mc.player.getPos()
x = pos.x
y = pos.y + 2
z = pos.z
newPos = x and y and z
blockAbove = mc.getBlock()
while blockAbove == 8 or blockAbove == 9:
    time.sleep(1)
    pos = mc.player.getPos(newPos)
    blockAbove = mc.player.getPos(pos.x, pos.y + 2, pos.z)
    score += 1
    mc.postToChat("Curent score: " + str(score))
mc.postToChat("final score:" + str(score))
if score > 6:
 lastPos = mc.player.getTilePos()
mc.setBlocks(lastPos.x - 5, lastPos.y + 10, lastPos.z - 5, lastPos.x + 5, lastPos.y + 10, lastPos.z + 5, 38)
