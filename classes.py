# Brian Mann
# Puerto Rico
# Classes
# 1/15/2018

import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, pn, numPlayers, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.pn = pn
		self.building_spaces = 12
		self.island_spaces = 12
		self.vpoints = 0
		if numPlayers == 3:
			self.doubloons = 2
		elif numPlayers == 4:
			self.doubloons = 3
		else:
			self.doubloons = 4

class CargoShip(pygame.sprite.Sprite):
	def __init__(self, numSpaces, size, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.total_Spaces = numSpaces
		self.size = size
		self.imagename = "assets\\cargoship" + str(self.total_Spaces) + ".png"
		self.image = pygame.image.load(self.imagename)
		self.rect = self.image.get_rect()
		if (self.size == 1):
			self.rect.center = ((10/20)*self.gs.width, (18/20)*self.gs.height)
		elif (self.size == 2):
			self.rect.center = ((11/20)*self.gs.width, (18/20)*self.gs.height)
		elif (self.size == 3):
			self.rect.center = ((12/20)*self.gs.width, (18/20)*self.gs.height)
		self.spaces_Left = numSpaces

class ColonistShip(pygame.sprite.Sprite):
	def __init__(self, numColonists, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\colonist_ship.png")
		self.rect = self.image.get_rect()
		self.rect.center = ((8/20)*self.gs.width, (18/20)*self.gs.height)
		self.numColonists = numColonists

class TradingHouse(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.space1 = None
		self.space2 = None
		self.space3 = None
		self.space4 = None
		self.image = pygame.image.load("assets\\trading_house.png")
		self.rect = self.image.get_rect()
		self.rect.center = ((9/20)*self.gs.width, (18/20)*self.gs.height)

class BuildingBoard(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\building_board.png")
		self.rect = self.image.get_rect()
		self.rect.center = (self.gs.width/2, 3*self.gs.height/10)

class Menu(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)
		self.gs = gs
		self.image = pygame.image.load("assets\\menu.png")
		self.rect = self.image.get_rect()
		self.rect.center = (self.gs.width/2, self.gs.height/2)
		self.numPlayers = self.gs.minPlayers
		self.isMenu = True

		self.l2 = pygame.font.SysFont('mono', 36, bold=True).render("Play with " + str(self.numPlayers) + " players (Press the Up or Down arrows to change)", True, (150,150,255))
		self.l3 = pygame.font.SysFont('mono', 36, bold=True).render("Press Enter to begin!", True, (150,150,255))

	def tick(self):
		self.l2 = pygame.font.SysFont('mono', 36, bold=True).render("Play with " + str(self.numPlayers) + " players (Press the Up or Down arrows to change)", True, (150,150,255))

	def changePlayers(self, code):
		if code == pygame.K_UP:
			if self.numPlayers == self.gs.maxPlayers:
				pass
			else:
				self.numPlayers += 1
		else:
			if self.numPlayers == self.gs.minPlayers:
				pass
			else:
				self.numPlayers -= 1

class PlayerBoard(pygame.sprite.Sprite):
	def __init__(self, playerNumber, gs=None):
		pygame.sprite.Sprite.__init__(self)
		self.gs = gs
		self.playerNumber = playerNumber
		self.image = pygame.image.load("assets\\player_board.png")
		self.rect = self.image.get_rect()
		self.rect.center = (self.gs.width/2, self.gs.height/2)

		self.playertext = pygame.font.SysFont('mono', 36, bold=True).render("Player " + str(self.playerNumber), True, (150,150,255))

class ClickableObject(pygame.sprite.Sprite):
	def __init__(self, card_type, name, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\"+name+".png")
		self.rect = self.image.get_rect()

		if card_type == 'RoleCard':
			#self.rect.center = (self.gs.width/2, self.gs.height/2)
			self.doubloons = 0
			if name == 'settler':
				pass
			elif name == 'mayor':
				pass
			elif name == 'builder':
				pass
			elif name == 'crafstman':
				pass
			elif name == 'trader':
				pass
			elif name == 'captain':
				pass
			elif name == 'prospector':
				pass
		elif card_type == 'Building':
			if name == 'small_indigo_plant':
				self.rect.center = ((99/320)*self.gs.width, (11/112)*self.gs.height)
			elif name == 'small_sugar_mill':
				self.rect.center = ((99/320)*self.gs.width, (21/112)*self.gs.height)
			elif name == 'small_market':
				self.rect.center = ((99/320)*self.gs.width, (31/112)*self.gs.height)
			elif name == 'hacienda':
				self.rect.center = ((99/320)*self.gs.width, (41/112)*self.gs.height)
			elif name == 'construction_hut':
				self.rect.center = ((99/320)*self.gs.width, (51/112)*self.gs.height)
			elif name == 'small_warehouse':
				self.rect.center = ((99/320)*self.gs.width, (61/112)*self.gs.height)
			elif name == 'indigo_plant':
				self.rect.center = ((259/640)*self.gs.width, (11/112)*self.gs.height)
			elif name == 'sugar_mill':
				self.rect.center = ((259/640)*self.gs.width, (21/112)*self.gs.height)
			elif name == 'hospice':
				self.rect.center = ((259/640)*self.gs.width, (31/112)*self.gs.height)
			elif name == 'office':
				self.rect.center = ((259/640)*self.gs.width, (41/112)*self.gs.height)
			elif name == 'large_market':
				self.rect.center = ((259/640)*self.gs.width, (51/112)*self.gs.height)
			elif name == 'large_warehouse':
				self.rect.center = ((259/640)*self.gs.width, (61/112)*self.gs.height)
			elif name == 'tobacco_storage':
				self.rect.center = (self.gs.width/2, (11/112)*self.gs.height)
			elif name == 'coffee_roaster':
				self.rect.center = (self.gs.width/2, (21/112)*self.gs.height)
			elif name == 'university':
				self.rect.center = (self.gs.width/2, (31/112)*self.gs.height)
			elif name == 'factory':
				self.rect.center = (self.gs.width/2, (41/112)*self.gs.height)
			elif name == 'harbor':
				self.rect.center = (self.gs.width/2, (51/112)*self.gs.height)
			elif name == 'wharf':
				self.rect.center = (self.gs.width/2, (61/112)*self.gs.height)
			elif name == 'guild_hall':
				self.rect.center = ((59.5/100)*self.gs.width, (15.25/112)*self.gs.height)
			elif name == 'residence':
				self.rect.center = ((6.85/10)*self.gs.width, (15.25/112)*self.gs.height)
			elif name == 'fortress':
				self.rect.center = ((59.5/100)*self.gs.width, (35.25/112)*self.gs.height)
			elif name == 'customs_house':
				self.rect.center = ((6.85/10)*self.gs.width, (35.25/112)*self.gs.height)
			elif name == 'city_hall':
				self.rect.center = ((64/100)*self.gs.width, (55.25/112)*self.gs.height)

	def is_clicked(self):
		self.rect.center = (self.gs.width/2, self.gs.height)