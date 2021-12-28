#WAP to print Fibonacci series of n numbers, where n is given by the programmer.
def fibonacci(num):
    if(num<=1):
        return 1
    return fibonacci(num-1) + fibonacci(num-2)

def fibonacci_series(num):
    for i in range(num+1):
        print(fibonacci(i), end=" ")

num = int(input("Enter the Term: "))
fibonacci_series(num)
