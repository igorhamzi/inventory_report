from csv import DictReader
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport
import json


class inventory:

    @classmethod
    def import_data(cls, path, inventory):
        file_type = path[-4::]

        if file_type == '.csv':
            with open(path, 'r') as file:
                list_of_products = list(DictReader(file))
        elif file_type == 'json':
            with open(path, 'r') as file:
                list_of_products = json.load(file)

        if inventory == 'simples':
            return print(SimpleReport.generate(list_of_products))
        elif inventory == 'completo':
            return print(CompleteReport.generate(list_of_products))


if __name__ == '__main__':
    inventory.import_data('inventory_report/data/inventory.csv', 'simples')

    print(__name__)
