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

    def autentica_cliente(self, email: str, senha: str):  # TODO change to database values
        if self.senha == senha and self.email == email:
            return True

        return False

    def atualiza_cadastro(self, bd):
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
