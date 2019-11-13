import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
c = conn.cursor()

print('How many total Characters are there?')
c.execute("SELECT COUNT(*) FROM charactercreator_character")
print(c.fetchone(), '\n')

print("How many of each specific subclass?")
c.execute("SELECT COUNT(*) FROM charactercreator_cleric")
print('Clerics:', c.fetchone(), '\n')

c.execute("SELECT COUNT(*) FROM charactercreator_fighter")
print('Fighters:', c.fetchone(), '\n')

c.execute("SELECT COUNT(*) FROM charactercreator_mage")
print('Mages:', c.fetchone(), '\n')

c.execute("SELECT COUNT(*) FROM charactercreator_necromancer")
print('Necromancers:', c.fetchone(), '\n')

c.execute("SELECT COUNT(*) FROM charactercreator_thief")
print('Thiefs:', c.fetchone(), '\n')

print("How many total Items?")
c.execute('SELECT COUNT(*) FROM armory_item')
print(c.fetchone(), '\n')



print("How many of the Items are weapons? How many are not?")


print("How many Items does each character have? (Return first 20 rows)")
print("How many Weapons does each character have? (Return first 20 rows)")
print("On average, how many Items does each Character have?")
print("On average, how many Weapons does each character have?")

# USE TO SAVE WORK IF SOMETHING CHANGEd
# SQLITE3 AUTO-SAVES THOUGH
# conn.commit() 

conn.close()