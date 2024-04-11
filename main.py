# OperationalError: database is locked Python SQLite 

import sqlite3

# 👇️ Set timeout to 30 seconds
con = sqlite3.connect("tutorial.db", timeout=30)

cur = con.cursor()
cur.execute("CREATE TABLE movie(title, year, score)")

con.close()