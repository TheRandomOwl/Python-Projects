"""
Answer whether a number is prime
input: n (int)
output: True if n is prime, False otherwise

>>> isPrime(1)
False
>>> isPrime(2)
True
>>> isPrime(3)
True
>>> isPrime(4)
False
>>> isPrime(5)
True
>>> isPrime(0)
False
>>> isPrime(-1)
False
"""
def isPrime(n):
    if n <= 0:
        return False
    factors = []
    if n == 1:
        return False
    for i in range(2,1+n//2):
        if n % i == 0:
            factors.append(i)
        if len(factors) > 0:
            return False
    return True

def main():
    print(isPrime(-22))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # main()