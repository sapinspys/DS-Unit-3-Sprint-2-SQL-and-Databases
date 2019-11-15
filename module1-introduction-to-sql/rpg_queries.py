import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
c = conn.cursor()

print('How many total Characters are there?')
c.execute("SELECT COUNT(*) FROM charactercreator_character")
print(c.fetchone(), '\n')

print("How many of each specific subclass?")
c.execute("SELECT COUNT(*) FROM charactercreator_cleric")
print('Clerics:', c.fetchone())

c.execute("SELECT COUNT(*) FROM charactercreator_fighter")
print('Fighters:', c.fetchone())

c.execute("SELECT COUNT(*) FROM charactercreator_mage")
print('Mages:', c.fetchone())

c.execute("SELECT COUNT(*) FROM charactercreator_necromancer")
print('Necromancers:', c.fetchone())

c.execute("SELECT COUNT(*) FROM charactercreator_thief")
print('Thiefs:', c.fetchone(), '\n')

print("How many total Items?")
c.execute('SELECT COUNT(*) FROM armory_item')
print(c.fetchone(), '\n')

print("How many of the Items are weapons? How many are not?")
c.execute('SELECT COUNT(*) FROM armory_weapon')
print(c.fetchone(), '\n')

print("How many Items does each character have? (Return first 20 rows)")
c.execute('SELECT COUNT(item_id) AS item_count, character_id FROM charactercreator_character_inventory GROUP BY character_id')
print(c.fetchmany(20), '\n')

print("How many Weapons does each character have? (Return first 20 rows)")
c.execute('SELECT COUNT(i.item_id) weapon_count, i.character_id FROM charactercreator_character_inventory i JOIN armory_weapon a ON i.item_id = a.item_ptr_id GROUP BY character_id')
print(c.fetchmany(20), '\n')

print("On average, how many Items does each Character have?")
c.execute('SELECT AVG(item_id) AS item_count_avg, character_id FROM charactercreator_character_inventory GROUP BY character_id')
print(c.fetchmany(20), '\n')

print("On average, how many Weapons does each character have?")
c.execute('SELECT AVG(i.item_id) weapon_count_avg, i.character_id FROM charactercreator_character_inventory i JOIN armory_weapon a ON i.item_id = a.item_ptr_id GROUP BY character_id')
print(c.fetchmany(20), '\n')

# USE TO SAVE WORK IF SOMETHING CHANGEd
# SQLITE3 AUTO-SAVES THOUGH
# conn.commit() 

conn.close()