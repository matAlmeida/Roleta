class Player(object):
    """Jogador"""

    def __init__(self, name):
        self.name = name
        self.drinks = {}

    def __repr__(self):
        return "Name: %s\nNmrDrinks: %d\nDrinks:\n%s" % (self.name, self.getShots(), self.drinks)

    def addShot(self, idx):
        if idx in self.drinks.keys():
            self.drinks[idx] += 1
        else:
            self.drinks[idx] = 1

    def getName(self):
        return self.name

    def getShots(self):
        d = self.drinks
        nmrShots = 0

        for key in d.keys():
            nmrShots += d[key]

        return nmrShots

    def getDrinks(self):
        return self.drinks
