# Research & Development

## 08/13/2020
```
IB Insync research 
- able to buy and sell 
- able to request HistoricalData
- contract detail

TA-lib research
- RSI indicator
```



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

terminal, and change directory to your the file that you downloaded. and run the commend below.

```
pip install {name of the file}
```


# Links
Backtrader:  https://www.backtrader.com/docu/quickstart/quickstart/

QTpylib: https://github.com/ranaroussi/qtpylib

IB TWS API: http://interactivebrokers.github.io/tws-api/

TA-Lib: https://mrjbq7.github.io/ta-lib/doc_index.html

ib_insync: https://ib-insync.readthedocs.io/notebooks.html

# Unrelated Reasearch
python path solution: https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f