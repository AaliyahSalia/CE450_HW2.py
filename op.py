#This code is only for positive integers


def op():
    a = int(input("Please enter a number for a: "))
    b = int(input("Please enter a number for b: "))
    c = int(input("Please enter a number for c: "))

    while a > -1:
        return a * b + c
           
print(op())