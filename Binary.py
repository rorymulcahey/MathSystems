'''

The number 4 is expressed in binary as 100. 

What is the number 5267 expressed as in binary?

'''

import math


# def get_binary(num):
#     binary = ['0']
#     index = 0
#     while num > index:
#         print(binary)
#         print(index)
#         for y in range(len(binary)-1, -1, -1):
#             if binary[y] == '0':
#                 binary[y] = '1'
#                 for z in range(y + 1, len(binary)):
#                     binary[z] = '0'
#                 break
#             if binary[y] == '1' and y == 0:
#                 binary.append('0')
#                 for w in range(y + 1, len(binary)):
#                     binary[w] = '0'
#         index += 1
#     binary = ''.join(binary)
#     return binary


def get_binary_fast(num):
    print(num)
    binary = 0
    while num > 0:
        exp = math.floor(math.log(num)/math.log(2))
        binary += 10**exp
        num -= 2**exp
    return binary


def find_binaries(lst):
    for x in range(0, lst):
        print(get_binary_fast(x))


def decimal(binary):
    num = 0
    binary = str(binary)
    binary = list(binary)
    for x in range(0, len(binary)):
        if binary[x] == '1':
            num += 2**(len(binary)-1-x)
    return num


# find_binaries(10000000)
print(get_binary_fast(1000))
print(decimal(1111101000))

