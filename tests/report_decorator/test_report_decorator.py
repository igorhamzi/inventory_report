from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    product_mock = [{
       "id": 13,
       "nome_do_produto": "Teia do miranha",
       "nome_da_empresa": "Stark-Inc",
       "data_de_fabricacao": "04-11-2022",
       "data_de_validade": "01-11-2020",
       "numero_de_serie": "1313",
       "instrucoes_de_armazenamento": "Este lado para cima"
     }]

    expected_colored = (
        "\033[32mData de fabricação mais antiga:\033[0m"
        " \033[36m04-11-2022\033[0m\n"
        "\033[32mData de validade mais próxima:\033[0m"
        " \033[36m01-11-2020\033[0m\n"
        "\033[32mEmpresa com mais produtos:\033[0m"
        " \033[31mStark-Inc\033[0m"
        )

    coloredReport = ColoredReport(SimpleReport)

    assert expected_colored == coloredReport.generate(product_mock)
