from mcpi.minecraft import Minecraft
Kiyui = Minecraft.create()
import time

A=0
while True:
    A = A+1
    Kiyui.postToChat("第"+str(A)+"次")
    time.sleep(1)
    