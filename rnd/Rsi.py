import talib
import numpy as np


class Rsi:

    def reqRsi(close):
        close = np.asarray(close)
        real = talib.RSI(close, timeperiod=100)
        print(real)