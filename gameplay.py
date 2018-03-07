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
        self.quarries = 0
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
    numPlayers = 0
    while numPlayers < 3 or numPlayers > 5:
        print "How many players? (Must be between 3 and 5)"
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
        playerFive = Player(5, numPlayers)
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
        print "Player " + str(players[turnPointer].pn) + "'s Turn!"
        for player in players:
            print str(player.pn) + ": " +  str(player.doubloons)
        for role in roleCards:
            if role.available:
                print role.role + ": " + str(role.doubloons)
        command = raw_input().lower()
        if command == "rage quit":
            gameOver = True
        elif command == "builder":
            if builder.available:
                players[turnPointer].doubloons += builder.doubloons
                players[turnPointer].doubloons += 1
                bonusPlayer = players[turnPointer].pn
                builder.clicked()
                turnPointer += 1
                for player in players:
                    print "Player " + str(player.pn) + ", do you want to build?"
                    answer = raw_input().lower()
                    while answer is not "next":
                        if (answer == "yes"):
                            print "You have " + str((player.doubloons + player.quarries)) + " doubloons available; what would you like to purchase?"
                            answer = raw_input().lower()
                            if (answer == "cancel"):
                                answer = "next"
                            elif (answer == "city hall"):
                                if (player.doubloons + player.quarries) < 10:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 10
                                    print "You bought a " + answer
                                    answer = "next"
                            elif (answer == "coffee roaster"):
                                if (player.doubloons + player.quarries) < 6:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 6
                                    print "You bought a " + answer
                                    answer = "next"
                            elif (answer == "construction hut"):
                                if (player.doubloons + player.quarries) < 2:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 2
                                    print "You bought a " + answer
                                    answer = "next"
                            elif (answer == "customs house"):
                                if (player.doubloons + player.quarries) < 10:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 10
                                    print "You bought a " + answer
                                    answer = "next"
                            elif (answer == "factory"):
                                if (player.doubloons + player.quarries) < 8:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 8
                                    print "You bought a " + answer
                                    answer = "next"
                            elif (answer == "fortress"):
                                if (player.doubloons + player.quarries) < 10:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 10
                                    print "You bought a " + answer
                                    answer = "next"
                            elif (answer == "guild hall"):
                                if (player.doubloons + player.quarries) < 10:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 10
                                    print "You bought a " + answer
                            elif (answer == "hacienda"):
                                if (player.doubloons + player.quarries) < 2:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 2
                                    print "You bought a " + answer
                                    answer = "next"
                            elif (answer == "harbor"):
                                if (player.doubloons + player.quarries) < 8:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 8
                                    print "You bought a " + answer
                                    answer = "next"
                            elif (answer == "hospice"):
                                if (player.doubloons + player.quarries) < 4:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 4
                                    print "You bought a " + answer
                                    answer = "next"
                            elif (answer == "indigo plant"):
                                if (player.doubloons + player.quarries) < 3:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 3
                                    print "You bought a " + answer
                                    answer = "next"
                            elif (answer == "large market"):
                                if (player.doubloons + player.quarries) < 5:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 5
                                    print "You bought a " + answer
                                    answer = "next"
                            elif (answer == "large warehouse"):
                                if (player.doubloons + player.quarries) < 6:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 6
                                    print "You bought a " + answer
                                    answer = "next"
                            elif (answer == "office"):
                                if (player.doubloons + player.quarries) < 5:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 5
                                    print "You bought a " + answer
                                    answer = "next"
                            elif (answer == "residence"):
                                if (player.doubloons + player.quarries) < 10:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 10
                                    print "You bought a " + answer
                                    answer = "next"
                            elif (answer == "small indigo plant"):
                                if (player.doubloons + player.quarries) < 1:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 1
                                    print "You bought a " + answer
                                    answer = "next"
                            elif (answer == "small market"):
                                if (player.doubloons + player.quarries) < 1:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 1
                                    print "You bought a " + answer
                                    answer = "next"
                            elif (answer == "small sugar mill"):
                                if (player.doubloons + player.quarries) < 2:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 2
                                    print "You bought a " + answer
                                    answer = "next"
                            elif (answer == "small warehouse"):
                                if (player.doubloons + player.quarries) < 3:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 3
                                    print "You bought a " + answer
                                    answer = "next"
                            elif (answer == "sugar mill"):
                                if (player.doubloons + player.quarries) < 4:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 4
                                    print "You bought a " + answer
                                    answer = "next"
                            elif (answer == "tobacco storage"):
                                if (player.doubloons + player.quarries) < 5:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 5
                                    print "You bought a " + answer
                                    answer = "next"
                            elif (answer == "university"):
                                if (player.doubloons + player.quarries) < 7:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 7
                                    print "You bought a " + answer
                                    answer = "next"
                            elif (answer == "wharf"):
                                if (player.doubloons + player.quarries) < 9:
                                    print "You don't have enough money to buy a " + answer
                                    print "Would you still like to build?"
                                    answer = raw_input().lower()
                                else:
                                    player.doubloons -= 9
                                    print "You bought a " + answer
                                    answer = "next"
                            else:
                                print "Bad input; do you still want to build?"
                                answer = raw_input().lower()
                        elif (answer == "no"):
                            answer = "next"
                            if player.pn == bonusPlayer:
                                player.doubloons -= 1
                            continue
                        else:
                            print "Bad input; do you still want to build?"
                            answer = raw_input().lower()
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
            players.append(players.pop(0))
            turnPointer = 0
