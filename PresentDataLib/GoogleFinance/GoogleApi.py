#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      RedSpiderMkV
#
# Created:     08/06/2014
# Copyright:   (c) RedSpiderMkV 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib2
import Google_JsonBuilder
from GoogleApi_Symbols import *

class GoogleFinanceApi:
    def __init__(self):
        self.url = r'http://finance.google.com/finance/info?q={0}'

    def __buildUrl(self, symbolString):
        return str.format(self.url, symbolString)

    def __buildSymbolString(self, stockList):
        symbols = ''
        for symbol in stockList:
            symbols += symbol + ','

        return symbols[:-1]

    def __buildStockInfoStr(self, stockObject, symbolList):
        stockInfoStr = ''

        for stockOb in stockObject.jsonObjects:
            if Symbols.Dividend in symbolList:
                stockInfoStr += stockOb.div + ' '
            if Symbols.ID in symbolList:
                stockInfoStr += stockOb.id + ' '
            if Symbols.Index in symbolList:
                stockInfoStr += stockOb.e + ' '
            if Symbols.LastTradeDateTime in symbolList:
                stockInfoStr += stockOb.lt_dts + ' '
            if Symbols.LastTradeDateTimeLong in symbolList:
                stockInfoStr += stockOb.lt + ' '
            if Symbols.LastTradePrice in symbolList:
                stockInfoStr += stockOb.l + ' '
            if Symbols.LastTradeTime in symbolList:
                stockInfoStr += stockOb.ltt + ' '
            if Symbols.LastTradeWithCurrency in symbolList:
                stockInfoStr += stockOb.l_cur + ' '
            if Symbols.StockSymbol in symbolList:
                stockInfoStr += stockOb.t + ' '
            if Symbols.Yield in symbolList:
                stockInfoStr += stockOb.yld + ' '

            stockInfoStr += '\n'

        return stockInfoStr

    def GetStockData(self, stockList, symbolList):
        symbolString = self.__buildSymbolString(stockList)
        apiUrl = self.__buildUrl(symbolString)

        response = ''

        try:
            request = urllib2.urlopen(apiUrl)
            response = request.read()[3:-1].strip()
            request.close()
        except Exception as e:
            print(e)

        stockObject = Google_JsonBuilder.StocksFromGoogle(response)
        stockInfoStr = self.__buildStockInfoStr(stockObject, symbolList)

        return stockInfoStr
