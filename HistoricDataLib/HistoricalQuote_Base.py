# -*- coding: utf-8 -*-
#
# Author:      RedSpiderMkV
#
# Created:     20/06/2014
# Copyright:   (c) RedSpiderMkV 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class HistoricalQuoteBase:
    
    def FormatList(self, results):
    
        resultsList = results.split('\n')[::-1]
        resultsList.insert(0, resultsList[len(resultsList) - 1])
        resultsList = resultsList[0:len(resultsList) - 1]
        
        return resultsList