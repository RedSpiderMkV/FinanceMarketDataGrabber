
from ForexData import ForexData

def main():
	stockList = ('USDJPY=X', 'GBPUSD=X', 'EURUSD=X', 'EURJPY=X', 'GBPJPY=X', 'USDCAD=X', 'USDCHF=X')
	forexData = ForexData(stockList)

	forexData.SetData()
	
	printStr = forexData.Symbol + " " + forexData.Name + " " + forexData.Bid + " " + forexData.Ask + " " + forexData.Open + " " \
	+ forexData.PreviousClose + " " + forexData.LastTradeWithTime
	
	print(printStr)

if __name__ == '__main__':
    main()
