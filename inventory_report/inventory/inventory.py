from csv import DictReader
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class inventory:

    @classmethod
    def import_data(cls, path, inventory):
        with open(path, 'r') as file:
            list_of_products = list(DictReader(file))

        if inventory == 'simples':
            return SimpleReport.generate(list_of_products)
        elif inventory == 'completo':
            return CompleteReport.generate(list_of_products)


if __name__ == '__main__':
    inventory.import_data(
        '/home/igor/trybe/projetos-19'
        '/cs-modulo/inventory-report'
        '/sd-019-c-inventory-report'
        '/inventory_report/data/inventory.csv',
        'completo'
    )

    print(__name__)
