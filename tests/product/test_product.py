from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product()
    assert type(product.id) == int
    assert type(product.nome_do_produto) == str
    assert type(product.nome_da_empresa) == str
    assert type(product.data_de_fabricacao) == str
    assert type(product.data_de_validade) == str
    assert type(product.numero_de_serie) == str
    assert type(product.instrucoes_de_armazenamento) == str
