'''

Roman Numeral Converter: int GetIntegerValue(string value)
Give a function to convert a Roman numeral to a base-10 integer.

'''


# def roman_to_decimal(letters):
#     num = 0
#     letters = list(letters.upper())
#     x = 0
#     while x < len(letters):
#         if letters[x] == 'I' and letters[x+1] != 'V':
#             num += 1
#             x += 1
#         elif letters[x] == 'I' and letters[x+1] == 'V':
#             num += 4
#             x += 2
#         else:
#             print('Invalid Syntax')
#             num = 0
#             break
#     print(num)
#
#
# roman_to_decimal('IIIIIiiiV')


def roman_to_decimal(letters):
    num = 0
    letters = list(letters.upper())
    for x in range(0, len(letters)):
        if x+1 < len(letters) and letters[x] == 'I' and letters[x+1] == 'V':
            num -= add_int(letters[x])
        else:
            num += add_int(letters[x])

    print(num)


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


roman_to_decimal('IV')
