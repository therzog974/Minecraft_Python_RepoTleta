from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time
def melon():
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlock(x, y - 1, z, 103)
    time.sleep(10)

melon()
melon()
melon()
melon()
melon()
melon()
