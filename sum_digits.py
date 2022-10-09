def sum_digits(n):
    def helper(total, n):
        if n == 0:
            return total
        return helper(total + n % 10, n // 10)
    return helper(0, n)

print(sum_digits(123))

#or

def sum_digits(n):
    tot, i = 0, n
    while (i > 0):
        tot = tot + n % 10
        i = i // 10
    return tot 

sum_digits(123)
