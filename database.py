import mysql.connector
from mysql.connector.cursor import MySQLCursor
from mysql.connector import MySQLConnection
from paprika import *

initial_schema_location: str = "sql_files/initial_schema.sql"
clean_database_location: str = "sql_files/clean_database.sql"


@data
@singleton
class Database:
    my_cursor: MySQLCursor
    mydb: MySQLConnection

    def find_product_by_name(self, nome):
        query = "SELECT * FROM produto WHERE nome = '{0}'".format(nome)
        self.my_cursor.execute(query)

        return self.my_cursor.fetchone()

    def create_client(self, client):  # TODO clienteDAO
        query = "INSERT INTO cliente (cpf, nome, email, telefone, senha) " \
                "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')" \
            .format(client.cpf, client.nome, client.email, client.telefone, client.senha)

        self.my_cursor.execute(query)
        self.mydb.commit()

        return self.my_cursor.lastrowid

    def update_client_balance(self, client):
        query = "UPDATE cliente SET saldo = '{0}' WHERE cpf = '{1}'" \
            .format(client.saldo, client.cpf)

        self.my_cursor.execute(query)
        self.mydb.commit()

    def update_client(self, client):
        query = "UPDATE cliente SET nome = '{0}', email = '{1}', telefone = '{2}', senha = '{3}' " \
                "WHERE cpf = '{4}'" \
            .format(client.nome, client.email, client.telefone, client.senha, client.cpf)

        self.my_cursor.execute(query)
        self.mydb.commit()

    def create_database(self):
        self._create_connection()

        self.my_cursor.execute("CREATE DATABASE IF NOT EXISTS market")
        self.mydb.commit()
        self.my_cursor.execute("USE market")
        self.mydb.commit()

        self._create_cliente_table()
        self._create_produto_table()
        self._create_venda_table()
        self._create_produto_venda_table()

        # self._create_products()

    def clean_database(self):
        self._execute_sql_script(clean_database_location)

    def _create_connection(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )

        self.my_cursor = self.mydb.cursor()

    def _execute_sql_script(self, file_location):
        with open(file_location, encoding='utf-8') as f:
            query = f.read().replace("\n", "")
            self.my_cursor.execute(query, multi=True)

    def _create_products(self):
        query = "INSERT INTO produto (nome, categoria, descricao, quantidade, valor) " \
                "VALUES (%s, %s, %s, %s, %s)"

        values = [("Coca-Cola", "Bebidas", "Refrigerante gaseificado 2L", 5, 12.0),
                  ("Ruffles", "Snack", "Batata frita 350g", 11, 7.80)]

        self.my_cursor.executemany(query, values)
        self.mydb.commit()

    def _create_cliente_table(self):
        self.my_cursor.execute("""CREATE TABLE IF NOT EXISTS cliente
        (
            id       int auto_increment primary key,
            cpf      char(11)     not null,
            nome     VARCHAR(255) not null,
            email    VARCHAR(255) not null,
            telefone VARCHAR(11)  not null,
            senha    VARCHAR(30)  not null,
            saldo    float default 0.0
        );""")

    def _create_produto_table(self):
        self.my_cursor.execute("""CREATE TABLE IF NOT EXISTS produto
        (
            id         int auto_increment primary key,
            nome       VARCHAR(255) not null,
            categoria  VARCHAR(255) not null,
            descricao  VARCHAR(255) not null,
            quantidade int          not null,
            valor      float        not null
        );""")

    def _create_venda_table(self):
        self.my_cursor.execute("""CREATE TABLE IF NOT EXISTS venda
        (
            id          int auto_increment primary key,
            id_cliente  int   not null,
            valor_total float not null,
            data timestamp not null
        );""")

    def _create_produto_venda_table(self):
        self.my_cursor.execute("""CREATE TABLE IF NOT EXISTS produto_venda
        (
            id         int auto_increment primary key,
            id_produto int   not null,
            id_venda   int   not null,
            quantidade int   not null,
            valor      float not null
        );
        """)
