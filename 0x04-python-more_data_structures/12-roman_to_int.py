#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    if isinstance(roman_string, str):
        for i in range(len(roman_string)):
            if roman_string[i] == "I":
                try:
                    if roman_string[i + 1] in 'VX':
                        result -= 1
                    else:
                        result += 1
                except:
                    result += 1
            if roman_string[i] == "V":
                result += 5
            if roman_string[i] == "X":
                try:
                    if roman_string[i + 1] == "C":
                        result -= 10
                    else:
                        result += 10
                except:
                    result += 10
            if roman_string[i] == "L":
                result += 50
            if roman_string[i] == "C":
                try:
                    if roman_string[i + 1] in 'DM':
                        result -= 100
                    else:
                        result += 100
                except:
                    result += 100
            if roman_string[i] == "D":
                result += 500
            if roman_string[i] == "M":
                result += 1000
    return(result)
