import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
c = conn.cursor()

# What are the ten most expensive items (per unit price) in the database?

# print(c.execute('SELECT sql FROM sqlite_master WHERE name="Product";').fetchall())

print(f"Ten most expensive items:\n{c.execute('SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC').fetchmany(10)}\n")

# What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)

# print(c.execute('SELECT sql FROM sqlite_master WHERE name="Employee";').fetchall())

print(f"Average age of employee at hire date:\n{c.execute('SELECT HireDate-BirthDate FROM Employee').fetchone()}\n") 

# (*Stretch*) How does the average age of employee at hire vary by city?

print(f"Average age of employee at hire by city:\n{c.execute('SELECT City, AVG(HireDate-BirthDate) FROM Employee GROUP BY City').fetchall()}\n") 

# What are the ten most expensive items (per unit price) in the database *and* their suppliers?

# print(c.execute('SELECT sql FROM sqlite_master WHERE name="Supplier";').fetchall())

print(f"Ten most expensive items with suppliers included:\n{c.execute('SELECT p.ProductName, s.CompanyName, p.UnitPrice FROM Product p JOIN Supplier s ON p.SupplierId = s.Id ORDER BY UnitPrice DESC').fetchmany(10)}\n")

# What is the largest category (by number of unique products in it)?

# print(c.execute('SELECT sql FROM sqlite_master WHERE name="Category";').fetchall()) 

print(f"Largest category by number of unique products:\n{c.execute('SELECT COUNT(p.ProductName), c.CategoryName FROM Product p JOIN Category c ON p.CategoryId = c.Id GROUP BY CategoryName ORDER BY CategoryName DESC').fetchone()}\n")

# - (*Stretch*) Who's the employee with the most territories? Use `TerritoryId` (not name, region, or other fields) as the unique identifier for territories.

# conn.commit() 

conn.close()