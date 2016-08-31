# story line stuff goes in game class. doesnt hold stats just text

import random


class Views:
	def __init__(self):
		pass

	# def user_login_input(self):
	# 	v_username = str(input("Input Username!"))
	# 	v_password = str(input("Input Password!"))
	# 	return v_username, v_password

	# def v_new_user(self):
	# 	choice = int(input("Create New User? \n> [1] Yes\n>[2] No"))
	# 	return choice



	# def name(self):
	# 	name = input("what is your name? ")
	# 	return name

	# def login(self, name):
	# 	print("checking to see if {name} is in Database".format(name = name))

	def input_player_name(self):
		print("Welcome to Hell!!!! \n I am your host demon and will help you get started!")
		input("What is your name? \n")
		name = "Buttface"
		print("Your name is Buttface,.... Thats wierd but I guess your parents hate you! I do too. ")
		return name

	def input_gender(self):
		gender = input("What is your gender? \n >  ")
		if gender == 'male' or 'Male':
			print("That thing between your legs doesnt count! We shall refer to you as It.")
			gender = "It"
			return gender
		elif gender == girl or Girl or female or Female:
			print ("You looka like a manboy! We shall call you Dickbutt")
			gender = "Dickbutt"
			return gender
		else:
			print("I dont even know what that is. We'll just say your an 'it'")
			gender = "It"
			return gender
	
	def input_player_class(self):
		input("What type of class are you? \n > Pagan \n > Barbarian \n > Witch Doctor \n")
		rando = random.randint(1,3)
		return rando

	def begining(self, player):  # this may require additional arguments to be passed in or more specific input than player
		print("{type1} {name} are you ready for your thousand years of torture!?".format( type1 = player.clas  , name = player.name ))
		choice = input("Choice: \n> Yes \n> No \n > Fight!")
		return choice
	
	def b1_choi_yes(self):		
		print("The demon starts beating you with his whip, and shouts get to the fire pit")
	
	def b1_choi_no(self):	
		print("Host Demon: How dare you defy me!!")
	
	def b1_choi_fight(self, player): # this may require additional arguments
		print("{name}: Shouts in {type1}, prepare to die DEMON SWINE!!!!".format(type1 = player.clas , name = player.name))

	def b1_choi_else(self):	
		print("What the heck are you doing? He whips you for being dumb -1HP")
#### need to jump to battle seq

	def middle(mid):
		pass

	def ending(end):
		pass

	
	def battle_view(self):
		choice = input("Health = {health} Mana = {mana} \n>[0] Attack with {weapon} \n>[1] Magic [costs 3 mana] \n> [2] Block \n>[3] Health {potion}".format( health = '', mana = '', weapon = '', potion = '' ))
		if choice in [ '0', '1', '2', '3']:
			return int(choice)

	def you_were_hit_message(self, enemy_type, enemy_damage):
		print("{} had attacked hit. and dealth {}".format(enemy_type , enemy_damage))

	def block_message(self):
		print("Your block was sucessful! You take no damage.")

	def you_are_dumb(self):
		print("Hey Buttface make a move!")

	def enemy_health(self, enemy_type, enemy_health):
		print("{} : HP> {}".format(enemy_type, enemy_health))

	def dead_player_message(self):
		choice = ''
		while True:
			print(" You died in Hell, im not sure where you go from here....  back to the start of your day. Or you could go back to Jersey.")
			choice = input(">[0] Restart \n>[1] Quit ")
			if choice in ['0','1']: 
				return int(choice)
		 # jump to the start

	def dead_monster_message(self):
		print("The {enemy} is dead!".format(enemy = ''))









