from database import *
from cliente import Cliente
from venda import Venda

import time
from datetime import datetime


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


def remover_produto_carrinho(nome):
    produto_banco = bd.find_product_by_name(nome)
    if produto_banco is not None:
        for i in range(len(produto_banco)):
            if type(produto_banco[i]) == float:
                id_produto = produto_banco[0]
                qtd_produto = estoque.get(id_produto)
                if estoque.get(id_produto) > 0:
                    Venda.valor_total -= produto_banco[i]
                    Venda.carrinho[id_produto] -= 1

                    estoque.pop(id_produto)
                    estoque.update({id_produto: qtd_produto + 1})
                # TODO else return error
                break


def adicionar_produto_carrinho(nome):
    global estoque
    produto_banco = bd.find_product_by_name(nome)
    if produto_banco is not None:
        for i in range(len(produto_banco)):
            if type(produto_banco[i]) == float:
                id_produto = produto_banco[0]
                qtd_produto = estoque.get(id_produto)
                if qtd_produto > 0:
                    Venda.valor_total += produto_banco[i]
                    Venda.carrinho[id_produto] += 1

                    estoque.pop(id_produto)
                    estoque.update({id_produto: qtd_produto - 1})
                    break
                else:
                    print("We are out of {0}".format(nome))
                # TODO else return error


def finalizar_compra():
    venda = Venda()
    venda.data = datetime.fromtimestamp(time.time())
    venda.id_cliente = cli.id
    venda.valor = Venda.valor_total

    if cli.saldo >= venda.valor:
        bd.make_sale(venda)
        cli.saldo -= venda.valor
        bd.update_client_balance(cli)
        bd.sell_sale_products(venda)

        Venda.valor_total = 0.0
        Venda.carrinho = dict((x, y) for x, y in bd.get_products_id())
    # TODO else return not enough balance


if __name__ == '__main__':
    global estoque
    global cli
    bd = Database()
    bd.create_database()
    # cli = mock_cliente(bd)
    estoque = dict((x, y) for x, y in bd.get_products_id_and_quantity())
    Venda.carrinho = dict((x, y) for x, y in bd.get_products_id())

    email = "bruno@email.com"
    senha = "12345"
    cli = Cliente.autentica_cliente(bd, email, senha)

    adicionar_produto_carrinho("Coca-Cola")
    adicionar_produto_carrinho("Coca-Cola")
    adicionar_produto_carrinho("Ruffles")
    adicionar_produto_carrinho("Ruffles")
    adicionar_produto_carrinho("Ruffles")

    remover_produto_carrinho("Ruffles")

    finalizar_compra()
