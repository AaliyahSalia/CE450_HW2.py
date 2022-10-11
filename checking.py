from tabnanny import check


def checking(x):
    base = 10
    while (x):
        result = x % 10
        x /= 10
        if result > base:
            return False
        base = result 
    return True

num = int(input("Please enter a number: "))
print(checking(num))