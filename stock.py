class Stock:
    def __init__(self, name, ticker, sector, originalPrice, numOfShares):
        self.name = name
        self.ticker = ticker
        self.sector = sector
        self.originalPrice = originalPrice
        self.numOfShares = numOfShares
        self.currentPrice = originalPrice

    def updatePrice(self, updateValue):
        self.currentPrice = updateValue

