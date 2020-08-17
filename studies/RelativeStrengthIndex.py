# The RSI is calculated using average price gains and losses over a given period of time.
import talib
import numpy as np
import pandas as pd

class RelativeStrengthIndex:

    # def reqRsi(close, date):
    #     pd.set_option('display.max_rows', None)
    #     df = pd.DataFrame({"date" : date})
    #     df['close'] = close
    #     for n in [14, 30, 90]:
    #         real = talib.RSI(close, timeperiod=n)
    #         df['rsi' + str(n)] = real
    #     print(df)

    def reqRsi(close, date):
            real = talib.RSI(close, timeperiod=n)
            df['rsi' + str(n)] = real
        print(df)

    def reqAvgGan(close):
        close = np.asarray(close)
        slicearray = np.sum(close[:50]) 
        print(slicearray)