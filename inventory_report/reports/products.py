from functools import lru_cache
import json


@lru_cache
def read(path):
    try:
        with open(path, 'r') as file:
            products = json.load(file)
    except FileNotFoundError:
        print('O arquivo não foi encontrado')
    except json.decoder.JSONDecodeError:
        print('tem alguma coisa errada com o arquivo')

    return products
