# Brian Mann
# Puerto Rico
# Core Gameplay
# 2/23/2018

import sys, math, os, random
from random import sample

class Player():
	def __init__(self, pn, numPlayers):
		self.pn = pn
		self.buildingSpaces = 12
		self.islandSpaces = 12
		self.victoryPoints = 0
		if numPlayers == 3:
			self.doubloons = 2
		elif numPlayers == 4:
			self.doubloons = 3
		else:
			self.doubloons = 4

if __name__ == '__main__':
	def main(self):

		# game constants
		self.gameOver = False
		self.input = ""
		self.player = Player(1, 3)

		while self.gameOver == False:
			command = input()
			print(command)
