#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      RedSpiderMkV
#
# Created:     10/06/2014
# Copyright:   (c) RedSpiderMkV 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import json

class StockDataFromJson(object):
    def __init__(self, jObject):
        self.__dict__ = json.loads(jObject)