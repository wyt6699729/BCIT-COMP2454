# Exercise 1

import pandas as pd
from sqlalchemy import create_engine

# The data file path and file name need to be configured.
filePath = '../datasets/retailerDB.csv'

df = pd.read_csv(filePath)

# Placed query in this function to enable code re-usability.
def showQueryResult(sql):
    engine = create_engine('sqlite://', echo=False)
    connection = engine.raw_connection()
    df.to_sql(name='RetailInventory', con=connection, if_exists='replace', index=False)

    # This code performs the query
    queryResult = pd.read_sql(sql, connection)
    return queryResult

# Read all rows from the table
SQL = "SELECT * FROM RetailInventory"
result = showQueryResult(SQL)
print(result)

# Exercise 2


# Exercise 3
SQL = "SELECT * FROM RetailInventory WHERE price >= 4"
result = showQueryResult(SQL)
print(result)

# Exercise 4
SQL = "SELECT * FROM RetailInventory WHERE price >= 4 ORDER BY productName"
result = showQueryResult(SQL)
print(result)

# Exercise 5
SQL = "SELECT * FROM RetailInventory ORDER BY productName, quantity"
result = showQueryResult(SQL)
print(result)

# Exercise 6
SQL = "SELECT * FROM RetailInventory WHERE vendor IN ('Cadbury', 'Nestle')"
result = showQueryResult(SQL)
print(result)

# Exercise 7
SQL = "SELECT productName, price, price*1.07 AS afterTaxPrice FROM RetailInventory"
result = showQueryResult(SQL)
print(result)

# Exercise 8
SQL = "SELECT vendor, productName FROM RetailInventory WHERE vendor LIKE '%ry'"
result = showQueryResult(SQL)
print(result)

# Exercise 9
SQL = "SELECT productName FROM RetailInventory WHERE productName LIKE 'F%'"
result = showQueryResult(SQL)
print(result)

# Exercise 10
SQL = "SELECT productName, MIN(price) AS minPrice FROM RetailInventory GROUP BY productName"
result = showQueryResult(SQL)
print(result)

# Exercise 11
SQL = "SELECT vendor, SUM(quantity) AS totalQuantity FROM RetailInventory WHERE vendor IN ('Silverware Inc.', 'Waterford Corp.') GROUP BY vendor"
result = showQueryResult(SQL)
print(result)

# Exercise 12
SQL = "SELECT vendor, SUM(price*quantity) revenueValue FROM RetailInventory WHERE vendor IN ('Silverware Inc.', 'Waterford Corp.') GROUP BY vendor"
result = showQueryResult(SQL)
print(result)