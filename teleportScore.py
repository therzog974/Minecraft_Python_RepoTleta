from mcpi.minecraft import Minecraft
mc = Minecraft.create()

points = int(input("enter your points"))
if points <= 2:
    mc.player.setPos(0,12,0)
elif points == 23:
    mc.player.setPos(91,6,30)
elif points > 2:
    mc.player.setPos(122, 10, 122)
elif points > 4:
    mc.player.setPos(60, 20, 32)
elif points > 6:
    mc.player.setPos(32, 18, -38)
else:
    mc.postToChat("I don't know what to do with that information. Please put in a number that acctuly exists - weather real or the square root of a negitive number.")
             
