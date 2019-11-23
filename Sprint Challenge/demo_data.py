import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
c = conn.cursor()

# Create table
c.execute("CREATE TABLE IF NOT EXISTS demo (S varchar(255), X int, Y int);")

# Truncate demo table
c.execute("DELETE FROM demo")
c.execute("INSERT INTO demo (S, X, Y) values ('g', '3', '9');")
c.execute("INSERT INTO demo (S, X, Y) values ('v', '5', '7');")
c.execute("INSERT INTO demo (S, X, Y) values ('f', '8', '7');")

# USE TO SAVE WORK IF SOMETHING CHANGED
# SQLITE3 AUTO-SAVES THOUGH
conn.commit() 

# Test with queries
c.execute("SELECT COUNT(*) FROM demo")
print(f'Total rows: {c.fetchone()}')

c.execute("SELECT COUNT(*) FROM demo WHERE X>=5 AND Y>=5")
print(f'Total number of rows where x and y are at least 5: {c.fetchone()}')

c.execute("SELECT COUNT(DISTINCT Y) FROM demo")
print(f'Total unique values of y: {c.fetchall()}')

conn.close()