def fancy_printing():
    n = int(input("Please enter a number: "))
    for i in range(1, n+1):
        if n % i == 0:
            print("Buzz!")
        else:
            print(i)
            
fancy_printing()