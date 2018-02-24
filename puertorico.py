# Brian Mann
# Puerto Rico
# Main Executable
# 1/15/2018

import sys, math, os, random
from classes import *
from pygame.locals import *
from random import sample

class GameSpace:
	def main(self):
		#initialization
		pygame.init()
		pygame.key.set_repeat(1, 50)

		# game constants
		infoObject = pygame.display.Info()
		self.size = self.width, self.height = infoObject.current_w, infoObject.current_h
		self.black = 255, 255, 255

		self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
		self.clock = pygame.time.Clock()

		self.gameOver = False
		self.selectedRole = ""
		self.quit = False

		self.title = pygame.font.SysFont('mono', 36, bold=True).render("Puerto Rico", True, (100, 100, 200))

		self.minPlayers = 3
		self.maxPlayers = 5

		# Menu Screen
		self.menu = Menu(self)

		while self.menu.isMenu == True:
			self.clock.tick(60)

			for event in pygame.event.get():
				if event.type == QUIT:
					sys.exit()
				elif event.type == KEYDOWN:
					if (event.key == pygame.K_UP or event.key == pygame.K_DOWN):
						self.menu.changePlayers(event.key)
					elif event.key == pygame.K_q:
						sys.exit()
					elif event.key == pygame.K_RETURN:
						self.menu.isMenu = False
					else:
						pass
				else:
					pass

			self.menu.tick()

			self.screen.fill(self.black)

			self.screen.blit(self.menu.image, self.menu.rect)
			self.screen.blit(self.title, ((self.width/2) - (self.title.get_rect().width/2), (1/20)*self.height))
			self.screen.blit(self.menu.l2, ((self.width/2) - (self.menu.l2.get_rect().width/2), (3/20)*self.height))
			self.screen.blit(self.menu.l3, ((self.width/2) - (self.menu.l3.get_rect().width/2), (17/20)*self.height))

			pygame.display.flip()

		self.numPlayers = self.menu.numPlayers
		self.players = []
		for i in range(0,self.numPlayers):
			self.players.append(Player(i, self.numPlayers, self))

		self.numCorn = 10
		self.numIndigo = 11
		self.numSugar = 11
		self.numTobacco = 9
		self.numCoffee = 9
		self.numQuarry = 8
		self.numCornPlants = 10
		self.numIndigoPlants = 12
		self.numSugarPlants = 11
		self.numTobaccoPlants = 9
		self.numCoffeePlants = 8

		sprite_list = []

		# Sprites that won't be clicked
		self.colonistship = ColonistShip(self.numPlayers, self)
		self.tradinghouse = TradingHouse(self)
		self.buildingboard = BuildingBoard(self)
		self.playerboards = []
		for i in range(1, self.numPlayers+1):
			self.playerboards.append(PlayerBoard(i, self))

		# Sprites that will be clicked
		self.settler = ClickableObject("RoleCard", "settler", self)
		sprite_list.append(self.settler)
		self.mayor = ClickableObject("RoleCard", "mayor", self)
		sprite_list.append(self.mayor)
		self.builder = ClickableObject("RoleCard", "builder", self)
		sprite_list.append(self.builder)
		self.craftsman = ClickableObject("RoleCard", "craftsman", self)
		sprite_list.append(self.craftsman)
		self.trader = ClickableObject("RoleCard", "trader", self)
		sprite_list.append(self.trader)
		self.captain = ClickableObject("RoleCard", "captain", self)
		sprite_list.append(self.captain)
		self.smallindigoplant = ClickableObject("Building", "small_indigo_plant", self)
		sprite_list.append(self.smallindigoplant)
		self.smallsugarmill = ClickableObject("Building", "small_sugar_mill", self)
		sprite_list.append(self.smallsugarmill)
		self.smallmarket = ClickableObject("Building", "small_market", self)
		sprite_list.append(self.smallmarket)
		self.hacienda = ClickableObject("Building", "hacienda", self)
		sprite_list.append(self.hacienda)
		self.constructionhut = ClickableObject("Building", "construction_hut", self)
		sprite_list.append(self.constructionhut)
		self.smallwarehouse = ClickableObject("Building", "small_warehouse", self)
		sprite_list.append(self.smallwarehouse)
		self.indigoplant = ClickableObject("Building", "indigo_plant", self)
		sprite_list.append(self.indigoplant)
		self.sugarmill = ClickableObject("Building", "sugar_mill", self)
		sprite_list.append(self.sugarmill)
		self.hospice = ClickableObject("Building", "hospice", self)
		sprite_list.append(self.hospice)
		self.office = ClickableObject("Building", "office", self)
		sprite_list.append(self.office)
		self.largemarket = ClickableObject("Building", "large_market", self)
		sprite_list.append(self.largemarket)
		self.largewarehouse = ClickableObject("Building", "large_warehouse", self)
		sprite_list.append(self.largewarehouse)
		self.tobaccostorage = ClickableObject("Building", "tobacco_storage", self)
		sprite_list.append(self.tobaccostorage)
		self.coffeeroaster = ClickableObject("Building", "coffee_roaster", self)
		sprite_list.append(self.coffeeroaster)
		self.university = ClickableObject("Building", "university", self)
		sprite_list.append(self.university)
		self.factory = ClickableObject("Building", "factory", self)
		sprite_list.append(self.factory)
		self.harbor = ClickableObject("Building", "harbor", self)
		sprite_list.append(self.harbor)
		self.wharf = ClickableObject("Building", "wharf", self)
		sprite_list.append(self.wharf)
		self.guildhall = ClickableObject("Building", "guild_hall", self)
		sprite_list.append(self.guildhall)
		self.residence = ClickableObject("Building", "residence", self)
		sprite_list.append(self.residence)
		self.fortress = ClickableObject("Building", "fortress", self)
		sprite_list.append(self.fortress)
		self.customshouse = ClickableObject("Building", "customs_house", self)
		sprite_list.append(self.customshouse)
		self.cityhall = ClickableObject("Building", "city_hall", self)
		sprite_list.append(self.cityhall)

		if self.numPlayers == 3:
			self.vpoints = 75
			self.colonists = 55
			self.cargo1 = CargoShip(4, 1, self)
			self.cargo2 = CargoShip(5, 2, self)
			self.cargo3 = CargoShip(6, 3, self)
			self.prospector1 = None
			self.prospector2 = None
			self.numPiles = 4
			self.doubloons = 80
		elif self.numPlayers == 4:
			self.vpoints = 100
			self.colonists = 75
			self.cargo1 = CargoShip(5, 1, self)
			self.cargo2 = CargoShip(6, 2, self)
			self.cargo3 = CargoShip(7, 3, self)
			self.prospector1 = ClickableObject("RoleCard", "prospector1", self)
			self.prospector2 = None
			self.numPiles = 5
			self.doubloons = 74
		else:
			self.vpoints = 122
			self.colonists = 95
			self.cargo1 = CargoShip(6, 1, self)
			self.cargo2 = CargoShip(7, 2, self)
			self.cargo3 = CargoShip(8, 3, self)
			self.prospector1 = ClickableObject("RoleCard", "prospector1", self)
			self.prospector2 = ClickableObject("RoleCard", "prospector2", self)
			self.numPiles = 6
			self.doubloons = 66

		self.turnOrder(self.players)

		showBuildingBoard = False
		playerView = 1

		# main game loop
		while self.quit == False:
			self.clock.tick(60)
			self.selectedRole = ""

			# handle input
			for event in pygame.event.get():
				if event.type == QUIT:
					sys.exit()
				elif event.type == KEYDOWN:
					if event.key == pygame.K_q:
						sys.exit()
					elif event.key == pygame.K_b:
						showBuildingBoard = True
					elif event.key == pygame.K_m:
						showBuildingBoard = False
					elif event.key == pygame.K_1:
						playerView = 1
					elif event.key == pygame.K_2:
						playerView = 2
					elif event.key == pygame.K_3:
						playerView = 3
					elif event.key == pygame.K_4 and self.numPlayers >= 4:
						playerView = 4
					elif event.key == pygame.K_5 and self.numPlayers == 5:
						playerView = 5
					else:
						pass
				elif event.type == MOUSEBUTTONUP and event.button == 1:
					for s in sprite_list:
						if s.rect.collidepoint(pygame.mouse.get_pos()):
							self.selectedRole = s.is_clicked()
				else:
					pass
			# game logic
			

			# display objects in main screen
			self.screen.fill(self.black)
			if showBuildingBoard:
				self.screen.blit(self.buildingboard.image, self.buildingboard.rect)
				self.screen.blit(self.smallindigoplant.image, self.smallindigoplant.rect)
				self.screen.blit(self.smallsugarmill.image, self.smallsugarmill.rect)
				self.screen.blit(self.smallmarket.image, self.smallmarket.rect)
				self.screen.blit(self.hacienda.image, self.hacienda.rect)
				self.screen.blit(self.constructionhut.image, self.constructionhut.rect)
				self.screen.blit(self.smallwarehouse.image, self.smallwarehouse.rect)
				self.screen.blit(self.indigoplant.image, self.indigoplant.rect)
				self.screen.blit(self.sugarmill.image, self.sugarmill.rect)
				self.screen.blit(self.hospice.image, self.hospice.rect)
				self.screen.blit(self.office.image, self.office.rect)
				self.screen.blit(self.largemarket.image, self.largemarket.rect)
				self.screen.blit(self.largewarehouse.image, self.largewarehouse.rect)
				self.screen.blit(self.tobaccostorage.image, self.tobaccostorage.rect)
				self.screen.blit(self.coffeeroaster.image, self.coffeeroaster.rect)
				self.screen.blit(self.university.image, self.university.rect)
				self.screen.blit(self.factory.image, self.factory.rect)
				self.screen.blit(self.harbor.image, self.harbor.rect)
				self.screen.blit(self.wharf.image, self.wharf.rect)
				self.screen.blit(self.guildhall.image, self.guildhall.rect)
				self.screen.blit(self.residence.image, self.residence.rect)
				self.screen.blit(self.fortress.image, self.fortress.rect)
				self.screen.blit(self.customshouse.image, self.customshouse.rect)
				self.screen.blit(self.cityhall.image, self.cityhall.rect)
			else:
				self.screen.blit(self.tradinghouse.image, self.tradinghouse.rect)
				self.screen.blit(self.colonistship.image, self.colonistship.rect)
				self.screen.blit(self.cargo1.image, self.cargo1.rect)
				self.screen.blit(self.cargo2.image, self.cargo2.rect)
				self.screen.blit(self.cargo3.image, self.cargo3.rect)
				self.screen.blit(self.builder.image, self.builder.rect)
				self.screen.blit(self.captain.image, self.captain.rect)
				self.screen.blit(self.craftsman.image, self.craftsman.rect)
				self.screen.blit(self.mayor.image, self.mayor.rect)
				self.screen.blit(self.settler.image, self.settler.rect)
				self.screen.blit(self.trader.image, self.trader.rect)
				if self.prospector1 is not None:
					self.screen.blit(self.prospector1.image, self.prospector1.rect)
				if self.prospector2 is not None:
					self.screen.blit(self.prospector2.image, self.prospector2.rect)
				if playerView == 1:
					self.screen.blit(self.playerboards[0].image, self.playerboards[0].rect)
					self.screen.blit(self.playerboards[0].playertext, ((self.width/2) - (self.title.get_rect().width/2), (1/20)*self.height))
				elif playerView == 2:
					self.screen.blit(self.playerboards[1].image, self.playerboards[1].rect)
					self.screen.blit(self.playerboards[1].playertext, ((self.width/2) - (self.title.get_rect().width/2), (1/20)*self.height))
				elif playerView == 3:
					self.screen.blit(self.playerboards[2].image, self.playerboards[2].rect)
					self.screen.blit(self.playerboards[2].playertext, ((self.width/2) - (self.title.get_rect().width/2), (1/20)*self.height))
				elif playerView == 4:
					self.screen.blit(self.playerboards[3].image, self.playerboards[3].rect)
					self.screen.blit(self.playerboards[3].playertext, ((self.width/2) - (self.title.get_rect().width/2), (1/20)*self.height))
				elif playerView == 5:
					self.screen.blit(self.playerboards[4].image, self.playerboards[4].rect)
					self.screen.blit(self.playerboards[4].playertext, ((self.width/2) - (self.title.get_rect().width/2), (1/20)*self.height))

			pygame.display.flip()

	def turnOrder(self, players):
		myorder = sample(range(len(players)), k=len(players))
		self.players = [self.players[i] for i in myorder]


if __name__ == '__main__':
	gs = GameSpace()
	gs.main()
