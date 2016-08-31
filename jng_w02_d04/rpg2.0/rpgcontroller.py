from rpgviews import Views
from hellrpgmodel import Model
import random

class Game:
	def __init__(self):
		self.views = Views()
		self.model = Model()
		

		#self.login()
		# self.username
		# self.password
		

	# def login(self):
	# 	user_info = self.view.user_login_input()
	# 	verify_user_exists == self.model.verify_user_info(user_login_input[0], user_login_input[1])
	# 	if self.views.new_user() == 1 :
	# 		self.model.create_login(user_login_input[0], user_login_input[1])
	# 	else:
	# 		break


	# def login(self):
	# 	login = self.view.login(self.name2)
	# 	check_user = self.model.check_user(self.name2)
	# 	if check_user is False:
	# 	  	self.model.add_player(self.name2)
	#	else:
	#		break
		

		# #newuser = self.views.v_new_user() #This is not = 1 or 2 and corresponds to make a new user yes or no
		# userinput = self.views.user_login_input()
		# print ("userinput", userinput)
		# check = self.model.check_user(userinput[0], userinput[1])
		# print ("check", check)
		# # if newuser == 1:
		# # 	user_data = self.views.user_login_input()
		# # elif newuser == 2
		# # 	user_data = self.views.user_login_input()
		# # 	if	user_data == self.model.check_user(user_data[0],user_data[1])
		
		
	def start(self):
		player = Main_dude(self.views, self.model) # I am confused as to weather or not this shoul be self. player or not. 
		player.randclas()
		fight1_choi  = self.views.begining(player) 
		B1 = self.battle.fight_scene_1(player, host_demon, fight1_choi)

class Main_dude(Game):
	def __init__(self, m, v):
		self.mod = m
		self.vew = v		
		self.name = self.vew.input_player_name()
		self.gender = self.vew.input_gender()
		self.rand = self.vew.input_player_class()



	def randclas(self):
		rando = self.rand
		if rando == 1:
			print("Hot Dog was'nt a choice.... but im not going to stand here and argue with a hotdog!")
			self.clas = "Hot Dog"
			self.hp = 40
			self.accuracy = .70
			self.mana = 16
			self.attack = 8
			self.magicdamage = 12
		elif rando == 2:
			print ("Wow I didnt know their were any Dilosaurs left in the world.")
			self.clas = "Dilosaur"
			self.hp = 60
			self.accuracy = .65
			self.mana = 10
			self.attack = 11
			self.magicdamage = 11
		else:
			print("Oh your an alcoholic, me too.. AA for life") 
			self.clas = "Alcoholic"
			self.hp = 80
			self.accuracy = .45
			self.mana = 6
			self.attack = 14
			self.magicdamage = 10

	def take_damage(self, damage):
		self.hp -= damage

	def heal_self(self, player):
		# need to access an inventory an use up a potion when the function heal self is called.
		self.hp += potion

	def use_mana(self, mana_cost):
		self.mana -= mana_cost

	def player_death(self, player):
		while player.hp > 0:
			if player.hp <= 0:
				choi = self.views.dead_player_message()
				if choi == 0:
					Game()
				elif choi == 1:
					raise SystemExit

class Battle(Game):
	def __init__(self, main_dude, damage): # i'm pretty sure i messed this up possibly needs an enemy
		Enemy.__init__(self)
		self.main_dude = Main_dude
		self.enemy = Enemy()
		self.view = Views()
		self.player_turn = True # not sure what to put here at the moment
		#self.enemy_turn = # not sure what to put here at the moment or if i need this


	def fight_scene_1(self, player, fight1_choi):		
		if fight1_choi.lower() == "yes":
			self.views.b1_choi_yes(self, player)
			#do something that moves you to the fire pit
			
		elif fight1_choi.lower(self, player) == "no":
			self.views.b1_choi_no(self, player)
			""" Start battle sequence"""
			
		elif fight1_choi.lower() == "fight":
			""" Start battle sequence"""
			self.views.b1_choi_fight(self, player)
			self.fight(host_demon)
		
		else:
			self.views.b1_choi_else(self, player)
			"""make the player lose 2 hp and start back at the top"""
			player.hp -= 1
			return player.hp

	def fight(self):
		while player.hp >= 0 or enemy.hp >= 0:
			self.views.battle_view()
			if player.hp <= 0:
				player_death()
			elif enemy.hp <= 0:
				self.views.dead_monster_message()
			elif self.player_turn:
				choice = self.views.battle_view()
				if choice == 0: #which corresponds to attack
					if self.player.accuracy < random.random(0,1):
						self.enemy.take_damage(self.player.attack)
				elif choice == 3: # use a potion
					self.player.heal_self(self.player.potion)
				elif choice == 2: # block
					if .70 < random.random(0,1):
						self.player.take_damage(self.enemy.attack)
						self.player_turn =True
						return True
					else:
						self.views.block_message
						self.player_turn = True
						return True
				elif choice == 1:
					if self.player.mana > 3:
						self.enemy.take_damage(self.player.magicdamage)
						self.player.use_mana(3)
				else:
					self.views.you_are_dumb
					self.player.take_damage(1)
			elif not self.player_turn:
				self.views.enemy_health(self.enemy.name , self.enemy.health)
				if self.enemy.accuracy < random.random(0,1):
					self.views.you_were_hit_message(self.enemy.name, self.enemy.damage)





class Enemy(Game):
	def __init__(self, damage):
		self.hp -= damage

	def death(self):
		return self.hp < 0

class host_demon(Enemy):
	def __init__(self):	
		self.hp = 30
		self.attack = 8
		self.accuracy = .65
		self.name = "Host Demon"
		self.clas = ''

class mini_demon(Enemy):
	def __init__(self):	
		self.hp = 10
		self.attack = 4
		self.accuracy = .7
		self.attackname = "Scratch"
		self.name = "Mini Demon"

class devil(Enemy):
	def __init__(self):	
		self.hp = 40
		self.attack = 12
		self.accuracy = .6
		self.attackspecial = 15
		self.name = "Devil"
		self.item = "potion"







game1 = Game()
game1.start()
