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

import YahooApi
from YahooApi_Symbols import *

def main():
    financeApi = YahooApi.yahooFinance()
    stockList = ('MSFT', 'AAPL', 'GOOG', 'BARC.L')
    symbolList = (SymbolInfo.Symbol, SymbolInfo.StockExchange, SymbolInfo.Name, Pricing.Ask, Pricing.Bid, Averages.LastTradeWithTime)

    print(financeApi.GetData(stockList, symbolList))

if __name__ == '__main__':
    main()
