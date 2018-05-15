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
#
#
# binary_num = get_binary(1000000)
# print(binary_num)
# print('11110100001001000000')
# print(math.log(1000000)/math.log(2))
# print(2**20)


def get_binary_fast(num):
    binary = 0
    while True:
        if num == 0:
            return 0
        exp = math.ceil(math.log(num)/math.log(2))
        print(exp)
        if num == 2**exp:
            binary += 10**exp
            return binary
        binary += 10**exp
        num -= 2**(exp-1)
        print(num)


binary_num = get_binary_fast(5267)
print(binary_num)
# print(2**7)
# print(math.ceil(math.log(2**7)/math.log(2)))