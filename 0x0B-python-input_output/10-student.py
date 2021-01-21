#!/usr/bin/python3
""" module of students """


class Student:
    """ Class of stundents """

    def __init__(self, first_name, last_name, age):
        """ Initialice the variables """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return the information of list """
        # En caso de ser None necesitamos que nos regres todos
        # los atributos que tengan los diccionarios o listas
        if attrs is None:
            return self.__dict__
        else:
            # guardo el self.__dict__ en una variable para manejarla
            # de mejor manera
            dictio = self.__dict__
            # ciclo for para traer la informacion de todas las llaves
            # y valores que tenga el dictionario y retornar este, usamos
            # self.__dict__ para que este muestre la informacion del
            # diccionario, es decir en el ejemplo 2 nos dan que attrs
            # es decir atributos sean first_name y age, entonces estos
            # seran los que se guardaran en el diccionario que declaramos
            # abajo y retornamos esta informacion
            dictio_2 = dict(([i, j] for i, j in dictio.items() if i in attrs))
            return dictio_2
