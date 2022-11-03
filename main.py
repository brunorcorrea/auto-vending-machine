from database import *
from cliente import Cliente


def mock_cliente(bd):
    cli = Cliente(
        cpf="47048952612",
        nome="Bruno",
        email="bruno@email.com",
        telefone="23934567645",
        senha="12345",
        saldo=0.0
    )  # TODO create method to create Cliente?

    bd.create_client(cli)

    cli.aumenta_saldo(200, bd)

    return cli


def adicionar_produto_carrinho(nome):
    produto_banco = bd.find_product_by_name(nome[0])
    # TODO get quantity and increment value

if __name__ == '__main__':
    carrinho = []
    bd = Database()
    bd.create_database()
    cli = mock_cliente(bd)

    adicionar_produto_carrinho("Coca-Cola")
    adicionar_produto_carrinho("Ruffles")


    print(carrinho)

    print(cli)
