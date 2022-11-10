from paprika import *
from database import Database


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
            return None  # TODO wrong login screen

    def atualiza_cadastro(self, bd):  # TODO will not be used in the interface
        novo_nome = input("Insira o novo nome: ")
        if novo_nome.strip() != "":
            self.nome = novo_nome

        novo_email = input("Insira o novo email: ")
        if novo_email.strip() != "":  # TODO validate if email is valid
            self.email = novo_email

        novo_telefone = input("Insira o novo telefone: ")
        if novo_telefone.strip() != "":
            self.telefone = novo_telefone

        nova_senha = input("Insira a nova senha: ")
        if nova_senha.strip() != "":
            self.senha = nova_senha

        bd.update_client(self)
