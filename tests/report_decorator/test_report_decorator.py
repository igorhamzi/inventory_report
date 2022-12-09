from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


my_product = [
        {
            "id": "1",
            "nome_do_produto": "Pilha AA",
            "nome_da_empresa": "Panasonic",
            "data_de_fabricacao": "2020-01-15",
            "data_de_validade": "2025-01-15",
            "numero_de_serie": "xpto12345",
            "instrucoes_de_armazenamento": "Manter em local seco"
        }
    ]


def test_decorar_relatorio():
    colored_report = ColoredReport(SimpleReport).generate(my_product)

    assert colored_report == (
        "\033[32mData de fabricação mais antiga:\033[0m"
        " \033[36m2020-01-15\033[0m\n"
        "\033[32mData de validade mais próxima:\033[0m"
        " \033[36m2025-01-15\033[0m\n"
        "\033[32mEmpresa com mais produtos:\033[0m"
        " \033[31mPanasonic\033[0m"
    )
