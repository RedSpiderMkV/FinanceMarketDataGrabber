#-------------------------------------------------------------------------------
# Name:        ..
# Purpose:
#
# Author:      RedSpiderMkV
#
# Created:     15/10/2015
# Copyright:   (c) RedSpiderMkV 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import YahooFinance.YahooApi as YahooApi
from YahooFinance.YahooApi_Symbols import *

import GoogleFinance.GoogleApi as GoogleApi
from GoogleFinance.GoogleApi_Symbols import *

def main():
    financeApi = YahooApi.yahooFinance()
    stockList = ('MSFT', 'AAPL', 'GOOG', 'BARC.L')
    #stockList = ('EURUSD=X', 'GBPUSD=X', 'EURGBP=X')
    symbolList = (SymbolInfo.Symbol, SymbolInfo.StockExchange, SymbolInfo.Name, \
    Pricing.Ask, Pricing.Bid, Pricing.LastTradeWithTime)

    print(financeApi.GetData(stockList, symbolList))
    
    api = GoogleApi.GoogleFinanceApi()

    stockList = ['MSFT', 'AAPL', 'BARC.L']
    symbolList = [Symbols.ID, Symbols.Index, Symbols.StockSymbol, Symbols.LastTradePrice]
    print api.GetStockData(stockList, symbolList)

if __name__ == '__main__':
    main()