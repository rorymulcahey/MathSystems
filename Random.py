'''

Random Number: int GetRandom(int seed)
Give a random function.

'''

seed = input("Give a seed integer ")
type(seed)

const = int(seed)
const = const%4 + 3 + 0.54
# const = int(const)
print(const)
for x in range(0, 10):
    y = 0.5
    index = 0
    while index < x:
        # print(y)
        y = const * y * (1 - y)
        index += 1
    y = int(y)
    print(x, int(y%10))

