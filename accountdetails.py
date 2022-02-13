from ib_insync import *


ib = IB()
ib.connect("127.0.0.1", 7497, clientId=1)
ib.accountdetails()


class AccountSummaryTags:
    ("AccountType", "NetLiquidation", "TotalCashValue", "SettledCash", "AccruedCash", "BuyingPower", "EquityWithLoanValue", "PreviousDayEquityWithLoanValue", "GrossPositionValue", "ReqTEquity", "ReqTMargin", "SMA", "InitMarginReq", "MaintMarginReq", "AvailableFunds", "ExcessLiquidity",
     "Cushion", "FullInitMarginReq", "FullMaintMarginReq", "FullAvailableFunds", "FullExcessLiquidity", "LookAheadNextChange", "LookAheadInitMarginReq", "LookAheadMaintMarginReq", "LookAheadAvailableFunds", "LookAheadExcessLiquidity", "HighestSeverity", "DayTradesRemaining", "Leverage")


account = ib.reqAccountSummary(AccountSummaryTags)

# reqAccountSummary(9001, "All", AccountSummaryTags.GetAllTags());
# reqAccountSummary(9002, "All", "$LEDGER");

#accountSummary(int reqId, string account, string tag, string value, string currency)
# print ("Acct Summary. ReqId: " + reqId + ", Acct: " + account + ", Tag: " + tag + ", Value: " + value + ", Currency: " + currency);


# accountSummaryEnd(int reqId)
           # print("AccountSummaryEnd. Req Id: "+reqId+"\n");

print(account)


def accountDetails(account, total):
    print("My account details")
    print(total)


account.totalEvent += accountDetails


ib.sleep(3)


for account in ib.accountSum():
    print("=== Account Detailed ===")
    print(account)

 # def nextValidId(self, accountId: int)

  #  print("Account Id nextValidAccountId: %d", accountId)
   # self.nextValidAccountId = accountId
    #self.reqAccountSummary(9002, "All", "$LEDGER")


# def accountSummary(self, reqId: int, account: str, tag: str, value: str, currency: str):
 #   print("Acct Summary. ReqId:", reqId, "Acct:", account,"Tag: ", tag, "Value:", value, "Currency:", currency)


ib.run(3)



####

#class MyStrategy(bt.Strategy):

    #def __init__(self):
        #print("initializing strategy")
        #self.data_ready = False
        
    #def notify_data(self, data, status):
        #print('Data Status =>', data._getstatusname(status))
        #if status == data.LIVE:
            #self.data_ready = True

    #def log_data(self):
        #ohlcv = []
        #ohlcv.append(str(self.data.datetime.datetime()))
        #ohlcv.append(str(self.data.open[0]))
        #ohlcv.append(str(self.data.high[0]))
        #ohlcv.append(str(self.data.low[0]))
        #ohlcv.append(str(self.data.close[0]))
        #ohlcv.append(str(self.data.volume[0]))
        #print(",".join(ohlcv))
    
    #def next(self):
        #self.log_data()

            #if not self.data_ready:
            #return

        # if not self.position:
        #     self.buy(size=2)
        # elif self.position:
        #     self.sell()
        

      
#def start():
    #print("starting backtrader")
    #cerebro = bt.Cerebro()

    #store = bt.stores.IBStore(port=7497)
    #data = store.getdata(dataname='USD.JPY', sectype='CASH', exchange='IDEALPRO', timeframe=bt.TimeFrame.Seconds)
    #cerebro.resampledata(data, timeframe=bt.TimeFrame.Seconds, compression=15)
    
    #cerebro.broker = store.getbroker()
    #cerebro.addstrategy(MyStrategy)
    #cerebro.run()

#start()

# https://www.youtube.com/watch?v=QF0aSdjv3Jc