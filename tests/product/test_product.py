from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        9,
        "farinha",
        "Farinini",
        "01-05-2021",
        "02-06-2023",
        "1234567",
        "ao abrigo de luz",
    )
    assert product.id == 9
    assert product.nome_do_produto == 'farinha'
    assert product.nome_da_empresa == 'Farinini'
    assert product.data_de_fabricacao == '01-05-2021'
    assert product.data_de_validade == '02-06-2023'
    assert product.numero_de_serie == '1234567'
    assert product.instrucoes_de_armazenamento == 'ao abrigo de luz'
