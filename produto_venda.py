from paprika import *


@data
class ProdutosVendidos:
    id: int
    id_cliente: int
    id_venda: int
    quantidade: int
    valor: float
