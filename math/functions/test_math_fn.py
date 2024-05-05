from quadratic import quadratic
from is_prime import isPrime

# Tests for quadratic function

# Test case: A = 0, B = 0, C = 0
assert quadratic(0, 0, 0) == (0.0, 0.0)

# Test case: A = 1, B = 0, C = 0
assert quadratic(1, 0, 0) == (0.0, 0.0)

# Test case: A = 1, B = 0, C = -1
assert quadratic(1, 0, -1) == (1.0, -1.0)

# Test case: A = 1, B = 0, C = 1
try:
    quadratic(1, 0, 1)
except ArithmeticError:
    pass
else:
    raise AssertionError("Expected ArithmeticError")

# Test case: A = 1, B = 2, C = 1
assert quadratic(1, 2, 1) == (-1.0, -1.0)

# Test case: A = 2, B = 4, C = 2
assert quadratic(2, 4, 2) == (-1.0, -1.0)

# Test case: A = 2, B = -4, C = 2
assert quadratic(2, -4, 2) == (1.0, 1.0)

# Test case with positive discriminant
assert quadratic(1, 0, -1) == (1.0, -1.0)

# Test case with zero discriminant
assert quadratic(1, 0, 0) == (0.0, 0.0)

# Test case with negative discriminant
try:
    quadratic(1, 0, 1)
except ArithmeticError:
    pass
else:
    raise AssertionError("Expected ArithmeticError")

# Test case with non-integer coefficients
assert quadratic(2.5, 1.5, -3) == (0.8357816691600547, -1.4357816691600547)

# Test case with large coefficients
assert quadratic(10**6, 10**6, -10**6) == (0.6180339887498948, -1.6180339887498947)

# Test case with very small coefficients
assert quadratic(1e-6, 1e-6, -1e-6) == (0.6180339887498948, -1.618033988749895)

# Test isPrime function

# Test case: n = -1
assert not isPrime(-1)

# Test case: n = 0
assert not isPrime(0)

# Test case: n = 1
assert not isPrime(1)

# Test case: n = 2
assert isPrime(2)

for n in range(3, 100):
    if all(n % i != 0 for i in range(2, n)):
        assert isPrime(n)