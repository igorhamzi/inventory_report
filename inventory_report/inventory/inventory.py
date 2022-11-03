from csv import DictReader
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport
import json
import xmltodict


class Inventory:

    @classmethod
    def reading_files(cls, path):
        file_type = path[-4::]

        if file_type == '.csv':
            with open(path, 'r') as file:
                list_of_products = list(DictReader(file))
        elif file_type == 'json':
            with open(path, 'r') as file:
                list_of_products = json.load(file)
        elif file_type == '.xml':
            with open(path, 'r') as file:
                list_of_products = xmltodict.parse(
                    file.read())["dataset"]["record"]

        return list_of_products

    @classmethod
    def import_data(cls, path, inventory):

        if inventory == 'simples':
            return SimpleReport.generate(Inventory.reading_files(path))
        elif inventory == 'completo':
            return CompleteReport.generate(Inventory.reading_files(path))


if __name__ == '__main__':
    Inventory.import_data('inventory_report/data/inventory.xml', 'completo')

    print(__name__)
