class Data:


 
    def __init__(self, stock, exchange, currency):
        self.contract = Stock(stock, exchange, currency)
        self.history = []
    
    def reqData(client):
        return client.reqHistoricalData(
        contract,
        endDateTime='',
        durationStr='1 D',
        barSizeSetting='1 min',
        whatToShow='TRADES',
        useRTH=True,
        formatDate=1)