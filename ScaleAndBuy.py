import json

import requests
import time
from threading import Thread

from databasefunction import create_connection, insert_ohlc, select_target
from graphs import graph_it


class MarketAction:
    def __init__(self,target,data,quantity):
        self.financial_data= data
        self.quantity = quantity
        self.target = target
        self.sell_one = 0
        self.sell_two = 0
        self.sell_three = 0
        self.sell_four = 0
        self.value_point = 0
    def scale_and_buy(self):
        for i in self.financial_data:
            compare = self.target/i['Last']
            if 7.635 <= compare <= 7.66:
                self.value_point = i['Last']
                print("7.634 I am buying at ", self.value_point)
            elif 6.107 <= compare <= 6.109:
                self.value_point = i['Last']
                print("6.10 I am buying at ", self.value_point)
            elif 4.999 <= compare <= 5.0001:
                self.value_point = i['Last']
                print("5 I am buying at ", self.value_point)
            elif 3.82 <= compare <= 3.83:
                self.value_point = i['Last']
                print("3.82 I am buying at ", self.value_point)
            elif 2.36 <= compare <= 2.37:
                self.value_point = i['Last']
                print("2.36 I am buying at ", self.value_point)
            elif 0 == compare:
                self.value_point = i['Last']
                print("0 I am buying at ", self.value_point)
            elif i['Last']>self.target:
                break
            else:
                print("not this time "+ str(i['Last']))

def target_search(con,OHLC,file):
    for data in OHLC:
        highs = data['High']
        prevDay = data['PrevDay']
        bid = data['Bid']
        last = data['Last']
        con = create_connection(file)
        compare = select_target(con,'Last','ohlc', 'Last  <= "'+str(last).strip(',')+'"')
        for i in compare:
            if last == prevDay or last ==highs or last==bid or last == i:
                highs_target = data['Last']
                print(highs_target)
                print("retracment at " + str(last))
                return highs_target
            else:
                print("no luck")
                print("bid = "+ str(bid))
                print("last = "+ str(last))
                print("prevDay = "+ str(prevDay))
                print("highs = "+ str(highs))
                print ("compare = " + str(compare))

                break


def ohlc_bittrex_grabber(market):
    while True:
        r = requests.api.request(url='https://api.bittrex.com/api/v1.1/public/getmarketsummary?market='+market,method='GET')
        j_data = r.json()
        data = j_data
        with open('C:/Users/P/Desktop/output2.json', 'w+') as open_file:
            open_file.truncate()
            data_string = str(data['result']).replace("'",'"')
            open_file.write(data_string)
            time.sleep(5)
        break


def parse_json_file(json_file)->list:
    with open(json_file,'r+') as openjson:
        json_list = openjson.read()
        OHLC = json.loads(json_list)
        return OHLC


file_one = 'C:/Users/P/Desktop/output2.json'
market_input = input("please tell me a market format x-y: ")
while True:
    ohlc_bittrex_grabber(market_input)
    data = parse_json_file(file_one)
    con = create_connection('retracer.sqlite')
    insert_ohlc(con,data[0])
    b = target_search(con,data,'retracer.sqlite')

    if b:
        while True:
            ohlc_bittrex_grabber(market_input)
            data = parse_json_file(file_one)
            con = create_connection('retracer.sqlite')
            insert_ohlc(con, data[0])

            fib_scale = MarketAction(b,data,quantity=1000)
            fib_scale.scale_and_buy()
            if fib_scale.value_point:
                break
