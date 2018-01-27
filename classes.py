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

class RoleCard(pygame.sprite.Sprite):
	def __init__(self, role, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.role = role
		self.image = pygame.image.load("assets\\"+role+".png")
		self.rect = self.image.get_rect()
		self.rect.center = (self.gs.width/2, self.gs.height/2)
		self.doubloons = 0

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

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
			self.rect.center = ((61/80)*self.gs.width, (1/14)*self.gs.height)
		elif (self.size == 2):
			self.rect.center = ((61/80)*self.gs.width, (3/14)*self.gs.height)
		elif (self.size == 3):
			self.rect.center = ((61/80)*self.gs.width, (5/14)*self.gs.height)
		self.spaces_Left = numSpaces

class ColonistShip(pygame.sprite.Sprite):
	def __init__(self, numColonists, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\colonist_ship.png")
		self.rect = self.image.get_rect()
		self.rect.center = ((19/80)*self.gs.width, (3/14)*self.gs.height)
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
		self.rect.center = ((19/80)*self.gs.width, (1/14)*self.gs.height)

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

		self.l2 = "Play with " + str(self.numPlayers) + " players (Press the Up or Down arrows to change)"
		self.l3 = "Press Enter to begin!"

	def tick(self):
		self.l2 = "Play with " + str(self.numPlayers) + " players (Press the Up or Down arrows to change)"

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

class SmallIndigoPlant(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\small_indigo_plant.png")
		self.rect = self.image.get_rect()
		self.rect.center = ((99/320)*self.gs.width, (11/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class SmallSugarMill(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\small_sugar_mill.png")
		self.rect = self.image.get_rect()
		self.rect.center = ((99/320)*self.gs.width, (21/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class SmallMarket(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\small_market.png")
		self.rect = self.image.get_rect()
		self.rect.center = ((99/320)*self.gs.width, (31/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class Hacienda(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\hacienda.png")
		self.rect = self.image.get_rect()
		self.rect.center = ((99/320)*self.gs.width, (41/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class ConstructionHut(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\construction_hut.png")
		self.rect = self.image.get_rect()
		self.rect.center = ((99/320)*self.gs.width, (51/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class SmallWarehouse(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\small_warehouse.png")
		self.rect = self.image.get_rect()
		self.rect.center = ((99/320)*self.gs.width, (61/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class IndigoPlant(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\indigo_plant.png")
		self.rect = self.image.get_rect()
		self.rect.center = ((259/640)*self.gs.width, (11/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class SugarMill(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\sugar_mill.png")
		self.rect = self.image.get_rect()
		self.rect.center = ((259/640)*self.gs.width, (21/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class Hospice(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\hospice.png")
		self.rect = self.image.get_rect()
		self.rect.center = ((259/640)*self.gs.width, (31/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class Office(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\office.png")
		self.rect = self.image.get_rect()
		self.rect.center = ((259/640)*self.gs.width, (41/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class LargeMarket(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\large_market.png")
		self.rect = self.image.get_rect()
		self.rect.center = ((259/640)*self.gs.width, (51/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class LargeWarehouse(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\large_warehouse.png")
		self.rect = self.image.get_rect()
		self.rect.center = ((259/640)*self.gs.width, (61/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class TobaccoStorage(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\tobacco_storage.png")
		self.rect = self.image.get_rect()
		self.rect.center = (self.gs.width/2, (11/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class CoffeeRoaster(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\coffee_roaster.png")
		self.rect = self.image.get_rect()
		self.rect.center = (self.gs.width/2, (21/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class University(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\university.png")
		self.rect = self.image.get_rect()
		self.rect.center = (self.gs.width/2, (31/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class Factory(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\factory.png")
		self.rect = self.image.get_rect()
		self.rect.center = (self.gs.width/2, (41/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class Harbor(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\harbor.png")
		self.rect = self.image.get_rect()
		self.rect.center = (self.gs.width/2, (51/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class Wharf(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\wharf.png")
		self.rect = self.image.get_rect()
		self.rect.center = (self.gs.width/2, (61/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class GuildHall(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\guild_hall.png")
		self.rect = self.image.get_rect()
		self.rect.center = ((59.5/100)*self.gs.width, (15.25/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class Residence(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\residence.png")
		self.rect = self.image.get_rect()
		self.rect.center = ((6.85/10)*self.gs.width, (15.25/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class Fortress(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\fortress.png")
		self.rect = self.image.get_rect()
		self.rect.center = ((59.5/100)*self.gs.width, (35.25/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class CustomsHouse(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\customs_house.png")
		self.rect = self.image.get_rect()
		self.rect.center = ((6.85/10)*self.gs.width, (35.25/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

class CityHall(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)

		self.gs = gs
		self.image = pygame.image.load("assets\\city_hall.png")
		self.rect = self.image.get_rect()
		self.rect.center = ((64/100)*self.gs.width, (55.25/112)*self.gs.height)

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())