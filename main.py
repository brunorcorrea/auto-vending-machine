from database import *
from cliente import Cliente

if __name__ == '__main__':
    my_cursor = database.create_connection()
    database.create_database(my_cursor)

    cli = Cliente(1,
                  "470.489.526-12",
                  "Bruno",
                  "bruno@email.com",
                  "23934567645",
                  "12345",
                  0.0
                  )  # TODO create method to create Cliente?

    Database.create_cliente(cli, my_cursor)

    print(cli)

    cli.__atualiza_cadastro__()

    print(cli)
