from mcpi.minecraft import Minecraft
mc = Minecraft.create()
air = 0
water = 8
river = 9
power = False

answer = input("Do you want to have Midas' curse? y/n: ")
if answer == "y":
    power = True
while power == True:
    pos = mc.player.getTilePos()
    blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)
    if blockBelow != water and blockBelow != air:
        mc.setBlock( pos.x, pos.y - 1, pos.z, 41)
    if blockBelow == river:
        power = False

