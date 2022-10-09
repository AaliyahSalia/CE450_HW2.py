def sum_num(n):
    if n == 0 or n == 1:
        return n
    return n + sum_num(n-2)

num = int(input("Please enter a number: "))
print(sum_num(num))

