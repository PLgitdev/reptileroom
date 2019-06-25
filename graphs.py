import psycopg2
import time
import  datetime
import  numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from ScaleAndBuy import db_list

def graph_it(column,table_name,db_list):
    con = sqlite3.connect(db_list)
    curs = con.cursor()
    sql = 'SELECT '+column+' From '+table_name+';'
    graphArray = []
    curs.execute(sql)
    startingInfo = str(curs.fetchall()).strip("'()[],")
    for i in startingInfo:
        split = startingInfo.split(',')
        graphArray.append(float(split[0]))
    x = np.array(graphArray)
    gR = (1 + np.math.sqrt(5)) / 2
    plt.figure
    plt.plot(x)
    plt.ylabel('Last')
    plt.grid(True)
    axis = plt.gca()
    axis.set_ylim([.029900001, .03050001])
    axis.set_xlim([0,10000])
    plt.show()

graph_it('Last','ohlc',db_list)

#
# sql_two = 'SELECT ' + column + ' From ' + table_name + ';'
# curs.execute(sql_two)
# startingInfoTwo = str(curs.fetchall()).strip("'()[],")
# graphArrayTwo = []
# for i in startingInfoTwo:
#     split = startingInfoTwo.split(',')
#     graphArrayTwo.append(float(split[0]))
