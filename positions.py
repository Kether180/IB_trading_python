from ib_insync import *

ib = IB()
ib.connect("127.0.0.1", 7497, clientId=1)
ib.positions()


# positions = positions ("string account", "Contract contract", "decimal pos", "double avgCost")
# 
# position(string account, Contract contract, decimal pos, double avgCost)
        
          # print ("Position. " + account + " - Symbol: " + contract.Symbol + ", SecType: " + contract.SecType + ", Currency: " + contract.Currency + 
             #   ", Position: " + Util.DecimalMaxString(pos) + ", Avg cost: " + Util.DoubleMaxString(avgCost));

# positionEnd()
            # print("PositionEnd \n");


            #    client.cancelPositions(); to cancel position
