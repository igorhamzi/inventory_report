from datetime import datetime
from collections import Counter


class SimpleReport:

    @classmethod
    def generate(cls, list):
        oldest_manufacturing_date = min([product['data_de_fabricacao']
                                        for product in list
                                         ])

        current_day = str(datetime.today())

        closest_expiration_date = min([product['data_de_validade']
                                      for product in list
                                      if product['data_de_validade'] >
                                      current_day])

        companies = [product['nome_da_empresa']
                     for product in list
                     ]

        company_more_products = Counter(companies).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {company_more_products}"
        )


if __name__ == '__main__':
    SimpleReport.generate(
        '/home/igor/trybe/projetos-19'
        '/cs-modulo/inventory-report'
        '/sd-019-c-inventory-report'
        '/inventory_report/data/inventory.json'
    )

    print(__name__)
