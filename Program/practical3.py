#WAP to find, a given number is PRIME or NOT.

num = int(input("Enter Number: "))

is_prime = True

for i in range(2, num):
    if(num%i==0):
        is_prime = False
        print(i,"*",num//i,"=",num)
        print(num,"is not prime!")
        break
    
if(is_prime):
    print(num,"is prime!")
