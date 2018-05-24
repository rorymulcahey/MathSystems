'''

Random Number: int GetRandom(int seed)
Give a random function.

'''

import datetime
from random import randint

# seed = input("Give a seed integer ")
# type(seed)

# import time
# seed = int(round(time.time() * 1000))


def create_seed():
    seed_date = datetime.datetime.fromtimestamp(1011286793)
    now = datetime.datetime.now()
    seconds = (now - seed_date).total_seconds()
    seed = seconds*10000 + 579127
    return seed


def get_random(seed):
    y = 0
    const = int(seed)
    const = const % 100000000/10000000000 + 4.25
    for x in range(0, 7):
        y = 0.5
        index = 0
        while index < x:
            y = const * y * (1 - y)
            index += 1
        y = int(y)
    return int(y % 10)


lst = [0] * 10
lst2 = [0] * 10
for z in range(0, 100000):
    new_seed = create_seed()
    random_num = get_random(new_seed)
    lst[int(random_num)] += 1
    temp = randint(0, 9)
    lst2[temp] += 1
print("My Function: ", lst)
print("Python Function: ", lst2)
