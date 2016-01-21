# -*- coding: utf-8 -*-
#
# Author:      RedSpiderMkV
#
# Created:     20/06/2014
# Copyright:   (c) RedSpiderMkV 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib2
from HistoricalQuote_Base import HistoricalQuoteBase

class HistoricalQuote(HistoricalQuoteBase):
    def __init__(self):
        self.url = ('http://www.google.co.uk/finance/historical?'
                    'q={0}&startdate={1}&enddate={2}&output=csv')

    def GetData(self, symbol, sDate, eDate):
        startDate = sDate.replace('-','+')
        endDate = eDate.replace('-', '+')

        try:
            url = str.format(self.url, symbol, startDate, endDate)
            request = (urllib2.urlopen(url)).read().strip()
        except Exception as e:
            print(e)
            return ""

        request = unicode(request, 'utf-8-sig')
        return self.FormatList(request)
