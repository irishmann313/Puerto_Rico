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

class RoleCard():
    def __init__(self, role):
        self.role = role
        self.doubloons = 0
        self.available = True

    def clicked(self):
        self.available = False
        self.doubloons = 0
        
    def cleanup(self):
        if self.available:
            self.doubloons += 1
        else:
            self.available = True

def turnOrder(players):
    myorder = sample(range(len(players)), k=len(players))
    return [players[i] for i in myorder]

if __name__ == '__main__':

    # get number of players
    print "How many players?"
    numPlayers = int(raw_input())

    # game constants
    gameOver = False
    command = ""
    turnPointer = 0
    # generate players
    players = []
    playerOne = Player(1, numPlayers)
    players.append(playerOne)
    playerTwo = Player(2, numPlayers)
    players.append(playerTwo)
    playerThree = Player(3, numPlayers)
    players.append(playerThree)
    if numPlayers >= 4:
        playerFour = Player(4, numPlayers)
        players.append(playerFour)
    if numPlayers == 5:
        playerFive = Playe(5, numPlayers)
        players.append(playerFive)
    players = turnOrder(players)

    # generate role cards
    roleCards = []
    builder = RoleCard("builder")
    roleCards.append(builder)
    captain = RoleCard("captain")
    roleCards.append(captain)
    craftsman = RoleCard("craftsman")
    roleCards.append(craftsman)
    mayor = RoleCard("mayor")
    roleCards.append(mayor)
    settler = RoleCard("settler")
    roleCards.append(settler)
    trader = RoleCard("trader")
    roleCards.append(trader)
    if numPlayers >=4:
        prospector1 = RoleCard("prospector")
        roleCards.append(prospector1)
    if numPlayers == 5:
        prospector2 = RoleCard("prospector")
        roleCards.append(prospector2)

    while gameOver == False:
        for player in players:
            print str(player.pn) + ": " +  str(player.doubloons)
        for role in roleCards:
            if role.available:
                print role.role + ": " + str(role.doubloons)
        print "What you doin'?"
        command = raw_input()
        if command == "rage quit":
            gameOver = True
        elif command == "builder":
            if builder.available:
                players[turnPointer].doubloons += builder.doubloons
                builder.clicked()
                turnPointer += 1
            else:
                print "Builder has already been taken"
        elif command == "captain":
            if captain.available:
                players[turnPointer].doubloons += captain.doubloons
                captain.clicked()
                turnPointer += 1
            else:
                print "Captain has already been taken"
        elif command == "craftsman":
            if craftsman.available:
                players[turnPointer].doubloons += craftsman.doubloons
                craftsman.clicked()
                turnPointer += 1
            else:
                print "Craftsman has already been taken"
        elif command == "mayor":
            if mayor.available:
                players[turnPointer].doubloons += mayor.doubloons
                mayor.clicked()
                turnPointer += 1
            else:
                print "Mayor has already been taken"
        elif command == "settler":
            if settler.available:
                players[turnPointer].doubloons += settler.doubloons
                settler.clicked()
                turnPointer += 1
            else:
                print "Settler has already been taken"
        elif command == "trader":
            if trader.available:
                players[turnPointer].doubloons += trader.doubloons
                trader.clicked()
                turnPointer += 1
            else:
                print "Trader has already been taken"
        elif command == "prospector":
            if prospector1.available:
                players[turnPointer].doubloons += prospector1.doubloons
                prospector1.clicked()
                turnPointer += 1
            elif prospector2.available:
                players[turnPointer].doubloons += prospector2.doubloons
                prospector2.clicked()
                turnPointer += 1
            else:
                print "Prospector has already been taken"
        else:
            print "Bad input"
        if turnPointer >= numPlayers:
            for role in roleCards:
                role.cleanup()
            turnPointer = 0
