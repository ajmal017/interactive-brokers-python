# The RSI is calculated using average price gains and losses over a given period of time.
import talib
import numpy as np
import pandas as pd


class TechnicalAnaylsisLibrary: 

    def reqRsi(close, date, period = 14):
        real = talib.RSI(close, timeperiod = period)
        df['rsi' + str(period)] = real
        return df

