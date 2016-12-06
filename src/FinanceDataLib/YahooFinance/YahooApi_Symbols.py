#-------------------------------------------------------------------------------
# Name:        YahooApi_Symbols
# Purpose:
#
# Author:      RedSpiderMkV
#
# Created:     05/06/2014
# Copyright:   (c) RedSpiderMkV 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Pricing:
    Ask = 'a'
    Bid = 'b'
    Ask_realTime = 'b2'
    Bid_realTime = 'b3'
    PreviousClose = 'p'
    Open = 'o'
    LastTrade = 'l1'
    LastTradeWithTime = 'l'

class Dividends:
    DividendYield = 'y'
    DividendPerShare = 'd'
    DividendPayDate = 'r1'
    ExDividendDate = 'q'

class Date:
    Change = 'c1'
    ChangeAndPercentChange = 'c'
    Change_realtTime = 'c6'
    ChangePercent_realTime = 'k2'
    ChangeInPercent = 'p2'
    LastTradeDate = 'd1'
    TradeDate = 'd2'
    LastTradeTime = 't1'

class Averages:
    AfterHoursChange_realTime = 'c8'
    Commission = 'c3'
    DayHigh = 'h'
    DayLow = 'g'
    OneYearTargetPrice = 't8'
    Delta200DayMA = 'm5'
    PercentDelta200DayMA = 'm6'
    Delta50DayMA = 'm7'
    PercentDelta50DayMA = 'm8'
    MovingAverage50 = 'm3'
    MovingAverage200 = 'm4'

class SymbolInfo:
    MoreInfo = 'v'
    MarketCapitalisation = 'j1'
    MarketCap_realTime = 'j3'
    FloatShares = 'f6'
    Name = 'n'
    Notes = 'n4'
    Symbol = 's'
    SharesOwned = 's1'
    StockExchange = 'x'
    SharesOutstanding = 'j2'

class Misc:
    DayValueChange = 'w1'
    DayValueChange_realTime = 'w4'
    PricePaid = 'p1'
    DayRange = 'm'
    DayRane_realTime = 'm2'
    HoldingsGainPercent = 'g1'
    AnnualisedGain = 'g3'
    HoldingsGain = 'g4'
    HoldingsGainPercent_realTime = 'g5'
    HoldingsGain_realTime = 'g6'

class Volume:
    Volume = 'v'
    AskSize = 'a5'
    BidSize = 'b6'
    LastTradeSize = 'k3'
    AveDailyVolume = 'a2'
