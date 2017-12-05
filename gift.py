from mcpi.minecraft import Minecraft
mc = Minecraft.create
x = 10
y = 11
z = 12
gift = mc.getBlock(x,y,z)

if gift == 57:
    mc.postToChat("OMG PLZ BRING A GIFT TO " + str(x) + ", " + str(y) + ", " + str(z))
elif gift == 6:
    mc.postToChat("meh. I mean, you can bring it if you want..." + str(x) + ", " + str(y) + ", " + str(z))
else:
    mc.postToChat("Bring a gift to" + str(x) + ", " + str(y) + ", " + str(z))
