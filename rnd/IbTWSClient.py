import sys
import os.path
filepath = os.path.join('..','..','..','TWS API','source','pythonclient')
sys.path.insert(0,filepath)

from ibapi.client import EClient
from ibapi.contract import EWrapper
from ibapi.contract import Contract

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
    
    def error(self, reqId, errorCode, errorString):
        print("Error", reqId, " ", errorCode, " ", errorString)
    
    def contractDetails(self, reqId, contractDetails):
        print("contractDetails: ", reqId, " ", contractDetails)

def main():
    app = TestApp()

    app.connect("127.0.0.1", 7497, 8888)

    contract = Contract()
    contract.symbol = "AAPL"
    contract.secIdType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.primaryExchange = "NASDAQ"

    app.reqContractDetails(1, contract)

    app.run()

if if __name__ == "__main__":
    main()


