from stock import Stock
from yahoo_fin import stock_info
import yfinance as yf
import warnings
warnings.filterwarnings("ignore")

portfolio =[]

def addStock(name,ticker,sector,num0fShares):
    price = round(float(stock_info.get_live_price(ticker)),2)
    newStock = Stock(name,ticker,sector,price,num0fShares)
    portfolio.append(newStock)

    
def viewPortfolio():
    print("{0:20s}{1:10s}{2:35s}{3:14s}{4:6s}{5:10s}".format("Name of Stock","Ticker","Industry","Price","QTY","Gain/Loss"))
    count =1
    for stock in portfolio:
        print(f"{count}. {stock.name:{17}}{stock.ticker:{10}}{stock.sector:{35}}${stock.currentPrice:{6}}{stock.numOfShares:{9}}")
        count+=1

def searchBySector(sector):
    print("\nStocks in the sector: " + sector)
    print("{0:20s}{1:10s}{2:35s}{3:14s}{4:6s}{5:10s}".format("Name of Stock", "Ticker", "Industry", "Price", "QTY", "Gain/Loss"))
    count = 1
    for stock in portfolio:
        if stock.sector.lower() == sector.lower():
            print(f"{count}. {stock.name:{17}}{stock.ticker:{10}}{stock.sector:{35}}${stock.currentPrice:{6}}{stock.num0fShares:{9}}")
            count += 1

def updatePrices():
    for stock in portfolio:
        try:
            new_price = round(float(stock_info.get_live_price(stock.ticker)), 2)
            stock.updatePrice(new_price)
        except Exception as e:
            print(f"Error updating price for {stock.name} ({stock.ticker}): {e}")

def mainMenu():
    print("\nMain Menu")
    print("1. Add a new stock to the portfolio")
    print("2. Update stock Prices")
    print("3. Search by Sector")
    print("4. View protfolio")
    print("5. Exit program")

print("welcome to my stock protfolio")

status =True

while(status):
    mainMenu()
    choice=input("Select from the following options:")
    if choice=="1":
        name =input("Enter the Name of the Stock: ")
        ticker = input("Enter the stock ticker name: ")
        tick = yf.Ticker(ticker).info
        sector=tick['industry']
        num0fShares= int(input("Enter number of stock shares to buy: "))
        addStock(name,ticker,sector,num0fShares)
    elif choice =="2":
        updatePrices()
        viewPortfolio()
    elif choice == "3":
        sector = input("Enter the sector you want to search for: ")
        searchBySector(sector)
    elif choice =="4":
        viewPortfolio()
    elif choice =="5":
        status =False
print("Thanks for using my stock portfolio program. Have a nice day")

