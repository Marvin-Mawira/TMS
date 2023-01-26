#!/usr/bin/python3
import sqlite3

conn = sqlite3.connect("crowd.db")

cr = conn.cursor()

cr.execute("create table if not exists main(\
        id integer primary key autoincrement not null,\
        name text,\
        location)")

cr.execute("create table if not exists sub(\
        id integer primary key autoincrement not null,\
        name text not null,\
        main integer,\
        foreign key (main) references main(id))")

def insert(name, main):
        query = "insert into sub (name, main) values (?, ?)"
        params = (name, main)
        cr.execute(query, params)
        conn.commit()
        print("inserted ", main)

cr.execute("insert into main(name, location) values('abel', 'home')")
cr.execute("insert into main(name, location) values('aden', 'home')")
cr.execute("insert into main(name, location) values('aisha', 'home')")
cr.execute("insert into main(name, location) values('aiden', 'home')")

conn.commit()
mems = ['aaron', 'abas', 'abbie', 'abby', 'abdul', 'abel', 'abelardo', 'abelrai', 'abigail', 'abisara', 'abogada', 'abogados', 'abraham', 'abrey', 'abril', 'achille', 'adam', 'adamn', 'adams', 'adan', 'adar', 'adel', 'adele', 'aden', 'adi', 'adimarys', 'adolfo', 'adria', 'adrian', 'adriana', 'adriane', 'adriann', 'adrianni', 'adriano', 'adrianus', 'adrien', 'adrienne', 'afrim', 'agathe', 'aggie', 'agnes', 'agnieszka', 'agostina', 'aguilar', 'agustin', 'ahlam', 'ahmay', 'ahmed', 'aida', 'aide', 'aiden', 'aileen', 'ailyn', 'aime', 'aimee', 'airnbn', 'aisha', 'akhil', 'aki', 'akiko']

l = len(mems)

k=0
i=1
for j in range(l):
        if k == 15:
                k=0
                i += 1
        insert(mems[j], i)
        k+=1

cr.close()
conn.close()
