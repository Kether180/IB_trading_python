from ib_insync import *
from bs4 import BeautifulSoup as bs  #  Library for pulling data out of HTML and XML files.

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

stock = Stock('DBK', 'SMART', 'EUR')  # Deutsche Bank AG Company information 


companyinfo = ib.reqFundamentalData(stock, 'ReportSnapshot')

print(companyinfo)

content = bs(companyinfo, "xml")

ratios = content.find_all("Ratio")

for ratio in ratios:
    print(ratio['FieldName'])
    print(ratio.text)

# 'ReportsFinSummary': Financial summary
# 'ReportsOwnership': Company's ownership
# 'ReportSnapshot': Company's financial overview
# 'ReportsFinStatements': Financial Statements
# 'RESC': Analyst Estimates
# 'CalendarReport': Company's calendar
