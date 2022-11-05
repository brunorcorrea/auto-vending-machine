from paprika import *


@data
class ProdutoCarrinho:
    id: int
    id_cliente: int
    id_produto: int
    quantidade: int
    valor: float
