__author__ = 'Tom'
import psycopg2
from index import platform
import inspect
import re


""" gets names of all categories of object from script """
def get_table_keys_from_script(tablename):
    return(platform[tablename].keys())


""" checks table exists in db """
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
def list_to_string_format(value_list):
    values = ','.join(str(v) for v in value_list)
#    k = ', '.join(list1)
    print('values: ' + values)
    return '(' + values + ')'


def get_table_values_from_script(tablename):
    return platform[tablename].values()


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

""" insert values of table in table in DB  """
def insert_row2(con, tablename, keys_arr, values_arr):
    if table_exists(con, tablename) == True:
        print(tablename)
        print("INSERT INTO " + tablename + " " + keys_arr + " VALUES " + values_arr + ";")
        cur.execute("INSERT INTO " + tablename + " " + keys_arr + " VALUES " + values_arr + ";")


def insert_to_db(table):

    l = platform.keys()
    table_names = []
    for i in l:
        table_names.append(i)

    print(table_names)

    key1 = list(get_table_keys_from_script(table))

    value1 = list(get_table_values_from_script(table))

    print(list_to_string_format(key1))

    insert_row2(conn, table, list_to_string_format(key1), list_to_string_format(value1))

# Connect to an existing database
conn = psycopg2.connect("dbname=Allied user=postgres password=snowman66 host=localhost")

# Open a cursor to perform database operations
cur = conn.cursor()

for i in platform.keys():
    insert_to_db(i)
#insert_to_db('platforms')

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
