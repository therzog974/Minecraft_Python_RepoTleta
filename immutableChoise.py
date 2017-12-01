from mcpi.minecraft import Minecraft
mc = Minecraft.create()



answer = input("Do you want blocks to be immutable?")
if answer == "Y":
    mc.setting("world_immutable", True)
    mc.postToChat("The world is immutable")
elif answer == "N":
    mc.setting("world_immutable", False)
    mc.postToChat("The world isn't immutable")
else:
    mc.postToChat("Please input Y or N. Or go play Skyrim. It's a better game")
