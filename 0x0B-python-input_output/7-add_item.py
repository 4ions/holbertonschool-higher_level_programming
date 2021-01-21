#!/usr/bin/python3
""" Module to load, add, and save """
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def app():
    """adds input args to file"""
    try:
        # tratar de cargar con la funcion que se trae del
        # archivo 6
        a_list = load_from_json_file('./add_item.json')
    except:
        # en caso de que no se puede cargar se crea una
        # lista vacia para poder almacenar los datos
        a_list = []
    # guardar todos los datos que se hallan escrito al momento
    # de la ejecucion que se encuentran almacenados en argv
    for i in range(1, len(argv)):
        a_list.append(argv[i])
    # usamos la funcion save para ingresar estos datos guardados
    # en la lista para generarlos en el archivo
    save_to_json_file(a_list, './add_item.json')

# Para proteger el doble ingreso al script
if __name__ == '__main__':
    app()
