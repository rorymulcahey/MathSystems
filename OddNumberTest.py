'''

Odd Number Tester: bool IsOdd(int n)
Give a function that returns true if the number is odd and false if even.

'''


def odd_number_test(num):
    boolean = num % 2 == 1
    return boolean


print(odd_number_test(2))
