'''

Fibonacci Numbers: int GetFibonacciNumber(int n)
Give a function that calculates the n-th Fibonacci number.

'''


def fibonacci(num):
    int1 = 0
    int2 = 1
    fibo = 0
    for x in range(0, num):
        fibo = int1 + int2
        int1 = int2
        int2 = fibo
    print(int1)


fibonacci(5)
