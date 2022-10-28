import mysql.connector

initial_schema_location: str = "sql_files/initial_schema.sql"
clean_database_location: str = "sql_files/clean_database.sql"


def create_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )

    return mydb.cursor()


def create_database(mycursor):
    mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
    mycursor.execute("USE mydatabase")

    execute_sql_script(initial_schema_location, mycursor)


def clean_database(mycursor):
    execute_sql_script(clean_database_location, mycursor)


def execute_sql_script(file_location, mycursor):
    with open(file_location, encoding='utf-8') as f:
        mycursor.execute(f.read(), multi=True)
