import psycopg2
import sqlite3
import pandas as pd

# sl_conn = sqlite3.connect('titanic.csv')
# sl_cur = sl_conn.cursor()
# sl_cur.execute('SELECT * FROM ')

# use pandas to open csv
df = pd.read_csv('titanic.csv')
print(df.head(5))

# connect to PG (psycopg)
host = 'raja.db.elephantsql.com'
user = 'tiqrfzyj'
database = 'tiqrfzyj'
password = 'FIyqnTjfI0zSpGc0l9M0OBtXRdcH0cF8'

pg_conn = psycopg2.connect(database=database, user=user, password=password, host=host)
pg_cur = pg_conn.cursor()

# create proper table (psycopg)
create_shippers_table = """
    CREATE TABLE Shippers(
    ShipperID serial PRIMARY KEY,
    CompanyName VARCHAR (200) NOT NULL,
    Phone VARCHAR (20) NOT NULL
    );
"""

pg_cur.execute(create_shippers_table)
pg_conn.commit()

# use pandas to_sql to pg_conn
df.to_sql('Customers', pg_conn_2)