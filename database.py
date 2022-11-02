import mysql.connector
from paprika import *
from cliente import *

initial_schema_location: str = "sql_files/initial_schema.sql"
clean_database_location: str = "sql_files/clean_database.sql"


@data
class Database:  #TODO convert to class Database

# TODO clienteDAO
def create_cliente(client: Cliente, mycursor):
    query = "INSERT INTO cliente VALUES (%d, %s, %s, %s, %s, %s, %s, %f)" % client
    mycursor.execute(query)


def create_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )

    return mydb.cursor()


def create_database(mycursor):
    mycursor.execute("CREATE DATABASE IF NOT EXISTS market")
    mycursor.execute("USE market")

    execute_sql_script(initial_schema_location, mycursor)


def clean_database(mycursor):
    execute_sql_script(clean_database_location, mycursor)


def execute_sql_script(file_location, mycursor):
    with open(file_location, encoding='utf-8') as f:
        mycursor.execute(f.read(), multi=True)
