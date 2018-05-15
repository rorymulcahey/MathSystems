'''

The number 4 is expressed in binary as 100. 

What is the number 5267 expressed as in binary?

'''


def get_binary(num):
    binary = ['0']
    index = 0
    while num > index:
        print(binary)
        print(index)
        for y in range(len(binary)-1, -1, -1):
            if binary[y] == '0':
                binary[y] = '1'
                for z in range(y + 1, len(binary)):
                    binary[z] = '0'
                break
            if binary[y] == '1' and y == 0:
                binary.append('0')
                for w in range(y + 1, len(binary)):
                    binary[w] = '0'
        index += 1
    binary = ''.join(binary)
    return binary


binary_num = get_binary(5267)
print(binary_num)