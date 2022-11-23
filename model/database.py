import mysql.connector
from mysql.connector.cursor import MySQLCursor
from mysql.connector import MySQLConnection
from paprika import *
from model.venda import Venda

initial_schema_location: str = "sql_files/initial_schema.sql"
clean_database_location: str = "sql_files/clean_database.sql"


@data
@singleton
class Database:
    my_cursor: MySQLCursor
    mydb: MySQLConnection

    def sell_sale_products(self, venda):
        for id, quantity in Venda.carrinho.items():
            if quantity > 0:
                price = self.get_product_value(id)

                self.decrement_product_quantity(id, quantity)
                query = "INSERT INTO produto_venda (id_produto, id_venda, quantidade, valor)" \
                        "VALUES ('{0}', '{1}', '{2}', '{3}')" \
                    .format(id, venda.id, quantity, quantity * price[0])

                self.my_cursor.execute(query)
                self.mydb.commit()

        return self.my_cursor.lastrowid

    def get_product_value(self, id):
        query = "SELECT valor FROM produto WHERE id = '{0}'"\
            .format(id)
        self.my_cursor.execute(query)

        return self.my_cursor.fetchone()

    def make_sale(self, venda):
        query = "INSERT INTO venda (id_cliente, valor_total, data) " \
                "VALUES ('{0}', '{1}', '{2}')" \
            .format(venda.id_cliente, venda.valor_total, venda.data)

        self.my_cursor.execute(query)
        self.mydb.commit()

        sale_id = self.my_cursor.lastrowid
        venda.id = sale_id

        return sale_id

    def authenticate_client(self, email, password):
        query = "SELECT * FROM cliente WHERE " \
                "email = '{0}' AND senha = '{1}'" \
                .format(email, password)
        self.my_cursor.execute(query)

        return self.my_cursor.fetchone()

    def get_products_id(self):
        query = "SELECT id, 0 FROM produto"
        self.my_cursor.execute(query)

        return self.my_cursor.fetchall()

    def get_products_id_and_quantity(self):
        query = "SELECT id, quantidade FROM produto"
        self.my_cursor.execute(query)

        return self.my_cursor.fetchall()

    def decrement_product_quantity(self, id, quantity):
        query = "UPDATE produto SET quantidade = quantidade - '{0}' " \
                "WHERE id = '{1}'".format(quantity, id)
        self.my_cursor.execute(query)
        self.mydb.commit()

    def find_all_products(self):
        query = "SELECT * FROM produto"
        self.my_cursor.execute(query)

        return self.my_cursor.fetchall()

    def find_product_by_name(self, nome):
        query = "SELECT * FROM produto WHERE nome = '{0}'".format(nome)
        self.my_cursor.execute(query)

        return self.my_cursor.fetchone()

    def create_client(self, client):
        query = "INSERT INTO cliente (cpf, nome, email, telefone, senha, saldo) " \
                "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')" \
            .format(client.cpf, client.nome, client.email, client.telefone, client.senha, client.saldo)

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

        if len(self.find_all_products()) == 0:
            self._create_products()

    def clean_database(self):
        self._execute_sql_script(clean_database_location)

    def _create_connection(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )

        self.my_cursor = self.mydb.cursor(buffered=True)

    def _execute_sql_script(self, file_location):
        with open(file_location, encoding='utf-8') as f:
            query = f.read().replace("\n", "")
            self.my_cursor.execute(query, multi=True)

    def _create_products(self):
        query = "INSERT INTO produto (nome, categoria, descricao, quantidade, valor) " \
                "VALUES (%s, %s, %s, %s, %s)"

        values = [("Coca-Cola", "Bebidas", "Refrigerante gaseificado 2L", 12, 12.0),
                  ("Ruffles", "Snack", "Batata frita 350g", 15, 7.80)]

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
            saldo    float
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
