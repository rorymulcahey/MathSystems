'''

Roman Numeral Converter: int GetIntegerValue(string value)
Give a function to convert a Roman numeral to a base-10 integer.

To do: OOP the roman numeral to base ten, then send it to is valid for checking
'''


def roman_to_decimal(letters):
    num = 0
    for x in range(0, len(letters)):
        if x+1 < len(letters):
            if letters[x] == 'I' and (letters[x+1] == 'V' or letters[x+1] == 'X'):
                num -= add_int(letters[x])
            elif letters[x] == 'V' and (letters[x+1] == 'X' or letters[x+1] == 'L'):
                num -= add_int(letters[x])
            elif letters[x] == 'X' and (letters[x+1] == 'L' or letters[x+1] == 'C'):
                num -= add_int(letters[x])
            elif letters[x] == 'L' and (letters[x+1] == 'C' or letters[x+1] == 'D'):
                num -= add_int(letters[x])
            elif letters[x] == 'C' and (letters[x+1] == 'D' or letters[x+1] == 'M'):
                num -= add_int(letters[x])
            elif letters[x] == 'D' and letters[x+1] == 'M':
                num -= add_int(letters[x])
            else:
                num += add_int(letters[x])
        else:
            num += add_int(letters[x])
    return num


def add_int(roman):
    if roman == 'M':
        return 1000
    elif roman == 'D':
        return 500
    elif roman == 'C':
        return 100
    elif roman == "L":
        return 50
    elif roman == "X":
        return 10
    elif roman == "V":
        return 5
    elif roman == "I":
        return 1


def is_valid(roman):
    for x in range(0, len(roman)-1):
        current_letter = roman[x]
        instances = 1
        occurrences = 0
        # duplicates = 0
        w, y, z = x, x, x
        if x+1 < len(roman) and add_int(current_letter)**10 < add_int(roman[x+1]):
            return False
        # while w+1 < len(roman) and add_int(current_letter) < add_int(roman[w+1]):
        #     print('test')
        #     w += 1
        #     duplicates += 1
        #     if duplicates == 2:
        #         return False
        while y+1 < len(roman) and current_letter == roman[y+1]:
            instances += 1
            y += 1
            if instances == 4:
                return False
        while z+1 < len(roman) and add_int(current_letter) < add_int(roman[z+1]):
            occurrences += 1
            z += 1
            if occurrences == 2:
                return False
    return True


# try:
#     roman_numeral = ''
#     while roman_numeral is not 0:
#         roman_numeral = input('Type a Roman Numeral: ')
#         roman_numeral = list(roman_numeral.upper())
#         if is_valid(roman_numeral):
#             roman_numeral = roman_to_decimal(roman_numeral)
#             print(roman_numeral)
#         else:
#             print('Not a valid number')
#             break
# except SyntaxError:
#     roman_numeral = None

roman_numeral = ''
while roman_numeral is not 0:
    roman_numeral = input('Type a Roman Numeral: ')
    roman_numeral = list(roman_numeral.upper())
    if is_valid(roman_numeral):
        roman_numeral = roman_to_decimal(roman_numeral)
        print(roman_numeral)
    else:
        print('Not a valid number')
        break

