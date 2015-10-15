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
from GoogleApi_Symbols import *

import json

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

    def __buildStockInfoStr(self, dataList, symbolList):
        stockInfoStr = ''

        for stockOb in dataList:
            for symbol in symbolList:
                stockInfoStr += stockOb[symbol] + ' '
                
            stockInfoStr += '\n'
                
        return stockInfoStr

    def GetStockData(self, stockList, symbolList):
        symbolString = self.__buildSymbolString(stockList)
        apiUrl = self.__buildUrl(symbolString)

        try:
            request = urllib2.urlopen(apiUrl)
            response = request.read()[3:-1].strip()
            request.close()
        except Exception as e:
            print(e)
            return ''

        jsonDataList = json.loads(response)
        stockInfoStr = self.__buildStockInfoStr(jsonDataList, symbolList)

        return stockInfoStr
