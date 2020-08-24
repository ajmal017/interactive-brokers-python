# Diagram (still in development)

![Alt text](/diagram/IbTWSClassDiagram.png "Optional Title")

# Research & Development

## 08/24/2020

### Development
- all order function are asynchronous
- update on Order.py
- update on Portfolio

### Python library
- Threading vs Asyncio vs multiprocessing

if I contiune using IB_insync to develop, I will not be able to use other async library? if I use threading and Asyncio, I am worry I will run into issue. I will stick with asyncio with ib insync for now. Order.py work perfectly with multiple asynchronous submission. Portfolio.py are pretty straight forward, I probably beautifying the data for the coming next push. 

### Coming Up
- beautifying 
- BOL study
- build a strategy
- probably missed something but will added back to here

## 08/17/2020

### TA-Lab research
- Relative Strength Index 

### Python library
- Pandas
- numpy


TA-Lab RSI function worked well orginally, which I havent really deep dive into
what is Relative Strength Index, RSI in a index range from 0 to 100, which it's indicating the current and historical strength or weakness of a stock or market based on the closing prices of a recent trading period. The period of time can be 
adjust accordingly your strategies and size of the bars. 

Pandas module for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series, here is few different functions which used for today research.

Create table and Adding Column
```py
df = pd.DataFrame({"COLUMN" : DATA_NUMPY_ARRAY})
df['SecondColumn'] = DATA_NUMPY_ARRAY
```

display every row
```py
pd.set_option('display.max_rows', None)
``` 

### Numpy
It is a better fast easier way to deal with array. it capables to handle big data set.
`


## 08/18/2020

### development
-drawing the application structure class diagram


## 08/13/2020

### IB Insync research 
- able to buy and sell 
- able to request HistoricalData
- contract detail

### TA-lib research
- RSI indicator





# Setup Enviornments
### Creating Python Enviornemts
We will use python3 for development. In this enviorment, we will install every related to interactive Brokers, included third parties library

create env
```
python3 -m venv env
```
activate
```
source /env/Scripts/activate
```
deactivate
```
deactivate
```

running an enviornment in VSCode, it need to change the python interpreter.
- ctrl+shf+P -> python: select interpreter

#  Technical Analysis Library

## Installation
download the correct version matching with your python version and 32 or 64

-download : https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib

terminal, and change directory to the file where you downloaded. and run the commend below.

```
pip install {name of the file}
```


# Links
Backtrader:  https://www.backtrader.com/docu/quickstart/quickstart/

QTpylib: https://github.com/ranaroussi/qtpylib

IB TWS API: http://interactivebrokers.github.io/tws-api/

TA-Lib: https://mrjbq7.github.io/ta-lib/doc_index.html

ib_insync: https://ib-insync.readthedocs.io/notebooks.html

# Unrelated Topic
python path solution: https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f