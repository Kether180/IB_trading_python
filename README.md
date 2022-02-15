# IB Python_api_websocket_trading

IB Python_api_websocket_trading

#  Guide to Interactive Brokers 

* Overview 

These programs can help you make the first steps towards working with the Interactive Brokers API. Interactive Brokers API can be very challenging when first getting started and the formal Interactive Brokers documentation lacks some detailed explanation and implementations.


#  Installation  - Preparing the environment : 

# Python.

* Run a installation of python library ib_insync /// for windows you need to use a lower python version not 3.10, use => 3.9.1 84x or lower.

* Install numpy library first => py -m pip install numpy, might need to upgrade => py -m pip install --upgrade pip

  If this doesn't work try these ones and then upgrade => py -m pip install --upgrade pip

1. 'py -m pip install numpy' OR (used)
2. 'python -m pip install numpy' OR
3. 'py -m pip3 install numpy' OR
4. 'python -m pip3 install numpy

* After Install ib_insync library = > py -m pip install ib_insync


* Install for Python 3.6  dataclasses package py -m pip install dataclasses

* Run in Python => python filename.py


* Interactive Broker's Trading Platform - don't forget to download your Interactive Broker's trading platform (desktop version ) and to log in for checking the Websocket connection.

# Next steps- Python, Node.js server, React.

* Websocket Python, Nodejs - Redis - Google Cloud.

https://ib-insync.readthedocs.io/api.html

 *contract details 

https://nbviewer.org/github/erdewit/ib_insync/blob/master/notebooks/contract_details.ipynb

https://interactivebrokers.github.io/tws-api/basic_orders.html

https://www.youtube.com/watch?v=Dx-HKnpW0bI&t=21s Tutorial 



# Trade keeps track of an order, its status and all its fills.

* Events:
statusEvent (trade: Trade)

modifyEvent (trade: Trade)

fillEvent (trade: Trade, fill: Fill)

commissionReportEvent (trade: Trade, fill: Fill, commissionReport: CommissionReport)

filledEvent (trade: Trade)

cancelEvent (trade: Trade)

cancelledEvent (trade: Trade)


# Market data scanners - worldwide 

* scanStocks.py file > Use in order to browse stocks in different regions. Also browse other assets like ETF, Funds and Bonds.

https://groups.io/g/insync/topic/market_data_scanners/22402297?p=

 e.g Use individual locationCodes to change world regions .

 LocationCode

"STK",
"STOCK.HK",
"STOCK.EU"
"STK.US",
"STK.US.MAJOR",
"STK.US.MINOR",
"STK.HK.SEHK",
"STK.HK.ASX",
"STK.EU"


scanCode

"LOW_OPT_VOL_PUT_CALL_RATIO",
"HIGH_OPT_IMP_VOLAT_OVER_HIST",
"LOW_OPT_IMP_VOLAT_OVER_HIST",
"HIGH_OPT_IMP_VOLAT",
"TOP_OPT_IMP_VOLAT_GAIN",
"TOP_OPT_IMP_VOLAT_LOSE",
"HIGH_OPT_VOLUME_PUT_CALL_RATIO",
"LOW_OPT_VOLUME_PUT_CALL_RATIO",
"OPT_VOLUME_MOST_ACTIVE",
"HOT_BY_OPT_VOLUME",
"HIGH_OPT_OPEN_INTEREST_PUT_CALL_RATIO",
"LOW_OPT_OPEN_INTEREST_PUT_CALL_RATIO",
"TOP_PERC_GAIN",
"MOST_ACTIVE",
"TOP_PERC_LOSE",
"HOT_BY_VOLUME",
"TOP_PERC_GAIN",
"HOT_BY_PRICE",
"TOP_TRADE_COUNT",
"TOP_TRADE_RATE",
"TOP_PRICE_RANGE",
"HOT_BY_PRICE_RANGE",
"TOP_VOLUME_RATE",
"LOW_OPT_IMP_VOLAT",
"OPT_OPEN_INTEREST_MOST_ACTIVE",
"NOT_OPEN",
"HALTED",
"TOP_OPEN_PERC_GAIN",
"TOP_OPEN_PERC_LOSE",
"HIGH_OPEN_GAP",
"LOW_OPEN_GAP",
"LOW_OPT_IMP_VOLAT",
"TOP_OPT_IMP_VOLAT_GAIN",
"TOP_OPT_IMP_VOLAT_LOSE",
"HIGH_VS_13W_HL",
"LOW_VS_13W_HL",
"HIGH_VS_26W_HL",
"LOW_VS_26W_HL",
"HIGH_VS_52W_HL",
"LOW_VS_52W_HL",
"HIGH_SYNTH_BID_REV_NAT_YIELD",
"LOW_SYNTH_BID_REV_NAT_YIELD"


