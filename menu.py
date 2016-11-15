class Menu(object):
    """Cardapio"""

    def __init__(self):
        self.drinks = {}
        self.nmrDrinks = 0

    def __repr__(self):
        return "Drinks:\n%s \n\nNmrDrinks: %d" % (self.drinks, self.nmrDrinks)

    def addItem(self, item):
        if not self.drinks:
            self.drinks[self.nmrDrinks] = {}
            self.drinks[self.nmrDrinks]['name'] = item
            self.drinks[self.nmrDrinks]['shots'] = 0
            self.nmrDrinks += 1
        else:
            for items in self.drinks.values():
                if item in items.values():
                    print "Item, %s, already in the menu" % (item)
                    return
            self.drinks[self.nmrDrinks] = {}
            self.drinks[self.nmrDrinks]['name'] = item
            self.drinks[self.nmrDrinks]['shots'] = 0
            self.nmrDrinks += 1

    def removeItem(self, idx):
        if idx in self.drinks.keys():
            del self.drinks[idx]
        else:
            return "Item not in the menu"

    def getItem(self, idx):
        if idx in self.drinks.keys():
            return self.drinks[idx]
        else:
            return "Item not in the menu"

    def addShot(self, idx):
        if idx in self.drinks.keys():
            self.drinks[idx]['shots'] += 1
        else:
            return "Item not in the menu"

    def getShots(self):
        d = self.drinks
        nmrShots = 0

        for key in d.keys():
            nmrShots += d[key]['shots']

        return nmrShots

    def getDrinks(self):
        return self.drinks

    def getNmrDrinks(self):
        return self.nmrDrinks

    def getCardapio(self):
        for i in range(0, self.nmrDrinks):
            print "Cod: %d - Nome: %s - Doses: %d" % (i, self.drinks[i]['name'], self.drinks[i]['shots'])
