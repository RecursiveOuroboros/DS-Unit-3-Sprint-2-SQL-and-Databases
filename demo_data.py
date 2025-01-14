"""
Part One: Sql and Databases Sprint Challenge
Jason Meil DS3 Sprint 3 Unit 2 - 06.07.2019
"""

import sqlite3
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

# Create the demo table
curs.execute("""CREATE TABLE demo
                (s, x, y)""")

# Insert Data intot he demo table
curs.execute("INSERT INTO demo VALUES ('g', 3, 9)")
curs.execute("INSERT INTO demo VALUES ('v', 5, 7)")
curs.execute("INSERT INTO demo VALUES ('f', 8, 7)")

# Save (commit) the changes for the demo table
conn.commit()

# Count Rows (should be 3) TEST
def row_count():
    curs.execute("""SELECT COUNT(*)
                    FROM demo;""")
    return curs.fetchall()

# How many rows where both 'x' and 'y' are at least 5? (should be 2)x TEST
def xy_atleast_5():
    curs.execute("""SELECT COUNT (*) FROM demo
                    WHERE x >= 5
                    AND y >= 5;""")
    return curs.fetchall()

# Unique values of 'y' (should be 2) TEST
def y_unique():
    curs.execute("""SELECT COUNT (DISTINCT y)
                    FROM demo;""")
    return curs.fetchall()
# Returning Values from the TESTS (Questions 1-3)
print('There are ', row_count(), ' rows in the demo table')
print('\n')
print('There are ', xy_atleast_5(), ' rows where both x and y are at least 5 in the demo table')
print('\n')
print('There are ', y_unique(), ' unique y values in the demo table')
