from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x = 13.6
y = 6.0
z = 103.9

mc.player.setTilePos(x, y, z)

time.sleep(10)

x = -70.2
y = 2.0
z = -14.6

mc.player.setTilePos(x, y, z)

time.sleep(10)

x = 13.6
y = 6.0
z = 103.9

