# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
#   Module:
#   Created on: Sun Jun 22 13:16:28 2014
#
#   Author:     RedSpiderMkV
#
#   Copyright:  (c) RedSpiderMkV 2014
#   Licence:    <your licence>
#----------------------------------------------------------------------------

import urllib2
from HistoricalQuote_Base import HistoricalQuoteBase

class HistoricalQuote(HistoricalQuoteBase):
    def __init__(self):
        self.url = ('http://real-chart.finance.yahoo.com/table.csv?'
                    's={0}&d={1}&e={2}&f={3}&g=d&a={4}&b={5}&c={6}&ignore=.csv')

    def GetData(self, symbol, sDate, eDate):
        startDate = sDate.split('-')
        endDate = eDate.split('-')

        endDate[0] = str(int(endDate[0]) - 1)
        startDate[0] = str(int(startDate[0]) - 1)

        request = ''

        try:
            request = urllib2.urlopen(str.format(self.url, symbol,
            endDate[0], endDate[1], endDate[2],
            startDate[0], startDate[1], startDate[2])).read().strip()
        except Exception as e:
            print(e)

        return self.FormatList(request)
