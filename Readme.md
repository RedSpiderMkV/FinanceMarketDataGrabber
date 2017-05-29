Finance API Library
===========

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/RedSpiderMkV/FinanceMarketDataGrabber/blob/master/LICENSE)

Python library to access current stock/forex quotes from Yahoo and Google Finance 'APIs'.  Historic data can also be retrieved.

Multiple stock quotes and multiple symbols can be retrieved in a single call, thereby reducing latency and bandwidth usage.

Usage - Yahoo Finance Live Quotes (delayed by 15 minutes by Yahoo)
------------------------------------------------------------------

To retrieve live stock data using the Yahoo Finance API, the following will be required.

```python
import FinanceDataLib.YahooFinance.YahooApi as YahooApi
from FinanceDataLib.YahooFinance.YahooApi_Symbols import *

financeApi = YahooApi.yahooFinance()
```
To retrieve stock data, provide a list of stocks of interest as well as a list symbols for each stock.

```python
stockList = ('MSFT', 'AAPL', 'BARC.L')
symbolList = (SymbolInfo.Symbol, SymbolInfo.StockExchange, SymbolInfo.Name, \
    Pricing.Ask, Pricing.Bid, Pricing.LastTradeWithTime)
    
financeApi.GetData(stockList, symbolList)
```

This will return the following response:

```
"MSFT","NMS","Microsoft Corporation",58.74,58.65,"4:00pm - <b>58.71</b>"
"AAPL","NMS","Apple Inc.",108.85,108.71,"4:00pm - <b>108.84</b>"
"BARC.L","LSE","BARCLAYS PLC ORD 25P",189.00,179.50,"5:05pm - <b>181.35</b>"
```

More examples can be found in the ```example.py``` file.

Pending
-------

More information about how to use the Google Finance API and the historical data retriever
will be provided soon.

As of 27/05/2017, the Google Finance API is still working.

Note On Yahoo Finance Historic Data
-----------------------------------

It appears Yahoo has changed their API, made it secure in such a way that simple HTTP requests no longer work.  For the time being, historic data is no longer working through Yahoo.

The Google Finance API is still working.
I'm currently looking into other data providers to retrieve historic data from.

So far the following have been found:
Dukascopy
AlphaVantage

Libraries to download data from them will be uploaded soon but will probably be in C# since I've grown weary of Python...

Neither provide crypto currency data though.
