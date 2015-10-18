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

stockList = ('MSFT', 'AAPL', 'BARC.L')
#stockList = ('EURUSD=X', 'GBPUSD=X', 'EURGBP=X')

def printLines(lst):
    for line in lst:
        print(line)

def printYahooQuotes():
    financeApi = YahooApi.yahooFinance()
    symbolList = (SymbolInfo.Symbol, SymbolInfo.StockExchange, SymbolInfo.Name, \
    Pricing.Ask, Pricing.Bid, Pricing.LastTradeWithTime)

    print(financeApi.GetData(stockList, symbolList))

def printGoogleQuotes():
    api = GoogleApi.GoogleFinanceApi()

    symbolList = [Symbols.ID, Symbols.Index, Symbols.StockSymbol, Symbols.LastTradePrice]
    print(api.GetStockData(stockList, symbolList))

def printHistoricQuotesGoogle():
    data = HistoricalQuote_GoogleAPI.HistoricalQuote()
    printLines(data.GetData('NASDAQ:AAPL', '6-18-2014', '6-19-2014'))

def printHistoricQuotesYahoo():
    data = HistoricalQuote_YahooAPI.HistoricalQuote()
    printLines(data.GetData('AAPL', '6-18-14', '6-19-14'))

def main():
    #printYahooQuotes()
    #printGoogleQuotes()
    printHistoricQuotesYahoo()
    printHistoricQuotesGoogle()

if __name__ == '__main__':
    main()