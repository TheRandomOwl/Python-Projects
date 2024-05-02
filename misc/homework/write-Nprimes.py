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
Write the first n prime numbers to a file, one per line
input: filename (str), n (int)
output: None
"""
def writePrimes(filename, n):
    i = 2
    primes = []
    
    while len(primes) < n:
        if isPrime(i):
            primes.append(i)
        i += 1
    with open(filename, 'w') as f:
        for item in primes:
            f.write(f"{item}\n")

def main():
    writePrimes('primes.txt', 10)

if __name__ == '__main__':
    main()