"""
all_factors.py

Find all factors (divisors) of a positive integer `n` efficiently.

Idea / concept:
- Every factor `i` of `n` less than or equal to sqrt(n) has a complementary
  factor `n//i` greater than or equal to sqrt(n).
- So it's sufficient to check integers from 1..sqrt(n) and add both `i` and
  `n//i` when `i` divides `n` evenly.

Complexity:
- Time: O(sqrt(n)) — we iterate up to sqrt(n).
- Space: O(k) where k is the number of factors (output size).

This implementation demonstrates the standard sqrt trick and avoids
checking all numbers up to `n`.
"""

from math import isqrt

def all_factors(n: int) -> list:
    """Return a sorted list of all positive factors of `n`.

    Args:
        n: positive integer

    Returns:
        Sorted list of positive divisors of `n`.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")

    # use a set to avoid duplicates when n is a perfect square
    factors = set()
    limit = isqrt(n)  # integer sqrt (floor)

    for i in range(1, limit + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)

    return sorted(factors)


if __name__ == "__main__":
    # example usage
    n = 36
    print(all_factors(n))  # [1, 2, 3, 4, 6, 9, 12, 18, 36]