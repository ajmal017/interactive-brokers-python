from Order import Order
from Strategy import Strategy
from ib_insync import *
import asyncio
import time

class Portfolio:

    def __init__(self, client):
        #maybe dont need to save the data locally, just fetch portfolio everytime when needed
        self.client = client

    #def createStratgy():
        
    def getPortfolio(self): #stock that I bought using paper money
        return self.client.portfolio()

    def getPositions(self): #unknown where all the position from
        return self.client.positions()

    def getLNP(self, account): #unable to get it working
        return self.client.pnl(account)

    def trades(self): #all the trades history
        return self.client.trades()
    

if __name__ == "__main__":
    ib = IB()
    ib.connect('127.0.0.1', 7497, clientId=8888)
    pf = Portfolio(ib)

    cur = pf.getPortfolio()
    print(cur)


    cur = pf.getLNP("ACCOUNT_NUMBER") #unsure where the account number from 
    print(cur)

    # cur = pf.trades()
    # print(cur)
    
    cur = pf.orders()
    print(cur)


