# https://nbviewer.jupyter.org/github/erdewit/ib_insync/blob/master/notebooks/ordering.ipynb

from ib_insync import *
import asyncio
import time
import threading

class Order:

    
    def __init__(self, client):
        #maybe dont need to save the data locally, just fetch portfolio everytime when needed
        self.orders = {}
        self.client = client
        
    # def createContract():

    def order(self,action, stock, exchange, currency, quantity):
        stk = Stock(stock, exchange, currency)
        order = MarketOrder(action, quantity)
        marketTrade = self.client.placeOrder(stk, order)
        return marketTrade
        

    async def buyOrder(self, stock, exchange, currency, quantity):
        currentOrder = self.order('BUY', stock, exchange, currency, quantity)
        print('Your Order submitted ' + currentOrder.contract.symbol)
        await self.orderStatus(currentOrder)
        

    async def sellOrder(self, stock, exchange, currency, quantity):
        currentOrder = self.order('SELL', stock, exchange, currency, quantity) 
        print('Your Order submitted ' + currentOrder.contract.symbol)
        await self.orderStatus(currentOrder)
    


    async def orderStatus(self,order): #not finish
        while order.orderStatus.status != 'Filled':
            print ("checking" + order.contract.symbol + ": " + order.orderStatus.status)
            await asyncio.sleep(5)
        else:
            if(order.contract.symbol in self.orders):
                #adding the total stock quantity into orders object
                self.orders[order.contract.symbol]['position'] += order.order.totalQuantity
            else:
                #create new stock in the orders object
                self.orders[order.contract.symbol] = {"position": order.order. totalQuantity }




if __name__ == "__main__":
    ib = IB()
    ib.connect('127.0.0.1', 7497, clientId=8888)
    order = Order(ib)
    apple = order.sellOrder('AAPL', 'SMART', 'USD', 2)
    nvda = order.sellOrder('NVDA', 'SMART', 'USD', 2)


    # -- asyncio (because of ib_insync using asyncio which much better handling async the order)
    async def main():
        statements = []
        statements.append(nvda)
        statements.append(apple)
        await asyncio.gather(*statements, return_exceptions=False)
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    del loop
    print(order.orders)
    
    # -- threading
    # t1 = threading.Thread(target=order1.orderStatus, args=(apple,))
    # t2 = threading.Thread(target=order2.orderStatus, args=(nvda,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # print(order.orders)



    # -- orderstatus
    # <class 'ib_insync.order.Trade'>
    # Trade(contract=Stock(symbol='AAPL', exchange='SMART', currency='USD'), order=MarketOrder(orderId=30, clientId=8888, action='SELL', totalQuantity=100), orderStatus=OrderStatus(orderId=30, status='PendingSubmit', filled=0, remaining=0, avgFillPrice=0.0, permId=0, parentId=0, lastFillPrice=0.0, clientId=0, whyHeld='', mktCapPrice=0.0), fills=[], log=[TradeLogEntry(time=datetime.datetime(2020, 8, 19, 15, 25, 8, 21265, tzinfo=datetime.timezone.utc), status='PendingSubmit', message='')])
