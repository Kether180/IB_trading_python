from ib_insync import *


ib = IB()
ib.connect("127.0.0.1", 7497, clientId=1)
ib.accountdetails()


class AccountSummaryTags:
    ("AccountType", "NetLiquidation", "TotalCashValue", "SettledCash", "AccruedCash", "BuyingPower", "EquityWithLoanValue", "PreviousDayEquityWithLoanValue", "GrossPositionValue", "ReqTEquity", "ReqTMargin", "SMA", "InitMarginReq", "MaintMarginReq", "AvailableFunds", "ExcessLiquidity",
     "Cushion", "FullInitMarginReq", "FullMaintMarginReq", "FullAvailableFunds", "FullExcessLiquidity", "LookAheadNextChange", "LookAheadInitMarginReq", "LookAheadMaintMarginReq", "LookAheadAvailableFunds", "LookAheadExcessLiquidity", "HighestSeverity", "DayTradesRemaining", "Leverage")


account = ib.reqAccountSummary(AccountSummaryTags)

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

