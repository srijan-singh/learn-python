#WAP to read a set of numbers in an array & to find the largest of them.

def largest(arr):
    i = 0
    for elm in arr:
        if i < elm:
            i = elm
    return i 

arr = [3,5,6,18,-11,75]
print(largest(arr))