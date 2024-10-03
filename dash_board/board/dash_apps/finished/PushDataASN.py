import psycopg2
import pandas as pd

sortingDate = 'sorting_date'


host = "192.168.1.173"
port = "5432"
userName = "postgres"
pas = "changeme"
BDName = "postgres"

def connectToBD():
    conn = psycopg2.connect(dbname=BDName, host=host, user=userName, password=pas, port=port)
    return(conn)

def createTables(conn):
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE asnData (
                    id SERIAL PRIMARY KEY, 
                    city           VARCHAR(50), 
                    street         VARCHAR(200), 
                    operator_names VARCHAR(50), 
                    os_names       VARCHAR(50), 
                    vpn_android    VARCHAR(200), 
                    vpn_ios        VARCHAR(200), 
                    server_switch        INTEGER, 
                    status_facebook_web  INTEGER,
                    status_instagram_web INTEGER, 
                    status_facebook_app  INTEGER,  
                    status_instagram_app INTEGER, 
                    not_exist         BOOLEAN , 
                    created        VARCHAR(50), 
                    video             FLOAT, 
                    author               INTEGER, 
                    mean_all             INTEGER, 
                    mean_web             INTEGER,  
                    mean_app             INTEGER, 
                    ip_address     VARCHAR(50), 
                    asn_city       VARCHAR(50), 
                    region         VARCHAR(50), 
                    country        VARCHAR(50), 
                    loc            VARCHAR(50), 
                    asnName        VARCHAR(250),  
                    asnNumber      VARCHAR(250),  
                    postal         VARCHAR(50), 
                    timezone       VARCHAR(150), 
                    sorting_date    DATE,
                    year                 INTEGER,
                    week_number           INTEGER, 
                    week_period    VARCHAR(150),
                    week_sorting_date  DATE, 
                    month_name      VARCHAR(50), 
                    month_sorting_date DATE
                   )""")
    


data = pd.read_json('тестовые обработанные 2.json')
print(data)
data[sortingDate] = pd.to_datetime(data[sortingDate], unit='ms')
data['week_sorting_date'] = pd.to_datetime(data['week_sorting_date'], unit='ms')
data['month_sorting_date'] = pd.to_datetime(data['month_sorting_date'], unit='ms')
print(data)
print(data.columns)
print(data.dtypes)
conn = connectToBD()
createTables(conn=conn)
if len(data) > 0:
    df_columns = list(data)
    columns = ",".join(df_columns)
    values = "VALUES({})".format(",".join(["%s" for _ in df_columns])) 
    insert_stmt = "INSERT INTO {} ({}) {}".format('asnData',columns,values)
    cur = conn.cursor()
    psycopg2.extras.execute_batch(cur, insert_stmt, data.values)
    conn.commit()
    cur.close()