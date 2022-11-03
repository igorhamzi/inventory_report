from csv import DictReader
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport
import json
import xmltodict


class Inventory:

    @classmethod
    def import_data(cls, path, inventory):
        file_type = path[-4::]

        if file_type == '.csv':
            with open(path, 'r') as file:
                list_of_products = list(DictReader(file))
        elif file_type == 'json':
            with open(path, 'r') as file:
                list_of_products = json.load(file)
        elif file_type == '.xml':
            with open(path, 'r') as file:
                read_list = xmltodict.parse(file.read())["dataset"]["record"]
                list_of_products = read_list

        if inventory == 'simples':
            return SimpleReport.generate(list_of_products)
        elif inventory == 'completo':
            return CompleteReport.generate(list_of_products)


if __name__ == '__main__':
    Inventory.import_data('inventory_report/data/inventory.xml', 'completo')

    print(__name__)
