def identity(x):
    return x 
def increment(x):
    return x + 1

def intrsct(f, x):
    def at_x(g):
        return f(x) == g(x)
    return at_x 

at_3 = intrsct(square, 3)
print(at_3(triple))

print(at_3(increment))