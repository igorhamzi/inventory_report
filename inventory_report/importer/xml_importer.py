from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".xml"):
            with open(path) as file:
                doc = xmltodict.parse(file.read())
                return doc["dataset"]["record"]
        else:
            raise ValueError("Arquivo inválido")
