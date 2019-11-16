import sqlite3
import pandas as pd
from sqlalchemy import create_engine

db_string = 'postgres://tiqrfzyj:FIyqnTjfI0zSpGc0l9M0OBtXRdcH0cF8@raja.db.elephantsql.com:5432/tiqrfzyj'
engine = create_engine(db_string)

pg_conn = engine.connect()


def latin2utf(x):
    return str(x, 'latin-1')


sl_conn = sqlite3.connect('../module1-introduction-to-sql/rpg_db.sqlite3')
sl_conn.text_factory = latin2utf

table_names_dict = {'armory_item':'item_id','charactercreator_character':'character_id','charactercreator_character_inventory':'id'}

for table_name, primary_key in table_names_dict.items():
    print(table_name)
    df = pd.read_sql(f"SELECT * FROM {table_name}", sl_conn)
    df = df.set_index(primary_key, verify_integrity=True)
    df.to_sql(table_name, pg_conn)