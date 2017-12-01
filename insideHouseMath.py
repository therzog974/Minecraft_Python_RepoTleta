from mcpi.minecraft import Minecraft
mc = Minecraft.create()

buildX = -72
buildY = 10
buildZ = 51
width = 10
height = 5
length = 6

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

inside = (-72 < -69 < buildX + width) and (buildY <= y <= buildY + height) and (buildZ <= z <= buildZ + length)

print(inside)


-69, 10, 51
