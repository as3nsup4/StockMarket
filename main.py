from stock import Stock
from yahoo_fin import stock_info
import yfinance as yf
import warnings
import os
from logo import Logo
import time
warnings.filterwarnings("ignore")

portfolio = []

def addStock(name, ticker, sector, numOfShares):
    price = round(float(stock_info.get_live_price(ticker)), 2)
    newStock = Stock(name, ticker, sector, price, numOfShares)
    portfolio.append(newStock)


def viewPortfolio():
    print("{0:20s}{1:10s}{2:35s}{3:14s}{4:6s}{5:15s}".format("Name of Stock", "Ticker", "Industry", "Price", "QTY", "Gain/Loss"))
    count = 1
    for stock in portfolio:
        gain_loss = stock.calculateGainLoss()
        gain_loss_str = f"${gain_loss:10.2f}" if gain_loss >= 0 else f"(${abs(gain_loss):9.2f}:{15}"
        print(f"{count}. {stock.name:{17}}{stock.ticker:{10}}{stock.sector:{35}}${stock.currentPrice:{6}.2f}{stock.numOfShares:{9}}{gain_loss_str:{15}}")
        count += 1


def searchBySector(sector):
    print("\nStocks in the sector: " + sector)
    print("{0:20s}{1:10s}{2:35s}{3:14s}{4:6s}{5:15s}".format("Name of Stock", "Ticker", "Industry", "Price", "QTY", "Gain/Loss"))
    count = 1
    for stock in portfolio:
        if stock.sector.lower() == sector.lower():
            gain_loss = stock.calculateGainLoss()
            gain_loss_str = f"${gain_loss:.2f}" if gain_loss >= 0 else f"(${abs(gain_loss):.2f})"
            print(f"{count}. {stock.name:{17}}{stock.ticker:{10}}{stock.sector:{35}}${stock.currentPrice:{6}.2f}{stock.numOfShares:{9}}{gain_loss_str}")
            count += 1


def updatePrices():
    for stock in portfolio:
        new_price = round(float(stock_info.get_live_price(stock.ticker)), 2)
        stock.updatePrice(new_price)


def mainMenu():
    print("\nMain Menu")
    print("1. Add a new stock to the portfolio")
    print("2. Update stock Prices")
    print("3. Search by Sector")
    print("4. View portfolio")
    print("5. Exit program")


print(Logo)
time.sleep(3)

status = True

while status:
    os.system('clear')
    mainMenu()
    choice = input("Select from the following options:")
    if choice == "1":
        print("")
        name = input("Enter the Name of the Stock: ")
        ticker = input("Enter the stock ticker name: ")
        tick = yf.Ticker(ticker).info
        sector = tick.get('industry', 'Unknown')
        numOfShares = int(input("Enter number of stock shares to buy: "))
        addStock(name, ticker, sector, numOfShares)
        print("")
    elif choice == "2":
        print("")
        updatePrices()
        viewPortfolio()
        print("")
    elif choice == "3":
        print("")
        sector = input("Enter the sector you want to search for: ")
        searchBySector(sector)
        print("")
    elif choice == "4":
        print("")
        viewPortfolio()
        print("")
    elif choice == "5":
        print("")
        status = False
    input("\nPress Enter to continue... ")

print("Thanks for using my stock portfolio program. Have a nice day")
