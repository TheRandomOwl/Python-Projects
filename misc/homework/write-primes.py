"""
Answer whether a number is prime
input: n (int)
output: True if n is prime, False otherwise
"""
def isPrime(n):
    factors = []
    if n == 1:
        return False
    for i in range(2,1+n//2):
        if n % i == 0:
            factors.append(i)
        if len(factors) > 0:
            return False
    return True

"""
Write prime numbers from 1 to n inclusive to a file, one per line
input: filename (str), n (int)
output: None
"""
def writePrimes(filename, n):
    with open(filename, 'w') as f:
        for i in range(1,n+1):
            if isPrime(i):
                f.write(f"{i}\n")
def main():
    writePrimes('primes.txt', 100)

if __name__ == '__main__':
    main()