def pay_change(paid, price):
    # set up the change and an empty dictionary for result
    global change
    change = paid - price
    bills = ['$20', '$10', '$5', '$2', '$1']

    # create a function to calculate the change for each bills
    def f(x):
        global change
        result = divmod(change, x)[0]
        change = divmod(change, x)[1]
        return result
    temp = list(map(f, (20, 10, 5, 2, 1)))

    # generate the final result as a dictionary
    result = dict(zip(bills, temp))

    # present the result, do not show if value is 0
    for k, v in result.items():
        if v != 0:
            print('Need', v, 'bills of', k)

pay_change(4, 6)

-----


def is_prime():
    def helper(i):
        if i == 0:
            return False
        elif i == 1:
            return True
        elif n % i == 0:
            return False
        return helper(i - 1)
    return helper (n - 1)

n = int(input("Please enter a number: "))
print(is_prime())

Define a function cnt_primes(m), where m is a 
positive integer and returns the number of prime 
integers from 1 to m in function RECURSION only, 
given that a function is_prime(n) has been defined. 
>>> cnt_primes(6) # 1, 2, 3, 4, 5, 6 
>>> 3  # 3 prime numbers from 1 to 6

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

  def count_Primes_nums(n):
    ctr = 0
    
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            ctr += 1

    return ctr

print(count_Primes_nums(10))
print(count_Primes_nums(100))

-----

If "f" is a function and n is a positive integer, 
then we can form the nth repeated application of f, 
which is defined to be the function whose value at x
is f(f(...(f(x))).  For example, if f adds 1 to its 
argument, then the nth repeated application of f adds 
n. Write a function that takes as inputs a function 
f and a positive integer n, and then returns the 
function that computes the nth repeated application 
of f:

def foo(f, n):
    """Return the function that computes the 
    nth application of f.
    >>>  incr(5)        # function is to add 1 for input 
    argument number
    6
    >>> add3 = foo (incr, 5) 
    >>> add3(3)        # Doing like: incr(incr(incr(incr(incr(3)))))      
    8
    >>> foo (triple, 5)(1)  # triple(triple(triple(triple(triple(1)))))
    243
    >>> foo (square, 2)(5) # square(square(5))
    625
    >>> foo (square, 4)(5) # square(square(square(square(5))))
    152587890625
    """
