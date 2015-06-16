
from ForexData import ForexData

def main():
	stockList = ('USDJPY=X', 'GBPUSD=X', 'EURUSD=X', 'EURJPY=X', 'GBPJPY=X', 'USDCAD=X', 'USDCHF=X')
	forexData = ForexData(stockList)

	forexData.GetData()

if __name__ == '__main__':
    main()
