from paprika import *


@data
class Venda:
    id: int
    id_cliente: int
    data: float
    valor: float
    valor_total = 0.0
    carrinho = dict()  # TODO will conflict when save?
