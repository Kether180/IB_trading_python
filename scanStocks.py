# SCANNER : STOCKS WORLD WIDE AND HIGH DIVIDEND, LOW DIVIDEND, RATIO, ETC

from ib_insync import *
from bs4 import BeautifulSoup as bs  #  Library for pulling data out of HTML and XML files.

ib = IB()

ib.connect('127.0.0.1', 7497, clientId=1) # 1 option

#allParams = ib.reqScannerParameters() # 2 option xml data for scanner.txt - scan info about different assets.
#print(allParams)  # 2 option

# Search for a particurlar Stock - STK

subscription = ScannerSubscription(instrument='STK', locationCode='STK.US.MAJOR', scanCode='SCAN_currYrETFFYDividendYield_DESC') # 1 option  High Dividend yield ETF  - STOCK.EU.MAJOR

scanData = ib.reqScannerData(subscription) # event to scan stocks etc.

for scan in scanData:
    print(scan) # US STOCKS 
    print(scan.contractDetails.contract.symbol) # 2 option High dividend stocks 

    
#content = bs(scanData, "xml") #  2 option xml data for scanAssets.txt - scan info about different assets. ETF - BONDS - STOCKS - FUNDS 

#print(content)

 # Objects : classib_insync.objects.ScannerSubscription https://ib-insync.readthedocs.io/api.html#module-ib_insync.objects
