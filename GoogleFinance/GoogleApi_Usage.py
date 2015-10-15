#-------------------------------------------------------------------------------
# Name:        GoogleApi_Usage
# Purpose:     Using the Google API to retrieve data
#              for stocks, provided in a list variable.
#
# Author:      RedSpiderMkV
#
# Created:     08/06/2014
# Copyright:   (c) RedSpiderMkV 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import GoogleApi
from GoogleApi_Symbols import *

def main():
    api = GoogleApi.GoogleFinanceApi()

    stockList = ['MSFT', 'AAPL', 'BARC.L']
    symbolList = [Symbols.ID, Symbols.Index, Symbols.StockSymbol, Symbols.LastTradePrice]
    print api.GetStockData(stockList, symbolList)

if __name__ == '__main__':
    main()