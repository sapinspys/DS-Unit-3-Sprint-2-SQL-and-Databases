import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
c = conn.cursor()

# USE TO SAVE WORK IF SOMETHING CHANGEd
# SQLITE3 AUTO-SAVES THOUGH
# conn.commit() 

conn.close()