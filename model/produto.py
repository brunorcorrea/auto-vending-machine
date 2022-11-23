from paprika import *


@data
class Produto:
    id: int
    nome: str
    categoria: str
    descricao: str
    quantidade: int
    valor: float
