from paprika import *


@data
class Cliente:
    id: int
    cpf: int
    nome: str
    email: str
    telefone: str
    senha: str
    saldo: float

    def __aumenta_saldo__(self, value: float):
        if value > 0:
            self.saldo += value

    def __autentica_cliente__(self, email: str, senha: str):
        if self.senha == senha and self.email == email:
            return True

        return False

    def __atualiza_cadastro__(self):
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
