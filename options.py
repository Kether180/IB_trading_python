from itertools import chain
from ib_insync import *

# options is part of the order function where you obtain the contract of the stock 
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

stock = Stock('AAPL', 'SMART', 'USD')
ib.qualifyContracts(stock)   # contract of the stock and exchange , etc - need to obtain contract id from the output for the chain function


ib.sleep(1)


chains = ib.reqSecDefOptParams(stock.symbol, '', stock.secType, stock.conId)

print(util.df(chains))


# panda library  : Expressive data structures designed to make working with “relational” or “labeled” data 
#  as in an SQL table or Excel spreadsheet.
