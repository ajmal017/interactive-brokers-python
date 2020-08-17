from ib_insync import *
from studies.RelativeStrengthIndex import RelativeStrengthIndex as rsi

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=8888) #client set in TWS


# ib.reqHeadTimeStamp(contract, whatToShow='TRADES', useRTH=True)

# check contracts detail
def qualifyContracts(contract):
    detail = ib.qualifyContracts(contract)
    print(detail)

#MarketOrder place order market price
def placeOrder(contract, order):
    marketTrade = ib.placeOrder(contract, marketOrder)
    print(marketTrade)


def ReqData(contract):
    return ib.reqHistoricalData(
        contract,
        endDateTime='',
        durationStr='1 D',
        barSizeSetting='1 min',
        whatToShow='TRADES',
        useRTH=True,
        formatDate=1)
    
    # df = util.df(bars)
    # print(df)


if __name__ == "__main__":
    #stock : stock, exchange, currency
    contract = Stock('AAPL', 'SMART', 'USD')
    # marketOrder = MarketOrder('SELL', 200)
    bars = ReqData(contract)
    df = util.df(bars)
    print(df)
    df_close = df["close"].values
    df_date = df["date"].values
    rsi.reqRsi(df_close, df_date)
    # rsi.reqAvgGan(df_close)


