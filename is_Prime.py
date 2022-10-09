def is_prime():
    for i in range(2, n):
        if (n % i) == 0:
            return False
        return True

n = int(input("Please enter a number: "))
print(is_prime())

def cnt_primes():
    cnt = 0

    for num in range(n):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            cnt += 1
    return cnt

print(cnt_primes())

        