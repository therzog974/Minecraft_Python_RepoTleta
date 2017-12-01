from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
answer = input("create a crater? y/n")
if answer == "y" or "Y":
    mc.setBlocks(pos.x+1, pos.y+1, pos.z+1,pos.x + 1, pos.y-1, pos.z-1, 0)
    mc.postToChat("Boom") 
elif answer == "n" or "N":
     print("Okay then! ^_^")
else:
     print("...")
 
    
    
    
