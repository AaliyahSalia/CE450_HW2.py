def identity(x):
    return x
def increment(x):
    return x + 1

def square(x):
    return pow(x, 2)

def triple(x):
    return x * 3

def intersects(f, x):

    def at_x(g):
        return f(x) == g(x)
    return at_x 

at_three = intersects(square, 3)

print(at_three(triple))
print(at_three(increment))
print(at_three(identity))