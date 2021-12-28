#Write a Function to swap values of a pair of integers.

def swap(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp
    return num1, num2 

num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))

print("Before Swap:", num1,num2)

num1,num2 = swap(num1,num2)

print("After Swap:", num1,num2)