'''

Conway Sequence: string[] GetConwaySequence(int n)
Give a function that calculates the n-th Conway sequence number.

'''


# def conway_sequence(instances, digit):
#     digit = str(digit)
#     output = [digit]
#     new_output = [digit]
#     for x in range(0, instances):
#         print('instance', x)
#         index = 1
#         new_output = []
#         y = 0
#         # subtracting index does not work as I expect it
#         # for y in range(0, len(output)-index+1):
#         while y < len(output)-index+1:
#             print('y val', y)
#             print('for y')
#             index = 1
#             number_of_instances = 1
#             current_digit = output[y]
#             if len(output) > (y + index) and current_digit == output[y+index]:
#                 while len(output) > (y + index) and current_digit == output[y+index]:
#                     print('while')
#                     print(output)
#                     number_of_instances += 1
#                     index += 1
#                 new_output = [str(number_of_instances)] + [current_digit]
#                 y += 1
#                 print('current index', index)
#                 print('len output', len(output))
#             # elif len(output) > (y + index) and current_digit != output[y+index]:
#             #     new_output = [current_digit] + output
#             else:
#                 new_output = [current_digit] + output
#                 y += 1
#                 break
#         output = new_output
#         print(new_output)
#     print(new_output)
#
#
# conway_sequence(3, 1)


def conway(instances, digit):
    digit = str(digit)
    output = [digit]
    new_output = output
    print(output)
    for x in range(0, instances-1):
        digit_index = 0
        new_output = []
        while len(output) > digit_index:
            current_digit = output[digit_index]
            instances = 1
            while len(output) > digit_index + 1 and current_digit == output[digit_index + 1]:
                instances += 1
                digit_index += 1
            new_output = new_output + [str(instances)] + [str(current_digit)]
            digit_index += 1
        output = new_output
        print(output)
    return new_output


conway(7, 3)
