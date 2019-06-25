import psycopg2


def create_connection(db_list):
    try:
        connection = psycopg2.connect(user = db_list[1] ,
                password = db_list[2],
                host = db_list[3],
                port = db_list[4],
                database = db_list[5])
        return connection
    except Exception:
        print(Exception)


def create_table(con):
    curs = con.cursor()
    curs.execute('''CREATE TABLE ohlc
(id INTEGER PRIMARY KEY AUTOINCREMENT,
MarketName VARCHAR (32),
 High FLOAT (10),
 Low FLOAT (10),
 Volume FLOAT (10),
 Last FLOAT (10),
 BaseVolume FLOAT (10),
 TimeStamp datetime_interval_precision ,
 Bid FLOAT (10),
 Ask FLOAT (10),
 OpenBuyOrders INTEGER (10),
 OpenSellOrders INTEGER (10),
 PrevDay FLOAT (10),
 Created DATETIME_INTERVAL_PRECISION
 );''')
    con.commit()


def insert_ohlc(con,args):
    for i in args:
        one = str(args['MarketName'])
        two = str(args['High'])
        three = str(args['Low'])
        four = str(args['Volume'])
        five = str(args['Last'])
        six = str(args['BaseVolume'])
        seven = str(args['TimeStamp'])
        eight = str(args['Bid'])
        nine = str(args['Ask'])
        ten  = str(args['OpenBuyOrders'])
        eleven = str(args['OpenSellOrders'])
        twelve = str(args['PrevDay'])
        thirteen = str(args['Created'])
    curs = con.cursor()
    sql = '''INSERT into ohlc
    (MarketName,
 High,
 Low,
 Volume,
 Last,
 BaseVolume,
 TimeStamp,
 Bid,
 Ask,
 OpenBuyOrders,
 OpenSellOrders ,
 PrevDay ,
 Created) 
    VALUES (\"'''+one+'","'+two+'","'+three+'","'+four+'","'+five+'","'+six+'","'+seven+'","'+eight+'","'+nine+'","'+ten+'","'+eleven+'","'+twelve+'","'+thirteen+'");'
    curs.fetchall()
    curs.execute(sql)
    con.commit()

def select_target(con,column,table_name,condition):
    sql= 'SELECT '+column+' FROM '+table_name+' WHERE '+condition+';'
    curs = con.cursor()
    curs.execute(sql)
    con.commit()
    return curs.fetchall()
