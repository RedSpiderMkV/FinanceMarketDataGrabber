#-------------------------------------------------------------------------------
# Name:        GoogleHistoricalQuote_Usage
# Purpose:     Retrieve historical stock data from Google/Yahoo finance API.
#              Quick test, still need to separate into Google/Yahoo section
#              and separate usage from 'library' functions.
#
# Author:      RedSpiderMkV
#
# Created:     20/06/2014
# Copyright:   (c) RedSpiderMkV 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import HistoricalQuote_GoogleAPI
import HistoricalQuote_YahooAPI

def printLines(lst):
    for line in lst:
        print line

def main():

    data = HistoricalQuote_GoogleAPI.HistoricalQuote()
    printLines(data.GetData('NASDAQ:AAPL', '6-18-2014', '6-19-2014'))

    print ''    
    
    data = HistoricalQuote_YahooAPI.HistoricalQuote()
    printLines(data.GetData('AAPL', '6-18-14', '6-19-14'))    

if __name__ == '__main__':
    main()
