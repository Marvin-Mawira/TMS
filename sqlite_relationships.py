import sqlite3

crs = sqlite3.connect('test2.db')
print("db created")

#table for families
crs.execute("CREATE TABLE IF NOT EXISTS FAMILIES (\
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
    reference VARCHAR(32) NOT NULL,\
    name TEXT NOT NULL,\
    unite VARCHAR)")

'''Table for articles.
    Many to One relationship:
    one family has one or many articles
    for both one to many or many to one relationships,
        we just need to place a foreign key on one side of
        the relationship.
'''
crs.execute("CREATE TABLE IF NOT EXISTS ARTICLES (\
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL\
    name TEXT NOT NULL, \
    quantity REAL,\
    unite VARCHAR,\
    purchased INTEGER,\
    reserved INTEGER,\
    sold INTEGER,\
    available INTEGER,\
    minimum INTEGER,\
    family_id INTEGER,\
    FOREIGN KEY(family_id) REFERENCES families(id))")

'''For one to one relationship:
each article can belong to one family
each family has only one article
we do that by using two foreign keys on both
    sides of the relationship.
the family code is added some lines as below
'''
# crs.execute("CREATE TABLE IF NOT EXISTS FAMILIES (\
#     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
#     reference VARCHAR(32) NOT NULL,\
#     name TEXT NOT NULL,\
#     unite VARCHAR,\
#     article_id INTEGER,\
#     FOREIGN KEY(article_id) REFERENCES articles(id))")

'''MANY TO MANY RELATIONSHIP
we create and introduce another third table on the relationship
which has two foreign keys that reference both tables
An article belongs to one or many families.
A family has one or many articles
# '''
# CREATE TABLE IF NOT EXISTS families (
#          id INTEGER PRIMARY KEY,
#          reference VARCHAR(32) NOT NULL,
#          name TEXT NOT NULL,
#          unite VARCHAR,
#     );

# CREATE TABLE IF NOT EXISTS  articles (
#         id INTEGER PRIMARY KEY,
#         reference VARCHAR(32) NOT NULL,
#         name TEXT NOT NULL,
#         quantity REAL,
#         unite VARCHAR,
#         purchased INTEGER,
#         reserved INTEGER,
#         sold INTEGER,
#         available INTEGER,
#         minimum INTEGER,
# );    

# CREATE TABLE IF NOT EXISTS articles_families (
#         article_id INTEGER,
#         family_id INTEGER,
#         FOREIGN KEY(article_id) REFERENCES articles(id),
#         FOREIGN KEY(family_id) REFERENCES families(id)

# );
