from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 90

y = 6

z = 30

blockType = 103

mc.setBlock(x, y, z, blockType)
mc.setBlock(x, y+1, z, blockType)
mc.setBlock(x, y-1, z, blockType)
