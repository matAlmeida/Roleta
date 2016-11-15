from player import Player
from menu import Menu
from random import randint

class Game(object):
    """Partida"""

    def __init__(self):
        self.name = "Game 1"
        self.menu = Menu()
        self.players = {}
        self.nmrPlayers = 0

    def addItem(self, item):
        self.menu.addItem(item)

    def addPlayer(self, name):
        self.players[self.nmrPlayers] = Player(name)
        self.nmrPlayers += 1

    def play(self, idxPlayer):
        if self.menu.getNmrDrinks() != 0:
            magic = randint(0,self.menu.getNmrDrinks() - 1)
            self.players[idxPlayer].addShot(magic)
            self.menu.addShot(magic)
            print "\n%s bebe uma dose de %s pela %d vez." % (self.players[idxPlayer].getName(), self.menu.getItem(magic)['name'], self.players[idxPlayer].getDrinks()[magic])
        else:
            return "Menu is empty!!!"

    def getPlayers(self):
        for key in self.players.keys():
            print "Cod: %d - Nome: %s - Doses: %d" % (key, self.players[key].getName(), self.players[key].getShots())

    def getCardapio(self):
        return self.menu.getCardapio()
