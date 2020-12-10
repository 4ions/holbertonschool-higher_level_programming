#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    info = dir(hidden_4)
    for i in info:
        if i[-2:] != "__":
            print(i)
