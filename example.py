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

import PresentDataLib.YahooFinance.YahooApi as YahooApi
from PresentDataLib.YahooFinance.YahooApi_Symbols import *

import PresentDataLib.GoogleFinance.GoogleApi as GoogleApi
from PresentDataLib.GoogleFinance.GoogleApi_Symbols import *

import HistoricDataLib.HistoricalQuote_GoogleAPI as HistoricalQuote_GoogleAPI
import HistoricDataLib.HistoricalQuote_YahooAPI as HistoricalQuote_YahooAPI

def printLines(lst):
    for line in lst:
        print line

def main():
    financeApi = YahooApi.yahooFinance()
    stockList = ('MSFT', 'AAPL', 'GOOG', 'BARC.L')
    #stockList = ('EURUSD=X', 'GBPUSD=X', 'EURGBP=X')
    symbolList = (SymbolInfo.Symbol, SymbolInfo.StockExchange, SymbolInfo.Name, \
    Pricing.Ask, Pricing.Bid, Pricing.LastTradeWithTime)

    print(financeApi.GetData(stockList, symbolList))

    print '\n'    
    
    api = GoogleApi.GoogleFinanceApi()

    stockList = ['MSFT', 'AAPL', 'BARC.L']
    symbolList = [Symbols.ID, Symbols.Index, Symbols.StockSymbol, Symbols.LastTradePrice]
    print api.GetStockData(stockList, symbolList)
    
    data = HistoricalQuote_GoogleAPI.HistoricalQuote()
    printLines(data.GetData('NASDAQ:AAPL', '6-18-2014', '6-19-2014'))

    print ''    
    
    data = HistoricalQuote_YahooAPI.HistoricalQuote()
    printLines(data.GetData('AAPL', '6-18-14', '6-19-14'))

if __name__ == '__main__':
    main()