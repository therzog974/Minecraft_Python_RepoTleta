from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 6
y = 26
z = 50
melon = 103
block = mc.getBlock(x,y,z)
noMelon = not melon
mc.postToChat("you need to get some food: "  + str(noMelon))

