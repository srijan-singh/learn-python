#WAP to read a set of numbers from keyboard & to find the sum of all elements of the given array using a function.

def sum_of_all(arr):
    result = 0
    for elm in arr:
        result+=elm
    return result

size = int(input("Size: "))
arr = []

for i in range(size):
    arr.append(int(input("Enter Value: ")))

print(sum_of_all(arr))

