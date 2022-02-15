from ib_insync import *

ib = IB()
ib.connect("127.0.0.1", 7497, clientId=1)
ib.positions()

# Doing a request involves network traffic going up and down and can take considerable time.
# The current state on the other hand is always immediately available. So it is preferable to use the current state methods over requests.
# For example, use ib.openOrders() in preference over ib.reqOpenOrders(), or ib.positions() over ib.reqPositions(), etc:

stock = Stock('TSLA', 'SMART', 'USD')

bars = ib.reqHistoricalData(
    stock, endDateTime='', durationStr='30 D', # 30 days of historical data
    barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)  # 1hour bars. ,userrth = info in regular trading hours.

ib.reqContractDetails(stock)


print(stock)

ib.sleep(3)


ib.run()


#positions = positions ("string account", "Contract contract", "decimal pos", "double avgCost")

#print ("Position. " + account + " - Symbol: " + contract.Symbol + ", SecType: " + contract.SecType + ", Currency: " + contract.Currency +  ", Position: " + Util.DecimalMaxString(pos) + ", Avg cost: " + Util.DoubleMaxString(avgCost));

# positionEnd()
#print("PositionEnd \n");

# client.cancelPositions(); to cancel position
