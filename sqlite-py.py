import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
        (ID INT PRIMARY KEY     NOT NULL,
        NAME            TEXT    NOT NULL,
        AGE             INT     NOT NULL,
        ADDRESS         CHAR(50),
        SALARY          REAL);''')
print("Table created successfuly")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (1, 'PAUL', 32, 'CALIFORNIA', 20000.00)")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (2, 'Allen', 25, 'Texas', 15000.00)")
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
        VALUES (3, 'mark', 25, 'Richmond', 56000.00)")
conn.commit()
print("Records created successfully.")
cursor = conn.execute("SELECT * from COMPANY")
print("\nReading records...\n\nPrinting records...\n")

for row in cursor:
    print(f"ID = {row[0]}")
    print(f"NAME = {row[1]}")
    print(f"AGE = {row[2]}")
    print(f"ADDRESS = {row[3]}")
    print(f"SALARY = {row[4]}")
    print()
print("DONE")



conn.execute("UPDATE COMPANY set SALARY = 25000.00  where ID = 1")
print("Updating values...\n")
conn.commit()

print("Total number of rows updated: ", conn.total_changes)
conn.execute("DELETE from COMPANY where ID = 4")
conn.commit()

print("Total number of rows deleted: ", conn.total_changes)
conn.close()