import sqlite3

conn = sqlite3.connect("data.db")

c = conn.cursor()

def add_user(name:str, age:int):
    int(age)
    c.execute("INSERT INTO users VALUES (?,?)",(name, age,))
    conn.commit()
def rev():
    c.execute("SELECT * FROM users")
    lits = c.fetchall()
    conn.commit()
    return lits

def rm():
    c.execute("DELETE FROM users")
    conn.commit()


conn.commit()