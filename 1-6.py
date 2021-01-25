from mcpi.minecraft import Minecraft
Kiyui = Minecraft.create()


Kiyui.postToChat("I'm watching you~~~")

while True:
    x,y,z = Kiyui.player.getTilePos()
    Kiyui.postToChat("X:"+str(x)+"Y:"+str(y)+"Z:"+str(z))