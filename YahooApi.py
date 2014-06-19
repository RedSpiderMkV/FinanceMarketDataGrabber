#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nikeah
#
# Created:     02/06/2014
# Copyright:   (c) Nikeah 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib2

class yahooFinance:

    def __init__(self):
        self.apiUrl = r'http://download.finance.yahoo.com/d/quotes.csv?s={0}&f={1}'

    def __formatParamList(self, paramString, separator):
        paramList = ''
        for param in paramString:
            paramList += param + separator

        return paramList[:-1]

    def __getRequest(self):
        request = urllib2.urlopen(self.apiUrl)
        response = request.read()
        request.close()

        return response

    def GetData(self, stocks, symbols):
        self.stocks = stocks
        self.symbols = symbols

        stockList = self.__formatParamList(stocks, '+')
        symbolList = self.__formatParamList(symbols, '')
        self.apiUrl = str.format(self.apiUrl, stockList, symbolList)

        return self.__getRequest().strip()