#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      RedSpiderMkV
#
# Created:     09/06/2014
# Copyright:   (c) RedSpiderMkV 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import Google_JsonObject

class StocksFromGoogle:
    jsonObjects = []

    def __init__(self, jsonObjList):
        objList = jsonObjList.split('}\n,')

        for o in objList:
            objectString = self.__formatJsonStr__(o)
            obj = Google_JsonObject.StockDataFromJson(objectString)
            self.jsonObjects.append(obj)

    def __formatJsonStr__(self, jsonStr):
        oStr = jsonStr[2:].strip()

        if not oStr.startswith('{'):
            oStr = '{\n' + oStr

        if oStr.endswith(']'):
            oStr = oStr[:-1]

        if not oStr.endswith('}'):
            oStr += '}'

        if oStr.endswith('}\n}'):
            oStr = oStr[:-1]

        return oStr