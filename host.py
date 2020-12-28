import os
import time
from os import system
from time import sleep

os.system("cls")

print("This Script Allow You To Create Host For GTPS © Clayne and NumeX")
print('--------------------------------------------------------\n')

host = input("[ + ] Enter Your IP Server: ")
name = input("[ + ] Enter Your Host Name: ")
end = input("[ + ] Enter Your End File (.js, .txt & etc): ")

f = open(f"{name}.{end}", "a+")

f.write(str(host + " growtopia1.com\n" + host + " growtopia2.com"))

f.close()
print('\n--------------------------------------------------------')
print(f"\n[LOGS] Host Successfully Created! ({name}.{end})")

time.sleep(5.0)
exit()
