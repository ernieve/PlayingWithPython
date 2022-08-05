from modules import search, insert, display
# Modulo para crear directorios, revisar archivos
import os

# Declaro variables globales
ROOT_DIR = "name_processor"
FOLDER = "files"
FILE = 'names.txt'
ROOT_COMPLETE = f"./{ROOT_DIR}/{FOLDER}/{FILE}"

def find():
    msg = "¿Cual es el nombre que deseas buscar?\n>>> "
    name = input(msg)
    name = name.replace(' ','').strip()
    print(name)
    while len(name) < 2 or not name.isalpha():
        print(f'No valido\n')
        name=input(msg)
        name = name.replace(' ','').strip()
    result = search.find(name.capitalize())
    return result

def new():
    msg = "¿Cual nombre deseas agregar?\n>>> "
    name = input(msg)
    name = name.replace(' ','').strip()
    while len(name.replace(' ','')) < 2 or len(name.replace(' ','')) > 25 or not name.isalpha():
        print('No valido\n')
        name = input(msg)
        name = name.replace(' ','').strip()
    result = insert.new(name.capitalize())
    return result

def show():
    result = display.show()
    return result

def delete():
    pass

def exit():
    return f'¡Adios!\n', False

def menu():
    # Inicializo la variable status que sera la condicional para salir del bucle general
    status = True
    option = {
        1 : show,
        2 : new,
        3 : delete,
        4 : find,
        5 : exit,
    }

    #Mientras STATUS sea True se sigue ejecutando
    while status:
        # Genero el menu de opciones
        menu="Elige una opcion valida:\n1.- Mostrar nombres\n2.- Agregar nombre\n3.- Borrar nombre\n4.- Buscar en lista\n5.- Salir\n>>> "
        
        # Solicito por pantalla el ingreso de la opcion
        selection = input(menu)
        
        # Mientras el valor ingresado no sea numero o el numero sea menor a uno o mayor a 4 queda en el bucle
        while not selection.isnumeric() or int(selection) < 1 or int(selection) > 4:
            print(f"'{selection.upper()}' no es valido\n")
            selection = input(menu)
        # Una vez que se ingresa una opcion valida se convierte el valor ingresado en entero
        selection = int(selection)
        
        # Ejecuto la opcion del usuario ingresando al diccionario segun la clave indicada
        action=option[selection]()
        
        # Muestro el mensaje que retorna la funcion
        print(action[0])
        # Actualizo el valor de STATUS
        status = action[1]

def main():
    # Reviso si el directorio existe o no en la misma ruta donde esta el script, sino existe lo crea
    folder = os.listdir(ROOT_DIR)
    if not folder.__contains__(FOLDER):
        os.mkdir(f'{ROOT_DIR}/{FOLDER}')

    # Reviso si el archivo existe en el directorio files, sino existe lo crea
    directory = os.listdir(f"{ROOT_DIR}/{FOLDER}")
    if not directory.__contains__('names.txt'):
        with open(f"{ROOT_COMPLETE}", "w", encoding="utf-8") as file:
            print(f"Success, {FILE} created")
            
    # Luego de validar la existencia del archivo entra al menu
    menu()

if __name__ == "__main__":
    main()