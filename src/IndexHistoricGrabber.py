#!/usr/bin/python

#-------------------------------------------------------------------------------
# Name:        ..
# Purpose:
#
# Author:      RedSpiderMkV
#
# Created:     11/11/2016
# Copyright:   (c) RedSpiderMkV 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import HistoricDataLib.HistoricalQuote_YahooAPI as HistoricalQuote_YahooAPI

import os
import sys

def printLines(lst, fileName):
    with open(fileName, 'w') as f:
        
        for line in lst:
            parts = line.split(',')
            
            p = ''
            for part in parts:
                p = p + part.ljust(8) + '\t'
            
            f.write(p + '\n')

def main():
    if(len(sys.argv) != 2):
        print('Index missing')
        return
        
    quoteAgent = HistoricalQuote_YahooAPI.HistoricalQuote()
    
    index = sys.argv[1].upper()
    
    dirName = "HistoricData/" + index
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    
    for year in range(2000, 2017):
        startDate = '01-01-{0}'.format(year)
        endDate = '12-31-{0}'.format(year)
        quoteData = quoteAgent.GetData('^' + index, startDate, endDate)

        printLines(quoteData, 'HistoricData/{0}/{0}_{1}.csv'.format(index, year))

if __name__ == '__main__':
    main()
