def func(n):
    if n <= 1:
        return 1
    else:
        return n * func(n - 2)
    
def cal(n):
    if n % 2 == 0:
        print(0)
    else:
        num1 = func(n)
        print(num1)
         

n = int(input("Please enter a number: "))
print(cal(n))