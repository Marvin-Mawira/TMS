import sqlite3

# create database if it does not exist or read existing
conn = sqlite3.connect('TMS.db')
cursor = conn.cursor()

# units table
cursor.execute("""CREATE table if not exists unit 
    (id text primary key not null,
    name varchar(50) not null,
    students int not null,
    lecturer varchar(20),
    foreign key (lecturer) references lecturer(id));""")

cursor.execute("""create table if not exists lecturer(
    id text primary key not null,
    name varchar(50) not null);""")

cursor.execute("""create table if not exists courses(
    id text primary key not null,
    abbr char(10),
    name varchar(100));""")

cursor.execute("""create table if not exists classes(
    name text primary key  not null,
    capacity int not null,
    block char not null);""")

cursor.execute("""create table if not exists classesunit(
    id integer primary key autoincrement not null,
    course int not null,
    unit text not null,
    foreign key(course) references courses(id),
    foreign key(unit) references unit(id));""")

print("DATABASE CREATED SUCCESSFULLY!>")
conn.commit()
cursor.close()
conn.close()
