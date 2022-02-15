from ib_insync import *
from bs4 import BeautifulSoup as bs  #  Library for pulling data out of HTML and XML files.

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

stock = Stock('DBK', 'SMART', 'EUR')  # Deutsche Bank AG Company information  - DBK   - AAPL . TSLA 


companyinfo = ib.reqFundamentalData(stock, 'ReportSnapshot') # Require a report type.


#print(companyinfo)

content = bs(companyinfo, "xml")

print(content)

ratios = content.find_all("Ratio")  # ratio's fields

for ratio in ratios:
 print(ratio['FieldName'])
 print(ratio.text)

# 'ReportsFinSummary': Financial summary
# 'ReportsOwnership': Company's ownership
# 'ReportSnapshot': Company's financial overview
# 'ReportsFinStatements': Financial Statements
# 'RESC': Analyst Estimates
# 'CalendarReport': Company's calendar


