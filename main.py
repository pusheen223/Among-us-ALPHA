from Maps.Skeld import Color_Skeld
from Maps.MiraHQ import Color_Mira
import time 
import os
clear = lambda: os.system("clear")
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"
print(" Loading Game")
print(bright_blue+"[///         ]"+bright_white)
time.sleep(1)
clear()
print(" Loading Game")
print(bright_blue+"[//////      ]"+bright_white)
time.sleep(0.7)
clear()
print(" Loading Game")
print(bright_blue+"[///////     ]"+bright_white)
time.sleep(1)
clear()
print(" Loading Game")
print(bright_blue+"[//////////  ]"+bright_white)
time.sleep(1.5)
clear()
print(" Loading Game")
print(bright_blue+"[////////////]"+bright_white)
time.sleep(0.3)
clear()
def Start():
	print("Welcome to Among us!")
	input("Click Enter to Start\n-->")
	clear()
	Map()
def Map():
	print("Choose Map:")
	print("1) Skelt")
	print("2) MiraHQ")
	Map_input = str(input("--> "))
	if Map_input=="1":
		clear()
		Color_Skeld()
	elif Map_input=="2":
		clear()
		Color_Mira()
	else:
		clear()
		print("You can only pick number from the list!\n")
while True:
	Start()
	clear()
	print("You did all your tasks")
	print(green+"You won the Game!"+bright_white)
	exit()