# Declaro variables globales
ROOT_DIR = "name_processor"
FOLDER = "files"
FILE = 'names.txt'
ROOT_COMPLETE = f"./{ROOT_DIR}/{FOLDER}/{FILE}"

def new(name):
    # Validar que el nombre no este repetido
    with open(ROOT_COMPLETE, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            if name in line:
                return f"Nombre repetido '{name}'", True
            else:
                with open(ROOT_COMPLETE, 'a', encoding='utf-8') as file:
                    file.write(f'{name}\n')
                    return f"Se agrego '{name}'", True