import time
import os
import random
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
def TaskRand():
	global Tasks
	global Chute
	global Download
	global STask
	global Card
	global Asters
	Tasks = random.randint(1,10)
	if Tasks==1:
		Chute = 0
		Download = 0
		STask = 0
		Card = 100
		Asters = 100

	elif Tasks==2:
		Chute = 100
		Download = 0
		STask = 0
		Card = 0
		Asters = 100	

	elif Tasks==3:
		Chute = 100
		Download = 100
		STask = 0
		Card = 0
		Asters = 0

	elif Tasks==4:
		Chute = 0
		Download = 100
		STask = 100
		Card = 0
		Asters = 0	

	elif Tasks==5:
		Chute = 0
		Download = 0
		STask = 100
		Card = 100
		Asters = 0

	elif Tasks==6:
		Chute = 0
		Download = 0
		STask = 0
		Card = 100
		Asters = 100	

	elif Tasks==7:
		Chute = 0
		Download = 0
		STask = 100
		Card = 0
		Asters = 100	

	elif Tasks==8:
		
		Chute = 0
		Download = 100
		STask = 0
		Card = 100
		Asters = 0

	elif Tasks==9:
		Chute = 0
		Download = 100
		STask = 0
		Card = 0
		Asters = 100

	elif Tasks==10:
		Chute = 100
		Download = 0
		STask = 100
		Card = 0
		Asters = 0	
	else:
		print(red+"an error Included")
		exit()		
def Color_Skeld():
	TaskRand()
	print('Choose Color:')
	print(bright_white+"1)"+black+" Black")
	print(bright_white+"2)"+bright_white+" White")
	print(bright_white+"3)"+bright_yellow+" Yellow")
	print(bright_white+"4)"+blue+" Blue")
	print(bright_white+"5)"+red+" Red")
	print(bright_white+"6)"+bright_magenta+" Purple")
	print(bright_white+"7)"+yellow+" Orange"+bright_white)
	pl = str(input("-->"))
	if pl=="1":
		clear()
		global Player_Color
		Player_Color = black+"Black"+bright_white
		Cafeteria()
	elif pl=="2":
		clear()
		Player_Color = bright_white+"White"
		Cafeteria()
	elif pl=="3":
		clear()
		Player_Color = bright_yellow+"Yellow"+bright_white
		Cafeteria()
	elif pl=="4":
		clear()
		Player_Color = blue+"Blue"+bright_white
		Cafeteria()
	elif pl=="5":
		clear()
		Player_Color = red+"Red"+bright_white
		Cafeteria()
	elif pl=="6":
		clear()
		Player_Color = bright_magenta+"Purple"+bright_white
		Cafeteria()
	elif pl=="7":
		clear()
		Player_Color = yellow+"Orange"+bright_white
		Cafeteria()
	else:
		clear()
		print("you can pick a number from the list!")
		Color_Skeld()
def Info():
	Win_Checker()
	print("Map: Skeld")
	print("You are the"+cyan+" Crewmate"+bright_white)
	print("Your color is",Player_Color)
	print("Tasks:")
	Tasks_Check()
	print("\n")

time.sleep(0)
def Cafeteria():
	Info()
	print(bright_blue+"Cafeteria"+bright_white)
	print("1) Go to Medbay")
	print("2) Go to Upper Engine")
	print("3) Go to Storage")
	print("4) Go to Admin")
	print("5) Go to Weapons")
	Cafe_Check()
	Move = str(input("-->"))
	if Move=="1":
		clear()
		Medbay()
	elif Move=="2":
		clear()
		Upper_Engine()
	elif Move=="3":
		clear()
		Storage()
	elif Move=="4":
		clear()
		Admin()
	elif Move=="5":
		clear()
		Weapons()
	elif Move=="6":
		if Chute==0:
			clear()
			Cafe_Chute()
		else:
			clear()
			print("You can pick a number from the list!\n")
			Cafeteria()
	else:
		clear()
		print("You can pick a number from the list!\n")
		Cafeteria()

def Admin():
	Info()
	print(bright_blue+"Admin"+bright_white)
	print("1) Go to Cafeteria")
	print("2) Go to Storage")
	Admin_Check()
	Move = str(input("-->"))
	if Move=="1":
		clear()
		Cafeteria()
	elif Move=="2":
		clear()
		Storage()
	elif Move=="3":
		if Download==1:
			clear()
			Download_Admin()
		else:
			clear()
			print("you can pick a number from the list!\n")
			Admin()
	elif Move=="4":
		if Card==0:
			clear()
			Swipe_Card()
		else:
			clear()
			print("you can pick a number from the list!\n")
			Admin()
	else:
		clear()
		print("you can pick a number from the list!\n")
		Admin()	
	
def Storage():
	Info()
	print(bright_blue+"Storage"+bright_white)
	print("1) Go to Upper_Engine")
	print("2) Go to Electrical")
	print("3) Go to Cafeteria")
	print("4) Go to Admin")
	print("5) Go to Communications")
	print("6) Go to Shields")
	Stor_Check()
	Move = str(input("-->"))
	if Move=="1":
		clear()
		Upper_Engine
	elif Move=="2":
		clear()
		Electrical()
	elif Move=="3":
		clear()
		Cafeteria()
	elif Move=="4":
		clear()
		Admin()
	elif Move=="5":
		clear()
		Communications()
	elif Move=="6":
		clear()
		Shields()
	elif Move=="7":
		if Chute==1:
			clear()
			Stor_Chute()
		else:
			clear()
			print("You can pick a number from the list!\n")
			Storage()
	else:
		clear()
		print("You can pick a number from the list!\n")
		Storage()
def Weapons():
	Info()
	print(bright_blue+"Weapons"+bright_white)
	print("1) Go to Cafeteria")
	print("2) Go to O2")
	print("3) Go to Navigation")
	print("4) Go to Shields")
	Weapons_Check()
	Move = str(input("-->"))
	if Move =="1":
		clear()
		Cafeteria()
	elif Move=="2":
		clear()
		O2()
	elif Move=="3":
		clear()
		Navigation()
	elif Move=="4":
		clear()
		Shields()
	elif Move=="5":
		clear()
		Asteroids()
	else:
		clear()
		print("you can pick a number from the list!")
		Weapons()
def Electrical():
	Info()
	print(bright_blue+"Electrical"+bright_white)
	print("1) Go to Storage")
	print("2) Go to Lower Engine")
	Elec_Check()
	Move = str(input("-->"))
	if Move=="1":
		clear()
		Storage()
	elif Move=="2":
		clear()
		Lower_Engine()
	elif Move=="3":
		if Download == 0:
			Download_Elec()
		else:
			clear()
			print("you can pick a number from the list!")
			Electrical()
	else:
		clear()
		print("you can pick a number from the list!")
		Electrical()
def Lower_Engine():
	Info()
	print(bright_blue+"Lower Engine"+bright_white)
	print("1) Go to Upper Engine")
	print("2) Go to Reactor")
	print("3) Go to Secruity")
	print("4) Go to Electrical")
	print("5) Go to Storage")
	Move = str(input("-->"))
	if Move =="1":
		clear()
		Upper_Engine()
	elif Move =="2":
		clear()
		Reactor()
	elif Move=="3":
		clear()
		Secruity()
	elif Move=="4":
		clear()
		Electrical()
	elif Move=="5":
		clear()
		Storage()
	else:
		clear()
		print("you can pick a number from the list!")
		Lower_Engine()
def Reactor():
	Info()
	print(bright_blue+"Reactor"+bright_white)
	print("1) Go to Upper Engine")
	print("2) Go to Secruity")
	print("3) Go to Lower Engine")
	Move = str(input("-->"))
	if Move =="1":
		clear()
		Upper_Engine()
	elif Move == "2":
		clear()
		Secruity()
	elif Move =="3":
		clear()
		Lower_Engine()
	else:
		clear()
		print("you can pick a number from the list!")
		Reactor()
def Secruity():
	Info()
	print(bright_blue+"Secruity"+bright_white)
	print("1) Go to Upper Engine")
	print("2) Go to Reactor")
	print("3) Go to Lower Engine")
	Move = str(input("-->"))
	if Move =="1":
		clear()
		Upper_Engine()
	elif Move == "2":
		clear()
		Reactor()
	elif Move =="3":
		clear()
		Lower_Engine()
	else:
		clear()
		print("you can pick a number from the list!")
		Secruity()

def Medbay():
	Info()
	print(bright_blue+"Medbay"+bright_white)
	print("1) Go to Upper Engine")
	print("2) Go to Cafeteria")
	Move = str(input("-->"))
	if Move =="1":
		clear()
		Upper_Engine()
	elif Move=="2":
		clear()
		Cafeteria()
	else:
		clear()
		print("you can pick a number from the list!")
		Medbay()


def O2():
	Info()
	print(bright_blue+"O2"+bright_white)
	print("1) Go to Weapons")
	print("2) Go to Navigation")
	print("3) Go to Shields")
	Move = str(input("-->"))
	if Move=="1":
		clear()
		Weapons()
	elif Move=="2":
		clear()
		Navigation()
	elif Move=="3":
		clear()
		Shields()
	else:
		clear()
		print("you can pick number from the list!")
		O2()

def Communications():
	Info()
	print(bright_blue+"Communications"+bright_white)
	print("1) Go to Storage")
	print("2) Go to Shields")
	Move = str(input("-->"))
	if Move=="1":
		clear()
		Storage()
	elif Move=="2":
		clear()
		Storage()
	else:
		clear()
		print("you can pick a number from the list!")
		Communications()

def Navigation():
	Info()
	print(bright_blue+"Navigation"+bright_white)
	print("1) Go to Weapons")
	print("2) Go to O2")
	print("3) Go to Shields")
	Move = str(input("-->"))
	if Move=="1":
		clear()
		Weapons()
	elif Move=="2":
		clear()
		O2()
	elif Move=="3":
		clear()
		Shields()
	else:
		clear()
		print("you can pick a number from the list")

def Shields():
	Info()
	print(bright_blue+"Shields"+bright_white)
	print("1) Go to Storage")
	print("2) Go to Communications")
	print("3) Go to Weapons")
	print("4) Go to O2")
	print("5) Go to Navigation")
	ShCheck()
	Move = str(input("-->"))
	if Move=="1":
		clear()
		Storage()
	elif Move=="2":
		clear()
		Communications()
	elif Move=="3":
		clear()
		Weapons()
	elif Move=="4":
		clear()
		O2()
	elif Move=="5":
		clear()
		Navigation()
	elif Move=="6":
		if STask==0:
			clear()
			Shields_Task()
		else:
			clear()
			print("you can pick a number from the list!")
			Shields()
	else:
		clear()
		print("you can pick a number from the list!")
		Shields()
def Upper_Engine():
	Info()
	print(bright_blue+"Upper Engine"+bright_white)
	print("1) Go to Reactor")
	print("2) Go to Secruity")
	print("3) Go to Lower Engine")
	print("4) Go to Medbay")
	print("5) Go to Cafeteria")
	Move = str(input("-->"))
	if Move=="1":
		clear()
		Reactor()
	elif Move=="2":
		clear()
		Secruity()
	elif Move=="3":
		clear()
		Lower_Engine
	elif Move=="4":
		clear()
		Medbay()
	elif Move=="5":
		clear()
		Cafeteria()
	else:
		clear()
		print("you can pick a number from the list!")
		Upper_Engine()


def Cafe_Chute():
	print("Type (Chute) and wait to do a task\nor (back) to back")
	cd = str(input("-->"))
	if cd=="Chute".lower():
		clear()
		time.sleep(1)
		global Chute
		Chute = 1
		Cafeteria()
	elif cd=="back".lower():
		clear()
		Cafeteria()
	else:
		clear()
		print("Fail!")
		Cafe_Chute()
def Stor_Chute():
	print("Type (Chute) and wait to do a task\nor (back) to back")
	cd = str(input("-->"))
	if cd=="Chute".lower():
		clear()
		time.sleep(1)
		print("Task Completed!")
		global Chute
		Chute = 2
		Cafeteria()
	elif cd=="back".lower():
		clear()
		Storage()
	else:
		clear()
		print("Fail!")
		Stor_Chute()
def Download_Elec():
	clear()
	print("Type (File) and wait to Dowload Data")
	print("or (back) to back")
	de = str(input("-->"))
	if de=="File".lower():
		clear()
		print("Downloading progress:")
		print("  |////           |")
		time.sleep(1)
		clear()
		print("Downloading progress:")
		print("  |////////       |")
		time.sleep(1)
		clear()
		print("Downloading progress:")
		print("  |/////////////  |")
		time.sleep(1)
		clear()
		print("Downloading progress:")
		print("  |///////////////|")
		time.sleep(0.5)
		clear()
		global Download
		Download = 1
		Electrical()
	elif de=="back".lower():
		clear()
		Electrical()
	else:
		clear()
		print("Fail!")
		Download_Elec()	
def Download_Admin():
	clear()
	print("Type (Files) and wait to Upload Data")
	print("or (back) to back")
	da = str(input("-->"))
	if da=="Files".lower():
		clear()
		print("Uploading progress:")
		print("  |////           |")
		time.sleep(1)
		clear()
		print("Uploading progress:")
		print("  |////////       |")
		time.sleep(1)
		clear()
		print("Uploading progress:")
		print("  |/////////////  |")
		time.sleep(1)
		clear()
		print("Uploading progress:")
		print("  |///////////////|")
		time.sleep(0.5)
		clear()
		print("Task Completed!")
		global Download
		Download = 2
		Admin()
	elif da=="back".lower():
		clear()
		Admin()
	else:
		clear()
		print("Fail!")
		Download_Admin()
def Shields_Task():
	print("Type (342) to Do a Prime Shields")
	print("or (back) to back")
	kk = str(input("-->"))
	if kk=="342":
		clear()
		print("3")
		time.sleep(0.5)
		clear()
		print("3 4")
		time.sleep(0.5)
		clear()
		print("3 4 2")
		time.sleep(0.5)
		clear()
		global STask
		STask = 1
		print("Task Completed!")
		Shields()
	elif kk=="back".lower():
		clear()
		Shields()
	else:
		clear()
		print("Fail!")
		Shields_Task()
def Swipe_Card():
	print("Type (Swipe) To Swipe the card")
	print("or (back) to back")
	oo = str(input("-->"))
	if oo=="Swipe".lower():
		Swipe_Troll = random.randint(1,3)
		if Swipe_Troll==1:
			global Card
			Card = 1
			clear()
			print("Connectinng to server...")
			time.sleep(1)
			clear()
			print(green+"Card Accepted"+bright_white)
			time.sleep(1.5)
			clear()
			print("Task Completed!")
			Admin()
		elif Swipe_Troll==2:
			print("Connectinng to server...")
			time.sleep(1.5)
			print(red+"Bad Read! Try again"+bright_white)
			time.sleep(2)
			clear()
			Swipe_Card()
		else:
			print("Connectinng to server...")
			print(red+"Bad Read! Try again"+bright_white)
			time.sleep(2)
			clear()
			Swipe_Card()
	elif oo=="back".lower():
		clear()
		Admin()
	else:
		clear()
		print("Fail")
		Swipe_Card()
def Asteroids():
	global Asters
	if Asters==0:
		print("(0/3)")
		print("Type (pew) to shoot Asteroid")
		print("or (back) to back")
		print("\n O   O   O\n")
		po = str(input("-->"))
		if po=="pew".lower():
			Asters = 1
			clear()
			Asteroids()
		elif po=="back".lower():
			clear()
			Weapons()
		else:
			clear()
			print("Fail!")
			Asteroids()
	elif Asters==1:
		print("(1/3)")
		print("Type (pew) to shoot Asteroid")
		print("or (back) to back")
		print("\n     O   O\n")
		po = str(input("-->"))
		if po=="pew".lower():
			Asters = 2
			clear()
			Asteroids()
		elif po=="back".lower():
			clear()
			Weapons()
		else:
			clear()
			print("Fail!")
			Asteroids()
	elif Asters==2:
		print("(2/3)")
		print("Type (pew) to shoot Asteroid")
		print("or (back) to back")
		print("\n         O\n")
		po = str(input("-->"))
		if po=="pew".lower():
			Asters = 3
			clear()
			Asteroids()
		elif po=="back".lower():
			clear()
			Weapons()
		else:
			clear()
			print("Fail!")
			Asteroids()
	elif Asters==3:
		clear()
		print("Task Completed!")
		Weapons()
	elif Asters==100:
		clear()
		print("you can pick a number from the list!\n")
		Weapons()


def Admin_Check():
	if Download==1:
		print("3) Upload Data Task")
	if Card==0:
		print("4) Swipe Card Task")
def Cafe_Check():
	if Chute==0:
		print("6) Do Chute Task")
def Stor_Check():
	if Chute==1:
		print("7) Do Chute Task")
def Weapons_Check():
	if Asters==0 or Asters==1 or Asters==2:
		print("5) Clear Asteroids Task")
def Elec_Check():
	if Download==0:
		print("3) Download Data Task")
def ShCheck():
	if STask==0:
		print("6) Prime Shields Task")


def Tasks_Check():
	if Chute==0:
		print(white+"Cafeteria : Chute : (0/2)"+bright_white)
	elif Chute==1:
		print(bright_yellow+"Storage : Chute : (1/2)"+bright_white)
	elif Chute==2:
		print(green+"Chute : (2/2)"+bright_white)
	if Download==0:
		print(white+"Electrical : Upload Data : (0/2)"+bright_white)
	elif Download==1:
		print(bright_yellow+"Admin : Upload Data : (1/2)"+bright_white)
	elif Download==2:
		print(green+"Upload Data : (2/2)"+bright_white)
	if STask==0:
		print(white+"Shields : Prime Shields"+bright_white)
	elif STask==1:
		print(green+"Prime Shields"+bright_white)
	if Card==0:
		print(white+"Admin : Swipe Card"+bright_white)
	elif Card==1:
		print(green+"Swipe Card"+bright_white)
	if Asters==0:
		print(white+"Weapons : Clear Asteroids (0/3)"+bright_white)
	elif Asters==1:
		print(bright_yellow+"Weapons : Clear Asteroids (1/3)"+bright_white)
	elif Asters==2:
		print(bright_yellow+"Weapons : Clear Asteroids (2/3)"+bright_white)
	elif Asters==3:
		print(green+"Clear Asteroids (3/3)"+bright_white)
def Win_Checker():
	if Tasks==1:
		if Chute==2 and Download==2 and STask==1:
			print("You did all your Tasks!")
			print(green+"You won the game!"+bright_white)
			exit()

	elif Tasks==2:
		if Download==2 and STask==1 and Card==1:
			print("You did all your Tasks!")
			print(green+"You won the game!"+bright_white)
			exit()
	elif Tasks==3:
		if STask==1 and Card==1 and Asters==3:
			print("You did all your Tasks!")
			print(green+"You won the game!"+bright_white)
			exit() 

	elif Tasks==4:
		if Chute==2 and Card==1 and Asters==3:
			print("You did all your Tasks!")
			print(green+"You won the game!"+bright_white)
			exit()

	elif Tasks==5:
		if Chute==2 and Download==2 and Asters==3:
			print("You did all your Tasks!")
			print(green+"You won the game!"+bright_white)
			exit() 

	elif Tasks==6:
		if Chute==2 and Download==2 and STask==1:
			print("You did all your Tasks!")
			print(green+"You won the game!"+bright_white)
			exit()

	elif Tasks==7:
		if Chute==2 and Download==2 and Card==1:
			print("You did all your Tasks!")
			print(green+"You won the game!"+bright_white)
			exit()
	elif Tasks==8:
		if Chute==2 and STask==1 and Asters==3:
			print("You did all your Tasks!")
			print(green+"You won the game!"+bright_white)
			exit()

	elif Tasks==9:
		if Chute==2 and STask==1 and Card==1:
			print("You did all your Tasks!")
			print(green+"You won the game!"+bright_white)
			exit()
	elif Tasks==10:
		if Download==2 and Card==1 and Asters==3:
			print("You did all your Tasks!")
			print(green+"You won the game!"+bright_white)
			exit()