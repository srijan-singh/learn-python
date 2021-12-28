#WAP to sort a list of names in ascending order

names = input("Enter: ")

names = names.split()

names.sort()

for name in names:
    print(name)