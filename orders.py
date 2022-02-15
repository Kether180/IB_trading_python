from ib_insync import *


ib = IB()
ib.connect("127.0.0.1", 7497, clientId=1)


stock = Stock("AAPL", "SMART", "EUR")

#order = MarketOrder("BUY", 10)

order = LimitOrder("BUY", 5, 91.33) # 5 shares

#order = LimitOrder('SELL', 20000, 1.11)

trade = ib.placeOrder(stock, order) # connect the event and the order 


print(trade)


def orderFilled(trade, fill): # call function , get a copy of the fill order
    print("order has been filled")
    print(order)
    print(fill)


trade.filledEvent += orderFilled # fillEvent 


ib.sleep(5)

for trade in ib.trades():
    print("=== one of my trades===")
    print(trade)

for order in ib.orders():
    print("=== one of my orders ===")
    print(order)


ib.run()
