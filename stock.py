from ib_insync import *

ib = IB()

ib.connect('127.0.0.1', 7497, clientId=1)  # connect to TWS (Workstation) websocket - you can have multiple ID connections 

# contract = Forex("EURUSD")
stock = Stock("AMD", "SMART", "USD") # can use also  = contract()  - symbol /exchange / currency 

bars = ib.reqHistoricalData(
    stock, endDateTime='', durationStr='30 D', # 30 days of historical data
    barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)  # 1hour bars. ,userrth = info in regular trading hours.


# convert to pandas dataframe:
# df = util.df(bars)
# print(df)

# Realtime Market data
market_data = ib.reqMktData(stock, "", False, False)

print(market_data)


def onPendingTicker(ticker):
    print("pending ticker event recieved")
    print(ticker)


ib.pendingTickersEvent += onPendingTicker

ib.run()
