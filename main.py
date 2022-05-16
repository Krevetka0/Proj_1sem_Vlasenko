import sqlite3 as sq

with sq.connect('DBeaver/saper.db') as con:
    cur = con.cursor()
    # cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
 user_id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT NOT NULL,
 sex INTEGER NOT NULL DEFAULT 1,
 old INTEGER,
 score INTEGER
 )""")
    cur.execute("UPDATE users SET old = 20 WHERE old = 19")
    cur.execute("SELECT * FROM users")
    print(cur.fetchall())
    cur.execute("UPDATE users SET score = score + 300 WHERE score < 1000")
    cur.execute("SELECT * FROM users")
    print(cur.fetchall())
    cur.execute("UPDATE users SET score = score + 100 WHERE old >= 20 ")
    cur.execute("SELECT * FROM users")
    print(cur.fetchall())
    cur.execute("DELETE FROM users WHERE score < 1000")
    cur.execute("SELECT * FROM users")
    print(cur.fetchall())