from mcpi.minecraft import Minecraft
from time import sleep 

mc = Minecraft.create()

x,y,z = mc.player.getPos()


lava = 10
water = 8
air = 0


mc.setBlock(x+3,y+3,z-10,lava)
sleep(20)
mc.setBlock(x+3,y+5,z-10, water)
sleep(4)
mc.setBlock(x+3,y+5,z-10, air) #end of first tower
sleep(4)
mc.setBlock(x+3,y+3,z,lava)
sleep(20)
mc.setBlock(x+3,y+5,z, water)
sleep(4)
mc.setBlock(x+3,y+5,z, air)# end of second towe r
sleep(4)
mc.setBlock(x-3,y+3,z+10,lava)
sleep(20)
mc.setBlock(x-3,y+5,z+10, water)
sleep(4)
mc.setBlock(x-3,y+5,z+10, air)#end of third tower
sleep(4)
mc.setBlock(x-3,y+3,z,lava)
sleep(20)
mc.setBlock(x-3,y+5,z, water)
sleep(4)
mc.setBlock(x-3,y+5,z, air)#end of fourth tower

