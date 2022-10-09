from functools import reduce

def foo(*func):
      
    def compose(f, g):
        return lambda x : f(g(x))
              
    return reduce(compose, func, lambda x : x)

n = int(input("Please enter a number: "))
  
def add(x):
    return x + 1

def incr(x):
    num1 = int(input("Please enter a number to increment: "))
    return x + num1
  
  
def triple(x):
    num2 = int(input("Please enter a number to triple: "))
    return x ** num2
   
  
def square(x):
    num3 = int(input("Please enter a number to square: "))
    return x ** num3
   



fooResult = foo(add, incr)  + foo(triple, square)
  
print("The result is: ", fooResult())



