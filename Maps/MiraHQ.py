import os, time, random
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
def Task_Rand():
	global Tasks
	global Plants
	global Code
	global Scan
	global Says
	global Vend
	Tasks = random.randint(1,10)
	if Tasks==1:
		Plants = 100
		Code = 100
		Scan = 0
		Says = 0
		Vend = 0

	elif Tasks==2:
		Plants = 0
		Code = 100	
		Scan = 100
		Says = 0
		Vend = 0

	elif Tasks==3:
		Plants = 0
		Code = 0	
		Scan = 100
		Says = 100
		Vend = 0

	elif Tasks==4:
		Plants = 0
		Code = 0	
		Scan = 0
		Says = 100
		Vend = 100

	elif Tasks==5:
		Plants = 100
		Code = 0	
		Scan = 0
		Says = 0
		Vend = 100

	elif Tasks==6:
		Plants = 0
		Code = 0	
		Scan = 100
		Says = 0
		Vend = 100

	elif Tasks==7:
		Plants = 100
		Code = 0	
		Scan = 100
		Says = 0
		Vend = 0

	elif Tasks==8:
		Plants = 0
		Code = 100	
		Scan = 0
		Says = 0
		Vend = 100
	elif Tasks==9:
		Plants = 100
		Code = 0	
		Scan = 0
		Says = 100
		Vend = 0
	elif Tasks==10:
		Plants = 0
		Code = 100	
		Scan = 0
		Says = 100
		Vend = 0

	else:
		clear()
		print(bright_red+"An Error included"+bright_white)
		exit()
def Color_Mira():
	Task_Rand()
	print("Choose a Color:")
	print("1)"+black+" Black"+white)
	print("2)"+bright_white+" White"+white)
	print("3)"+bright_yellow+" Yellow"+white)
	print("4)"+blue+" Blue"+white)
	print("5)"+bright_red+" Red"+white)
	print("6)"+magenta+" Purple"+white)
	print("7)"+yellow+" Orange"+white)
	pl = str(input("-->"))
	if pl=="1":
		clear()
		global Player_Color
		Player_Color = black+"Black"+bright_white
		Launchpad()
	elif pl=="2":
		clear()
		Player_Color = "White"+bright_white
		Launchpad()
	elif pl=="3":
		clear()
		Player_Color = bright_yellow+"Yellow"+bright_white
		Launchpad()
	elif pl=="4":
		clear()
		Player_Color = blue+"Blue"+bright_white
		Launchpad()
	elif pl=="5":
		clear()
		Player_Color = bright_red+"Red"+bright_white
		Launchpad()
	elif pl=="6":
		clear()
		Player_Color = magenta+"Purple"+bright_white
		Launchpad()
	elif pl=="7":
		clear()
		Player_Color = yellow+"Orange"+bright_white
		Launchpad()
	else:
		clear()
		print("you can pick a number from the list!")
		Color_Mira()
def Info():
	Win_Checker()
	print("Map: MiraHQ")
	print("you are"+cyan+" Crewmate"+bright_white)
	print("your color is",Player_Color)
	print("Tasks:"+white)
	Task_Checker()
	print("\n")

def Launchpad():
	Info()
	print(bright_blue+"Launchpad"+bright_white)
	print("1) Go to Medbay")
	print("2) Go to Communications")
	print("3) Go to Locker Room")
	print("4) Go to Office")
	print("5) Go to GreenHouse")
	print("6) Go to Admin")
	print("7) Go to Cafeteria")
	ll = str(input("-->"))
	if ll=="1":
		clear()
		Medbay()
	elif ll=="2":
		Comms()
		clear()
	elif ll=="3":
		clear()
		Locker_Room()
	elif ll=="4":
		clear()
		Office()
	elif ll=="5":
		clear()
		GreenHouse()
	elif ll=="6":
		clear()
		Admin()
	elif ll=="7":
		clear()
		Cafeteria()
	else:
		clear()
		print("You can pick a number from the list!")
		Launchpad()
def Medbay():
	Info()
	print(bright_blue+"Medbay"+bright_white)
	print("1) Go to Launchpad")
	print("2) Go to Communications")
	print("3) Go to Locker Room")
	print("4) Go to Office")
	print("5) Go to GreenHouse")
	print("6) Go to Admin")
	print("7) Go to Cafeteria")
	Med_Check()
	ll = str(input("-->"))
	if ll=="1":
		clear()
		Launchpad()
	elif ll=="2":
		clear()
		Comms()
	elif ll=="3":
		clear()
		Locker_Room()
	elif ll=="4":
		clear()
		Office()
	elif ll=="5":
		clear()
		GreenHouse()
	elif ll=="6":
		clear()
		Admin()
	elif ll=="7":
		clear()
		Cafeteria()
	elif ll=="8":
		if Scan==0:
			clear()
			Sumbit_Scan()
		else:
			clear()
			print("You can pick a number from the list!")
			Reactor()
	else:
		clear()
		print("You can pick a number from the list!")
		Medbay()
def Comms():
	Info()
	print(bright_blue+"Comms"+bright_white)
	print("1) Go to Launchpad")
	print("2) Go to Medbay")
	print("3) Go to Locker Room")
	print("4) Go to Office")
	print("5) Go to GreenHouse")
	print("6) Go to Admin")
	print("7) Go to Cafeteria")
	ll = str(input("-->"))
	if ll=="1":
		clear()
		Launchpad()
	elif ll=="2":
		clear()
		Medbay()
	elif ll=="3":
		clear()
		Locker_Room()
	elif ll=="4":
		clear()
		Office()
	elif ll=="5":
		clear()
		GreenHouse()
	elif ll=="6":
		clear()
		Admin()
	elif ll=="7":
		clear()
		Cafeteria()
	else:
		clear()
		print("You can pick a number from the list!")
		Comms()
def Locker_Room():
	Info()
	print(bright_blue+"Locker Room"+bright_white)
	print("1) Go to Launchpad")
	print("2) Go to Medbay")
	print("3) Go to Communications")
	print("4) Go to Office")
	print("5) Go to GreenHouse")
	print("6) Go to Admin")
	print("7) Go to Cafeteria")
	print("8) Go to Decontamination")
	ll = str(input("-->"))
	if ll=="1":
		clear()
		Launchpad()
	elif ll=="2":
		clear()
		Medbay()
	elif ll=="3":
		clear()
		Comms()
	elif ll=="4":
		clear()
		Office()
	elif ll=="5":
		clear()
		GreenHouse()
	elif ll=="6":
		clear()
		Admin()
	elif ll=="7":
		clear()
		Cafeteria()
	elif ll=="8":
		clear()
		Dec()
	else:
		clear()
		print("You can pick a number from the list!")
		Locker_Room()
def Office():
	Info()
	print(bright_blue+"Office"+bright_white)
	print("1) Go to Launchpad")
	print("2) Go to Medbay")
	print("3) Go to Locker Room")
	print("4) Go to Communications")
	print("5) Go to GreenHouse")
	print("6) Go to Admin")
	print("7) Go to Cafeteria")
	ll = str(input("-->"))
	if ll=="1":
		clear()
		Launchpad()
	elif ll=="2":
		clear()
		Medbay()
	elif ll=="3":
		clear()
		Locker_Room()
	elif ll=="4":
		clear()
		Comms()
	elif ll=="5":
		clear()
		GreenHouse()
	elif ll=="6":
		clear()
		Admin()
	elif ll=="7":
		clear()
		Cafeteria()
	else:
		clear()
		print("You can pick a number from the list!")
		Office()
def GreenHouse():
	Info()
	print(bright_blue+"GreenHouse"+bright_white)
	print("1) Go to Launchpad")
	print("2) Go to Medbay")
	print("3) Go to Locker Room")
	print("4) Go to Communications")
	print("5) Go to Office")
	print("6) Go to Admin")
	print("7) Go to Cafeteria")
	Green_Check()
	ll = str(input("-->"))
	if ll=="1":
		clear()
		Launchpad()
	elif ll=="2":
		clear()
		Medbay()
	elif ll=="3":
		clear()
		Locker_Room()
	elif ll=="4":
		clear()
		Comms()
	elif ll=="5":
		clear()
		Office()
	elif ll=="6":
		clear()
		Admin()
	elif ll=="7":
		clear()
		Cafeteria()
	elif ll=="8":
		if Plants==1:
			clear()
			print("you need take the pot first!")
			GreenHouse()
		else:
			clear()
			print("You can pick a number from the list!")
			Reactor()
	else:
		clear()
		print("You can pick a number from the list!")
		GreenHouse()
def Admin():
	Info()
	print(bright_blue+"Admin"+bright_white)
	print("1) Go to Launchpad")
	print("2) Go to Medbay")
	print("3) Go to Locker Room")
	print("4) Go to Communications")
	print("5) Go to GreenHouse")
	print("6) Go to Office")
	print("7) Go to Cafeteria")
	Admin_Check()
	ll = str(input("-->"))
	if ll=="1":
		clear()
		Launchpad()
	elif ll=="2":
		clear()
		Medbay()
	elif ll=="3":
		clear()
		Locker_Room()
	elif ll=="4":
		clear()
		Comms()
	elif ll=="5":
		clear()
		GreenHouse()
	elif ll=="6":
		clear()
		Office()
	elif ll=="7":
		clear()
		Cafeteria()
	elif ll=="8":
		if Code==0:
			clear()
			Enter_Code()
		else:
			clear()
			print("You can pick a number from the list!")
			Reactor()
	else:
		clear()
		print("You can pick a number from the list!")
		Admin()
def Cafeteria():
	Info()
	print(bright_blue+"Cafeteria"+bright_white)
	print("1) Go to Launchpad")
	print("2) Go to Medbay")
	print("3) Go to Locker Room")
	print("4) Go to Communications")
	print("5) Go to GreenHouse")
	print("6) Go to Admin")
	print("7) Go to Office")
	print("8) Go to Storage")
	print("9) Go to Balcony")
	Cafe_Check()
	ll = str(input("-->"))
	if ll=="1":
		clear()
		Launchpad()
	elif ll=="2":
		clear()
		Medbay()
	elif ll=="3":
		clear()
		Locker_Room()
	elif ll=="4":
		clear()
		Comms()
	elif ll=="5":
		clear()
		GreenHouse()
	elif ll=="6":
		clear()
		Admin()
	elif ll=="7":
		clear()
		Office()
	elif ll=="8":
		clear()
		Storage()
	elif ll=="9":
		clear()
		Balcony()
	elif ll=="0":
		if Vend==0:
			clear()
			Vend_Task()
		else:
			clear()
			print("you can pick a number from the list")
			Cafeteria()
	else:
		clear()
		print("You can pick a number from the list!")
		Cafeteria()
def Storage():
	Info()
	print(bright_blue+"Storage"+bright_white)
	print("1) Go to Cafeteria")
	print("2) Go to Balcony")
	Stor_Check()
	ll = str(input("-->"))
	if ll=="1":
		clear()
		Cafeteria()
	elif ll=="2":
		clear()
		Balcony()
	elif ll=="3":
		if Plants==0:
			clear()
			Water_Plants()
		else:
			clear()
			print("You can pick a number from the list!")
			Storage()
	else:
		clear()
		print("You can pick a number from the list!")
		Storage()
def Balcony():
	Info()
	print(bright_blue+"Balcony"+bright_white)
	print("1) Go to Cafeteria")
	print("2) Go to Storage")
	ll = str(input("-->"))
	if ll=="1":
		clear()
		Cafeteria()
	elif ll=="2":
		clear()
		Storage()
	else:
		clear()
		print("You can pick a number from the list!")
		Balcony()
def Dec():
	Info()
	print(bright_blue+"Decontamination"+bright_white)
	print("1) Go to Reactor")
	print("2) Go to Laboratory")
	print("3) Go to Locker Room")
	ll = str(input("-->"))
	if ll=="1":
		clear()
		Reactor()
	elif ll=="2":
		clear()
		Lab()
	elif ll=="3":
		clear()
		Locker_Room()
	else:
		clear()
		print("You can pick a number from the list!")
		Dec()
def Reactor():
	Info()
	print(bright_blue+"Reactor"+bright_white)
	print("1) Go to Laboratory")
	print("2) Go to Decontamination")
	Reactor_Check()
	ll = str(input("-->"))
	if ll=="1":
		clear()
		Lab()
	elif ll=="2":
		clear()
		Dec()
	elif ll=="3":
		if Says==0:
			clear()
			Simon_Says()
		else:
			clear()
			print("You can pick a number from the list!")
			Reactor()
	else:
		clear()
		print("You can pick a number from the list!")
		Reactor()
def Lab():
	Info()
	print(bright_blue+"Laboratory"+bright_white)
	print("1) Go to Reactor")
	print("2) Go to Decontamination")
	ll = str(input("-->"))
	if ll=="1":
		clear()
		Reactor()
	elif ll=="2":
		clear()
		Dec()
	else:
		clear()
		print("You can pick a number from the list!")
		Lab()
def Water_Plants():
	print("Type (pot) and wait do take pot")
	print("or (back) to back")
	pp = str(input("-->"))
	if pp=="pot":
		clear()
		time.sleep(3)
		global Plants
		Plants = 1
		print("you took pot (1/2)")
		Storage()
	elif pp=="back":
		clear()
		Storage()
	else:
		clear()
		print("Fail!")
		Water_Plants()
def Water_Plants2():
	print("Type (Water) and wait to water the plants")
	print("or (back) to back")
	pp = str(input("-->"))
	if pp=="Water":
		clear()
		time.sleep(3)
		global Plants
		Plants = 2
		print("you watered the plants (2/2)")
		GreenHouse()
	elif pp=="back":
		clear()
		GreenHouse()
	else:
		clear()
		print("Fail!")
		Water_Plants2()
def Enter_Code():
	Randcode = random.randint(1000,9999)
	print("Type (",Randcode,") or (back) to back")
	tt = str(input("-->"))
	if tt==str(Randcode):
		clear()
		global Code
		Code = 1
		print("Code is right! (1/1)")
		clear()
		Admin()
	elif tt=="back":
		clear()
		Admin()
	else:
		clear()
		print("Wrong code!")
		time.sleep(1)
		Enter_Code()
def Sumbit_Scan():
	print("Type (Scan) to do a task or (back) to back")
	ff = str(input("-->"))
	if ff=="Scan".lower():
		clear() 
		global Scan
		Scan = 1
		print("You did a task!")
		Medbay()
	elif ff=="back".lower():
		clear()
		Medbay()
	else:
		clear()
		print(bright_red+"Fail!"+bright_white)
		Sumbit_Scan()
def Simon_Says():
	Randcode1 = random.randint(1000,9999)
	print("Type (" + str(Randcode1) + ") to do task")
	print("or (back) to back")
	yy = str(input("-->"))
	if yy==str(Randcode1):
		clear()
		global Says
		Says = 1
		print("Task Completed!")
		Reactor()
	elif yy=="back":
		clear()
		Reactor
	else:
		clear()
		print(bright_red+"Fail!"+bright_white)
		Simon_Says()
def Vend_Task():
	rand9 = random.randint(1,9)
	print("Type ("+str(rand9)+") to do a task")
	print("or (back) to back")
	nn = str(input("-->"))
	if nn==str(rand9):
		global Vend
		Vend = 1
		clear()
		print("Task Completed!")
		Cafeteria()
	elif nn=="back".lower():
		clear()
		Cafeteria()
	else:
		clear()
		print("Fail!")
		Vend_Task()

def Med_Check():
	if Scan==0:
		print("8) Do a Scan Task")
def Stor_Check():
	if Plants==0:
		print("3) Water Plants Task")
def Green_Check():
	if Plants==1:
		print("8) Water Plants Task")
def Cafe_Check():
	if Vend==0:
		print("0) Do Venting Machine Task")
def Reactor_Check():
	if Says==0:
		print("3) Start Reactor Task")
def Admin_Check():
	if Code==0:
		print("8) Enter Code Task")

	
def Task_Checker():
	if Plants==0:
		print(white+"Storage : Water Plants (0/2)"+bright_white)
	elif Plants==1:
		print(bright_yellow+"GreenHouse : Water Plants (1/2)"+bright_white)
	elif Plants==2:
		print(green+"Water Plants (2/2)"+bright_white)
	if Code==0:
		print(white+"Admin : Enter Code"+bright_white)
	elif Code==1:
		print(green+"Enter Code"+bright_white)
	if Scan==0:
		print(white+"Medbay : Sumbit Scan"+bright_white)
	elif Scan==1:
		print(green+"Sumbit Scan"+bright_white)
	if Says==0:
		print(white+"Reactor : Start Reactor"+bright_white)
	elif Says==1:
		print(green+"Start Reactor"+bright_white)
	if Vend==0:
		print(white+"Cafeteria : Venting Machine"+bright_white)
	elif Vend==1:
		print(green+"Venting Machine"+bright_white)
def Win_Checker():
	if Tasks==1:
		if Scan==1 and Says==1 and Vend==1:
			clear()
			print("You did all your tasks")
			print(green+"You won the Game!"+bright_white)
			exit()

	elif Tasks==2:
		if Plants==2 and Says==1 and Vend==1:
			clear()
			print("You did all your tasks")
			print(green+"You won the Game!"+bright_white)
			exit()

	elif Tasks==3:
		if Plants==2 and Code==1 and Vend==1:
			clear()
			print("You did all your tasks")
			print(green+"You won the Game!"+bright_white)
			exit()

	elif Tasks==4:
		if Plants==2 and Code==1 and Scan==1:
			clear()
			print("You did all your tasks")
			print(green+"You won the Game!"+bright_white)
			exit()

	elif Tasks==5:
		if Code==1 and Scan==1 and Says==1:
			clear()
			print("You did all your tasks")
			print(green+"You won the Game!"+bright_white)
			exit()

	elif Tasks==6:
		if Plants==2 and Code==1 and Says==1:
			clear()
			print("You did all your tasks")
			print(green+"You won the Game!"+bright_white)
			exit()

	elif Tasks==7:
		if Code==1 and Says==1 and Vend==1:
			clear()
			print("You did all your tasks")
			print(green+"You won the Game!"+bright_white)
			exit()

	elif Tasks==8:
		if Plants==2 and Scan==1 and Says==1:
			clear()
			print("You did all your tasks")
			print(green+"You won the Game!"+bright_white)
			exit()

	elif Tasks==9:
		if Code==1 and Scan==1 and Vend==1:
			clear()
			print("You did all your tasks")
			print(green+"You won the Game!"+bright_white)
			exit()

	elif Tasks==10:
		if Plants==2 and Scan==1 and Vend==1:
			clear()
			print("You did all your tasks")
			print(green+"You won the Game!"+bright_white)
			exit()