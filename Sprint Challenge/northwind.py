import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
c = conn.cursor()

# What are the ten most expensive items (per unit price) in the database?

# print(c.execute('SELECT sql FROM sqlite_master WHERE name="Product";').fetchall())

print(c.execute("SELECT ProductName, MAX(UnitPrice) FROM Product").fetchone()) 

# What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)

# print(c.execute('SELECT sql FROM sqlite_master WHERE name="Employee";').fetchall())

print(c.execute("SELECT FirstName, LastName, HireDate-BirthDate FROM Product").fetchone()) 

# (*Stretch*) How does the average age of employee at hire vary by city?

# conn.commit() 

conn.close()