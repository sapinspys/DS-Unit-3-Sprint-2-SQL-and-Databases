import psycopg2

host = 'raja.db.elephantsql.com'
user = 'tiqrfzyj'
database = 'tiqrfzyj'
password = 'FIyqnTjfI0zSpGc0l9M0OBtXRdcH0cF8'

pg_conn = psycopg2.connect(database=database, user=user, password=password, host=host)

pg_conn.rollback()
pg_conn.commit()