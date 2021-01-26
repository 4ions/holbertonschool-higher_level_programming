#!/usr/bin/python3
""" 11-main """
from models.square import Square

if __name__ == "__main__":

    s = Square(1, 1, 1, 1)
    
    try:
        s.update(size="hello")
        print("Exitoso")
    except:
        print("no se puede")
    print(s)
    s_dictionary = s.to_dictionary()
    print(s_dictionary)
