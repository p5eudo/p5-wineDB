import sqlite3


# Connects to DB
def dbConnector(dbName):
    db = sqlite3.connect(dbName)    
    return db

# Closes DB connection
def dbCloser(db):
    db.close()

# Creates cursor
def cursorCreator(db):
    cur = db.cursor()
    return cur

# Displays table contents
def tableDisplay(cur):
    cur.execute('SELECT * FROM wines;')
    for row in cur:
        print(row)
    

def main():
    dbName = 'p5-wineDB.db'
    
    db = dbConnector(dbName)
    cur = cursorCreator(db)
    tableDisplay(cur)
    dbCloser(db)
    
    print('\nfinished')


if __name__ == '__main__':
    main()
