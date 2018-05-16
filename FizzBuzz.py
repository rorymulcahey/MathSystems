'''

Fizz Buzz: void FizzBuzz(int n)
Give a function that prints "fizz" if divisible by 3, "buzz" if divisible by 5 and "fizz buzz" if divisible by both.

'''


def fizz_buzz(num):
    if num % 3 == 0 and num % 5 != 0:
        print('fizz')
    elif num % 5 == 0 and num % 3 != 0:
        print('buzz')
    elif num % 15 == 0:
        print('fizz buzz')
    else:
        print('zzz')


fizz_buzz(14)
