def quadratic(A, B, C):
    import math
    """
    Calculate the solution to the quadratic formula
    input: A (float), B (float), C (float)
    output: (float, float)

    >>> quadratic(1, 0, -1)
    (1.0, -1.0)
    >>> quadratic(1, 0, 1)
    Traceback (most recent call last):
        ...
    ArithmeticError: No real solution
    >>> quadratic(1, 0, 0)
    (0.0, 0.0)
    
    >>> quadratic(2, 4, 2)
    (-1.0, -1.0)
    """
    if B*B - 4*A*C < 0:
        raise ArithmeticError("No real solution")
    
    elif A == 0 and B == 0:
        return (0, 0)
    
    elif A == 0:
        return (-C/B, -C/B)

    
    ans1 = (-B + math.sqrt(B*B - 4*A*C)) / (2*A)
    ans2 = (-B - math.sqrt(B*B - 4*A*C)) / (2*A)
    return (ans1, ans2)

def main():
    print(quadratic(1, 0, -1))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # main()