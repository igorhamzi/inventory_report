import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")

    _, path, type = sys.argv

    if path.endswith(".csv"):
        return sys.stdout.write(
            InventoryRefactor(CsvImporter).import_data(path, type)
        )
    if path.endswith(".json"):
        return sys.stdout.write(
            InventoryRefactor(JsonImporter).import_data(path, type)
        )

    if path.endswith(".xml"):
        return sys.stdout.write(
            InventoryRefactor(XmlImporter).import_data(path, type)
        )
