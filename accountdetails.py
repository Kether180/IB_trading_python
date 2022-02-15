from ib_insync import *

from accountdetails import *

ib = IB()
ib.connect("127.0.0.1", 7497, clientId=1)
ib.Accountdetails()


# reqAccountSummary(9001, "All", AccountSummaryTags.GetAllTags());
# reqAccountSummary(9002, "All", "$LEDGER");

account_summary = ib.reqAccountSummary("accountSummaryTags", False, False)

print ("Acct Summary. ReqId: " + reqId + ", Acct: " + account + ", Tag: " + tag + ", Value: " + value + ", Currency: " + currency)


print(account_summary)


def onAccountSummary(accountdetails):  # define function
    print("pending Account Details event received")
    print(accountdetails)
    ib.accountSummaryEvent += onAccountSummary


ib.sleep(3)

ib.run(3)
