#!/usr/bin/python3
import sqlite3

conn = sqlite3.connect('try.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS REC ( NUMBER REAL, NAME TEXT)')

NN = 123
NM = 'GFG'

c.execute('INSERT INTO REC (NUMBER, NAME) VALUES(?, ?)', (NN, NM))
conn.commit()

c.close()
conn.close()
