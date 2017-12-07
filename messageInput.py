from mcpi.minecraft import Minecraft
mc = Minecraft.create()
message = input("Input your message")
mc.postToChat(message)
