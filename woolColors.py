from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def getWoolState(color):
    """Takes a color as a string and returns the wool block state for that color"""
    if color == "pink":
        blockState = 6
    elif color == "blue":
        blockState = 11
    elif color == "green":
        blockState = 13
    elif color == "brown":
        blockState = 12
    elif color == "orange":
        blockState = 1
    elif color == "white":
        blockState = 0
    elif color == "cyan":
        blockState = 9
    elif color == "purple":
        blockState = 10
    elif color == "gray":
        blockState = 7
    elif color == "yellow":
        blockState = 4
    elif color == "red":
        blockState = 14
    elif color == "magenta":
        blockState = 2
    elif color == "lime":
        blockState = 5
    elif color == "light blue":
        blockState = 3
    elif color == "light gray":
        blockState = 8
    elif color == "black":
        blockState = 15
    else:
        blockState = 15

color = str(input("Enter a block color: "))
blockState = int(getWoolState(color))

pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, 35.0, blockState)
