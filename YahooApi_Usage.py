#-------------------------------------------------------------------------------
# Name:        YahooApi_Usage
# Purpose:
#
# Author:      RedSpiderMkV
#
# Created:     02/06/2014
# Copyright:   (c) RedSpiderMkV 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import YahooApi
from YahooApi_Symbols import *

def main():
    financeApi = YahooApi.yahooFinance()
    stockList = ('MSFT', 'AAPL', 'GOOG', 'BARC.L')
    #stockList = ('EURUSD=X', 'GBPUSD=X', 'EURGBP=X')
    symbolList = (SymbolInfo.Symbol, SymbolInfo.StockExchange, SymbolInfo.Name, \
    Pricing.Ask, Pricing.Bid, Pricing.LastTradeWithTime)

    print(financeApi.GetData(stockList, symbolList))

if __name__ == '__main__':
    main()
