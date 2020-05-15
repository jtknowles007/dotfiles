#! /usr/bin/env python3

from datetime import datetime, time
import yahoo_fin.stock_info as yf
def stock(symbol):
    lookup = yf.get_quote_table(symbol, dict_result=True)
    quoteprice = lookup['Quote Price']
    openprice = lookup['Previous Close']
    currentprice = round(quoteprice,2)
    diffprice = round(quoteprice - openprice,2)
    if diffprice >0:
        symbol = ''
    elif diffprice <0:
        symbol = ''
    else:
        symbol = ' '
    return [currentprice,symbol,diffprice]

def main():
    now = datetime.now().time()
    stocklist = ['^DJI','^IXIC']
    if time(16,0) <= now <= time(9,30):
        dji = stock(stocklist[0])
        ndq = stock(stocklist[1])
        print("{} DJIA: {:,} {}{:,} \
            NASDAQ: {:,} {}{:,}\
            ".format(now,dji[0],dji[1],dji[2],ndq[0],ndq[1],ndq[2]))
    else:
        print("Markets Closed")

if __name__ == "__main__":
    main()