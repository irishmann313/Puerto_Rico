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
		self.size = self.width, self.height = 1366, 768
		self.black = 255, 255, 255

		self.screen = pygame.display.set_mode(self.size)#, pygame.FULLSCREEN)
		self.clock = pygame.time.Clock()

		self.gameOver = False
		self.quit = False

		self.title = "Puerto Rico"

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
			self.screen.blit(pygame.font.SysFont('mono', 36, bold=True).render(str(self.title), True, (100, 100, 200)), ((self.width/2.5), 30))
			self.screen.blit(pygame.font.SysFont('mono', 24, bold=True).render(str(self.menu.l2), True, (150,150,255)), ((self.width/5), 85))
			self.screen.blit(pygame.font.SysFont('mono', 32, bold=True).render(str(self.menu.l3), True, (150,150,255)), ((self.width/2.75), (self.height-70)))

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

		# Sprites that will be clicked
		self.settler = RoleCard("settler", self)
		sprite_list.append(self.settler)
		self.mayor = RoleCard("mayor", self)
		sprite_list.append(self.mayor)
		self.builder = RoleCard("builder", self)
		sprite_list.append(self.builder)
		self.craftsman = RoleCard("craftsman", self)
		sprite_list.append(self.craftsman)
		self.trader = RoleCard("trader", self)
		sprite_list.append(self.trader)
		self.captain = RoleCard("captain", self)
		sprite_list.append(self.captain)
		self.smallindigoplant = SmallIndigoPlant(self)
		sprite_list.append(self.smallindigoplant)
		self.smallsugarmill = SmallSugarMill(self)
		sprite_list.append(self.smallsugarmill)
		self.smallmarket = SmallMarket(self)
		sprite_list.append(self.smallmarket)
		self.hacienda = Hacienda(self)
		sprite_list.append(self.hacienda)
		self.constructionhut = ConstructionHut(self)
		sprite_list.append(self.constructionhut)
		self.smallwarehouse = SmallWarehouse(self)
		sprite_list.append(self.smallwarehouse)
		self.indigoplant = IndigoPlant(self)
		sprite_list.append(self.indigoplant)
		self.sugarmill = SugarMill(self)
		sprite_list.append(self.sugarmill)
		self.hospice = Hospice(self)
		sprite_list.append(self.hospice)
		self.office = Office(self)
		sprite_list.append(self.office)
		self.largemarket = LargeMarket(self)
		sprite_list.append(self.largemarket)
		self.largewarehouse = LargeWarehouse(self)
		sprite_list.append(self.largewarehouse)
		self.tobaccostorage = TobaccoStorage(self)
		sprite_list.append(self.tobaccostorage)
		self.coffeeroaster = CoffeeRoaster(self)
		sprite_list.append(self.coffeeroaster)
		self.university = University(self)
		sprite_list.append(self.university)
		self.factory = Factory(self)
		sprite_list.append(self.factory)
		self.harbor = Harbor(self)
		sprite_list.append(self.harbor)
		self.wharf = Wharf(self)
		sprite_list.append(self.wharf)
		self.guildhall = GuildHall(self)
		sprite_list.append(self.guildhall)
		self.residence = Residence(self)
		sprite_list.append(self.residence)
		self.fortress = Fortress(self)
		sprite_list.append(self.fortress)
		self.customshouse = CustomsHouse(self)
		sprite_list.append(self.customshouse)
		self.cityhall = CityHall(self)
		sprite_list.append(self.cityhall)

		print(len(sprite_list))

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
			self.prospector1 = RoleCard("prospector", self)
			self.prospector2 = None
			self.numPiles = 5
			self.doubloons = 74
		else:
			self.vpoints = 122
			self.colonists = 95
			self.cargo1 = CargoShip(6, 1, self)
			self.cargo2 = CargoShip(7, 2, self)
			self.cargo3 = CargoShip(8, 3, self)
			self.prospector1 = RoleCard("prospector", self)
			self.prospector2 = RoleCard("prospector", self)
			self.numPiles = 6
			self.doubloons = 66

		self.turnOrder(self.players)

		# main game loop
		while self.quit == False:
			self.clock.tick(60)


			# handle input
			for event in pygame.event.get():
				if event.type == QUIT:
					sys.exit()
				elif event.type == KEYDOWN:
					if event.key == pygame.K_q:
						sys.exit()
				elif event.type == MOUSEBUTTONUP:
					print("clicked")

			# tick objects

			# display objects
			self.screen.fill(self.black)
			self.screen.blit(self.buildingboard.image, self.buildingboard.rect)
			self.screen.blit(self.tradinghouse.image, self.tradinghouse.rect)
			self.screen.blit(self.colonistship.image, self.colonistship.rect)
			self.screen.blit(self.cargo1.image, self.cargo1.rect)
			self.screen.blit(self.cargo2.image, self.cargo2.rect)
			self.screen.blit(self.cargo3.image, self.cargo3.rect)
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

			pygame.display.flip()

	def turnOrder(self, players):
		myorder = sample(range(len(players)), k=len(players))
		self.players = [self.players[i] for i in myorder]


if __name__ == '__main__':
	gs = GameSpace()
	gs.main()
