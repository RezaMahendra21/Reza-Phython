import datetime as dt
import os

import sqlite3 as sqlite
from collections import Counter

os.system("clear")



# print(dt.datetime.now())

# con = sqlite.connect("coba.db")
# cur = con.cursor()
# cur.execute("CREATE TABLE movie(title, year, score)")
# res = cur.execute("SELECT title FROM movie")
# res.fetchone()
# cur.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)
# con.commit()

# res = cur.execute("SELECT score FROM movie")
# print(res.fetchall())
# res.fetchall()
# for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
#     print(row)

# dataSet = [1,2,3,45,5,566,7,8,8,1,2,4,5,5,3,2]
# print(dataSet.count(1))
# dataCount = Counter(dataSet)
# print(dataCount[5])
import io
file = io.open("./12_standard_library/saya_ok.txt", "r")
print(file.read())