# Declaro variables globales
ROOT_DIR = "name_processor"
FOLDER = "files"
FILE = 'names.txt'
ROOT_COMPLETE = f"./{ROOT_DIR}/{FOLDER}/{FILE}"

def find(name):
    with open(ROOT_COMPLETE, 'r', encoding='utf-8') as file:
        # data_file = file.readlines()
        for line in file.readlines():
            if name in line:
            #if line == name:
                return f"Exist '{name}'\n", True
            else:
                return f"Don't exists '{name}'\n", True