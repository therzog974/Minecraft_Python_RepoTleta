from mcpi.minecraft import Minecraft
mc = Minecraft.create()
username = input("please enter username:")
message = input("Enter Your message")
mc.postToChat(username + ":" + message)
