def a_func(n):
    if n <= 3:
        return n
    return (a_func(n-1)+(2*a_func(n-2))+(3*a_func(n-3)))

num = int(input("Please enter a number: "))
<<<<<<< HEAD
print(a_func(num))
=======
print(a_func(num))
>>>>>>> 45275e1 (My commit)
