from mcpi.minecraft import Minecraft
mc = Minecraft()
import time
pos = mc.player.getTilePos
def calculateMove():
    """changes the x and z variables for a block. If the block in front of the block is less than 2 blocks higher, it will move forward; otherwise it will try to move left, than backward, then finally right. """
    x = pos.x
    y = pos.y
    z = pos.z

    currentHeight = mc.getHeight(x,z,) - 1

    forwardHeight = mc.getHight(x + 1, z)
    rightHeight = mc.getHeight(x, z + 1)
    backwardHeight = mc.getHeight(s, z + 1)
    leftHeight = mc.getHeight(x, z- 1)
    if forwardHeight - currentHeight < 3:
        x += 1
    elif rightHeight - currentHeight < 3:
        z += 1
    elif leftHeight - currentHeight < 3:
        z -= 1
    elif backwardHeight - currentHeight < 3:
        x -= 1
    y = mc.getHeight(x, z)
while True:
    calculateMove()
    mc.setBlock(x,y,z,103)
    time.sleep(1)
    mc.setBlock(x,y,z,0)
        
    
