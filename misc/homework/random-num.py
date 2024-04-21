import random

def sumOfRandomSequence():
    '''
    Use the following to generate a random number between 0 and 100:
        n = random.randint(0, 100)
    If the number is even, add it to the sum of even numbers.
    If the number is odd, add it to the sum of odd numbers.
    If the number is zero, return a tuple of the sum of even numbers and the sum of odd numbers.
    '''
    sum_even = 0
    sum_odd = 0
    while True:
        n = random.randint(0, 100)
        if n == 0:
            return (sum_even, sum_odd)
        elif n % 2 == 0:
            sum_even += n
        else:
            sum_odd += n

def main():
    random.seed(0)
    print(sumOfRandomSequence())   # (1584, 1405)
    random.seed(1)
    print(sumOfRandomSequence())   # (518, 710)

if __name__ == '__main__':
    main()