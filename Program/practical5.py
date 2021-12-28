#WAP to find N! Using function. 

def factorial(num):
    if(num==1):
        return 1
    num *= factorial(num-1)
    return num

num = int(input("Enter the Number: "))
print("The factorial of",num,"is",factorial(num))