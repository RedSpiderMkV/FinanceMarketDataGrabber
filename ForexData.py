
import YahooApi
from YahooApi_Symbols import *
from ForexDataModel import ForexDataModel

class ForexData:
	def __init__(self, stockList):
		self.stockList = stockList
		
		self.symbolList = (SymbolInfo.Symbol, SymbolInfo.Name, Pricing.Ask, Pricing.Bid, Pricing.Open, Pricing.PreviousClose, Pricing.LastTradeWithTime)
		
	def GetData(self):
		financeApi = YahooApi.yahooFinance()
		forexData = financeApi.GetData(self.stockList, self.symbolList)
		
		index = 0
		forexDataList = []
		for line in forexData.split('\n'):
			forexDataList.append(ForexDataModel(line))
			
			
