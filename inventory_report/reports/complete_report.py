from ..reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):

    @classmethod
    def generate(cls, list):

        companies = [product['nome_da_empresa']
                     for product in list
                     ]

        company_products = Counter(companies).most_common()

        string_result = '\nProdutos estocados por empresa:\n'

        for comapany in company_products:
            name_company = comapany[0]
            quantity_products = comapany[1]
            string_result += f'- {name_company}: {quantity_products}\n'

        return super().generate(list) + string_result


if __name__ == '__main__':
    CompleteReport.generate(
        '/home/igor/trybe/projetos-19'
        '/cs-modulo/inventory-report'
        '/sd-019-c-inventory-report'
        '/inventory_report/data/inventory.json'
    )

    print(__name__)
