__author__ = 'Tom'
import psycopg2
from index import platform
import inspect
import re

# Connect to an existing database
conn = psycopg2.connect("dbname=Allied user=postgres password=snowman66 host=localhost")

# Open a cursor to perform database operations
cur = conn.cursor()


""" gets names of all categories of object from script """

l = platform.keys()
table_names = []
for i in l:
   # print(i)
    table_names.append(i)

print(table_names)
""" checks table exists in db """


def get_table_keys_from_script(tablename):
    return(platform[tablename].keys())

key1 = list(get_table_keys_from_script('currencies'))

def get_table_values_from_script(tablename):
    return(platform[tablename].values())

value1 = list(get_table_values_from_script('currencies'))
print(value1)
def check_col_exists_in_db_table(con, table_name, colname):
    try:
        cur = con.cursor()
        cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name='" + table_name + "' and column_name='" + colname + "';")
        exists = cur.fetchone()[0]
        print(exists + 'hh')
        cur.close()
    except(psycopg2.Error, TypeError, UnboundLocalError) as e:
        print(e)
        print('column name doesnt exist?')
    return exists


print(key1)
print(check_col_exists_in_db_table(conn, 'currencies', 'id'))

def table_exists(con, table_str):
    exists = False
    try:
        cur = con.cursor()
        str2 = "select exists(select relname from pg_class where relname='" + table_str + "')"
        cur.execute(str2)
        exists = cur.fetchone()[0]
        print(exists)
        cur.close()
    except(psycopg2.Error) as e:
        print(e)
        print('table name doesnt exist?')

    return exists

""" Function converts list to ( , , , ,) format """
def list_to_string_format(list1):
    k = ', '.join(list1)
    return '(' + k + ')'


print(list_to_string_format(key1))
""" insert values of table in table in DB if table exists """

       # EXAMPLE INSERT STRRING      cur.execute("INSERT INTO " + 'test' + " (id, num, data) VALUES (88, 33 ,'FF');")

def insert_row2(con, tablename, keys_arr, values_arr):
    if table_exists(con, tablename) == True:
        print("INSERT INTO " + tablename + " " + keys_arr + " VALUES " + values_arr + ";")
        cur.execute("INSERT INTO " + tablename + " " + keys_arr + " VALUES " + values_arr + ";")
#### TO DO - is check the right data types match up to db and that there are apostrophes enclosing every element 


insert_row2(conn, 'currencies', list_to_string_format(key1), list_to_string_format(value1))

# Execute a command: this creates a new table
#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)

#cur.execute("INSERT INTO password_resets (email, token, created_at) VALUES (%s, %s, %s)", ["PPP", "2", datetime.datetime.now()])
# Query the database and obtain data as Python objects
#cur.execute("SELECT * FROM password_resets;")
#print(cur.fetchall())

#cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
#cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE';")
#print(cur.fetchall())

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
