import sqlite3


def connection():
    conn = sqlite3.connect("TMS.db")
    return conn


def cursr(conn):
    cursor = conn.cursor()
    return cursor


def units(cursor, conn, id, name, students, lecturer):
    query = """insert into unit (id, name, students, lecturer)
    values (?, ?, ?, ?)"""
    params = (id, name, students, lecturer)
    cursor.execute(query, params)
    conn.commit()


def lecturer(cursor, conn, id, name):
    query = """insert into lecturer (id, name) values (?, ?)"""
    params = (id, name)
    cursor.execute(query, params)
    conn.commit()


def courses(cursor, conn, id, abbr, name):
    query = """insert into courses (id, abbr, name) values(?, ?, ?)"""
    params = (id, abbr, name)
    cursor.execute(query, params)
    conn.commit()


def classes(cursor, conn, name, capacity, block):
    query = """insert into classes (name, capacity, block) values (?, ?, ?)"""
    params = (name, capacity, block)
    cursor.execute(query, params)
    conn.commit()
