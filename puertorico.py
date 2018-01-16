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

		self.colonistship = ColonistShip(self.numPlayers, self)
		self.tradinghouse = TradingHouse(self)
		self.settler = RoleCard("settler", self)
		self.mayor = RoleCard("mayor", self)
		self.builder = RoleCard("builder", self)
		self.craftsman = RoleCard("craftsman", self)
		self.trader = RoleCard("trader", self)
		self.captain = RoleCard("captain", self)
		self.buildingboard = BuildingBoard(self)

		if self.numPlayers == 3:
			self.vpoints = 75
			self.colonists = 55
			self.cargo1 = CargoShip(4, self)
			self.cargo2 = CargoShip(5, self)
			self.cargo3 = CargoShip(6, self)
			self.prospector1 = None
			self.prospector2 = None
			self.numPiles = 4
			self.doubloons = 80
		elif self.numPlayers == 4:
			self.vpoints = 100
			self.colonists = 75
			self.cargo1 = CargoShip(5, self)
			self.cargo2 = CargoShip(6, self)
			self.cargo3 = CargoShip(7, self)
			self.prospector1 = RoleCard("prospector", self)
			self.prospector2 = None
			self.numPiles = 5
			self.doubloons = 74
		else:
			self.vpoints = 122
			self.colonists = 95
			self.cargo1 = CargoShip(6, self)
			self.cargo2 = CargoShip(7, self)
			self.cargo3 = CargoShip(8, self)
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

			# tick objects

			# display objects
			self.screen.fill(self.black)
			self.screen.blit(self.buildingboard.image, self.buildingboard.rect)
			self.screen.blit(self.tradinghouse.image, self.tradinghouse.rect)
			self.screen.blit(self.colonistship.image, self.colonistship.rect)

			pygame.display.flip()

	def turnOrder(self, players):
		myorder = sample(range(len(players)), k=len(players))
		self.players = [self.players[i] for i in myorder]


if __name__ == '__main__':
	gs = GameSpace()
	gs.main()
