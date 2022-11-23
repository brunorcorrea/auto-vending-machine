from paprika import *
from model.database import Database

global starter_balance
starter_balance = 300


@data
class Cliente:
    id: int
    cpf: str
    nome: str
    email: str
    telefone: str
    senha: str
    saldo: float

    def aumenta_saldo(self, value: float, bd):
        if value > 0:
            self.saldo += value
            bd.update_client_balance(self)

    @staticmethod
    def autentica_cliente(email: str, senha: str):
        bd = Database()
        cliente_salvo = bd.authenticate_client(email, senha)
        if cliente_salvo is not None:
            cliente = Cliente()
            cliente.id = cliente_salvo[0]
            cliente.cpf = cliente_salvo[1]
            cliente.nome = cliente_salvo[2]
            cliente.email = cliente_salvo[3]
            cliente.telefone = cliente_salvo[4]
            cliente.senha = cliente_salvo[5]
            cliente.saldo = cliente_salvo[6]

            return cliente
        else:
            return None

    @staticmethod
    def cria_cliente(nome, cpf, email, telefone, senha):
        bd = Database()
        cliente = Cliente()
        cliente.nome = nome
        cliente.cpf = cpf
        cliente.email = email
        cliente.telefone = telefone
        cliente.senha = senha
        cliente.saldo = starter_balance
        cliente.id = bd.create_client(cliente)

        return cliente
