""" ###1 create a class charecter in the game:
 it will have attributes like name, gender, class, armor, magic item, weapon,health



##2
classes will be (barbarian, wizard, ninja)
create a class for each.

##3
barbarian will have:
weapon: ax
armor : leather
health : 80

##4
wizard will have
weapon: wand
armor : robe
health: 60

##5
Ninja:
weapon: sword
armor: ninja armor
health: 70

###6
you will be prompted for an input for your name, gender, and class, health

##7
text will appear --- hello honerable{class} {name}, I have a  quest for you. 
you must rescue the princess from the dungeon and collect the sword of destiny.

##8 
do you want to go on the quest yes or no
quest_yes_no = str(input("yes or no"))
if quest_yes_no == "yes":
	print(" You must head into the secret cellar under the haunted tree)
elif quest_yes_no == "no":
	print("then why the hell would you play the game")
else:
	print("that is not a yest or no")

##9
print(" you  journey over to the tree and see there is a gnome near the tree.
He shouts to you hurry chosen one, you must rescue the princess. Drink this potion )
print("do you drink the potion" > y > n)
if y:
	size = True
	print("you are shunken to gnome size, and now can enter the cellar. \n the guarding transforms into a gargoyle and sneak attacks you fro 5 damage")

else: 
	size = False

<yourname>.health(-5)

##10
 
print("You can use attack, or block")
str(input("attack"))
str(input("block"))

if attack:






"""

import random

# story line stuff goes in game class. doesnt hold stats just text
class Game:
	print("Welcome to Hell!!!! \n I am your host demon and will help you get started!")
	def __init__(self):
		self.user = Charecter()
		self.begin = self.begining()
		self.mid = self.middle()
		self.end = self.ending()
		self.user = user

	def begining(self):
		while True:
			print("{type1} {name} are you ready for your thousand years of torture!?".format( type1 = Charecter.char_type , name = Charecter.name))
			choice = input("Choice: \n> Yes \n> No \n > Fight!")
#### need to jump to battle seq
			if choice.lower() == "yes":
				print("The demon starts beating you with his wip towards a whip, and shouts get to the fire pits. '- 2HP total HP = {health}".format(health = self.user.hp))
				"""cause player to lose 2 healh & start the battle"""
			elif choice.lower() == "no":
				print("How dare you defy me!")
				""" Start battle sequence"""
			elif choice.lower() == "fight":
				print("you take a swing at the demon!")
				""" Start battle sequence"""
			else: 
				print("What the heck are you doing? He whips you for being dumb -1HP")
				"""make the player lose 2 hp and start back at the top"""
				return self.user.hp - 1




	def middle(mid):
		pass

	def ending(end):
		pass


class Charecter(Game):
	""" set up the charecter"""
	def __init__(self):
		self.name = self.name_setup()
		self.gender = self.gender_setup()
		self.char_type = Classes()

		print ("Okay... {name}... so you area a {gender}, and {class}. \n Yup everyone really hates you no wonder your in Hell!".format( name = self.name , gender = self.gender))
		

	def name_setup(self):
		input("What is your name? \n")
		self.name = "Buttface"
		print("Your name is Buttface,.... Thats wierd but I guess your parents hate you! I do too. ")
		return self.name
	
	def say_gender(self):
		gender = input("What is your gender? \n >  ")
		if gender == male or Male:
			print("That thing between your legs doesnt count! We shall refer to you as It.")
			self.gender = "It"
			return self.gender
		elif gender == girl or Girl or female or Female:
			print ("You looka like a manboy! We shall call you Dickbutt")
			self.gender = "Dickbutt"
			return self.gender
		else:
			print("I dont even know what that is. We'lll just say your an 'it'")
			self.gender = "It"
			return self.gender

class Classes(Charecter):
	def __init__(self):
		self.clas = self.type()
		self.hp = hp
		self.mana = mana
		self.accuracy = accuracy

	def type(self):
		input("What type of class are you? \n > Pagan \n > Barbarian \n > Witch Doctor")
		rando = random.randint(1,3)
		if rando == 1:
			print("Hot Dog was'nt a choice.... but im not going to stand here and argue with a hotdog!")
			self.clas = Classes.hotdog()
			return self.clas 
		elif rando == 2:
			print ("Wow I didnt know their were any dilosaurs left in the world.")
			self.clas = Classes.dilosaurs()
			return self.clas
		else:
			print("Oh your an alcoholic, me too.. AA for life") 
			self.clas = Classes.alcoholic()
			return self.clas

	def hotdog(self):
		self.hp = 40
		self.accuracy = .70
		self.mana = 16
		self.attack = Weapons.hotdog_damage()
		self.speed = Weapons.hotdog_speed()
		self.magic = Magic.fireball_damage

	def alcoholic(self):
		self.hp = 60
		self.accuracy = .45
		self.mana = 10
		self.attack = Weapons.alcoholic_damage()
		self.speed = Weapons.alcoholic_speed()
		self.magic = Magic.fireball_damage

	def dilosaurs(self):
		self.hp = 80
		self.accuracy = .67
		self.mana = 6
		self.attack = Weapons.dilosaurs_damage()
		self.speed = weapons.dilosaurs_speed()
		self.magic = Magic.fireball_damage



class Weapons(Classes):
	axe_damage = 10
	axe_speed = 1
	sword_damage = 7
	sword_speed = 1.3
	wand_damage = 6
	wand_speed = 1.1
	hotdogpunch = 

class Magic(Classes):
	fireball_damage = 13
	fireball_use = 2

class Enemy():

	def host_demon():


class Battle(Game)



start = Game()




	# def __init__(self, armor, health, weapon, Char_type): 
	# 	self.armor = armor
	# 	self.health = health
	# 	self.weapon = weapon

	# def health(self, n):
	# 	health = 80
	# 	print(health)
	# 	if health > 0:
	# 		return 80 - n
	# 	else:
	# 		print("You are dead!")

	# def attack(self, n):
	# 	pass






# str(input("Choose your class. \n > Barbarian \n > Wizard \n Ninja"))
# name = str(input)



# print ("hello honerable{cclass} {name}, I have a  quest for you. you must rescue the princess from the dungeon and collect the sword of destiny.".format)



