# Declaro variables globales
ROOT_DIR = "name_processor"
FOLDER = "files"
FILE = 'names.txt'
ROOT_COMPLETE = f"./{ROOT_DIR}/{FOLDER}/{FILE}"

def show():
    with open(ROOT_COMPLETE, 'r', encoding='utf-8') as file:
        # list_name = [ f'{i}\n' for i in file ]
        list_name = "\nLista de nombres:\n"
        indice = 1
        for i in file:
            list_name += f"{indice}.- {i.strip()}\n"
            indice += 1
        return list_name, True