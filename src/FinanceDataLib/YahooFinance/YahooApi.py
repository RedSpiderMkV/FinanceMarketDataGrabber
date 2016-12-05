#-------------------------------------------------------------------------------
# Name:        YahooApi
# Purpose:
#
# Author:      RedSpiderMkV
#
# Created:     02/06/2014
# Copyright:   (c) RedSpiderMkV 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib2

class yahooFinance:

    def __init__(self):
        self._apiUrlTemplate = r'http://download.finance.yahoo.com/d/quotes.csv?s={0}&f={1}'

    def __formatParamList(self, paramString, separator):
        paramList = ''
        for param in paramString:
            paramList += param + separator

        return paramList[:-1]

    def __getRequest(self, url):
        response = ''

        try:
            request = urllib2.urlopen(url)
            response = request.read()
            request.close()
        except Exception as e:
            print(e)

        return response

    def GetData(self, stocks, symbols):
        stockList = self.__formatParamList(stocks, '+')
        symbolList = self.__formatParamList(symbols, '')
        apiUrl = str.format(self._apiUrlTemplate, stockList, symbolList)
        
        print apiUrl

        return self.__getRequest(apiUrl)
