import functools

@functools.lru_cache(maxsize=None)
def factorial(n: int) -> int:
    """Calculates the factorial of a non-negative integer n.

    Args:
        n: The integer to compute the factorial of. Must be non-negative.

    Returns:
        The factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

@functools.lru_cache(maxsize=None)
def permutations(n: int, k: int) -> int:
    """Calculates the number of permutations P(n, k).

    Args:
        n: The total number of items.
        k: The number of items to choose.

    Returns:
        The number of possible permutations.

    Raises:
        ValueError: If n < 0, k < 0, or k > n.
    """
    if n < 0 or k < 0:
        raise ValueError("n and k must be non-negative.")
    if k > n:
        raise ValueError("k cannot be greater than n.")
    return factorial(n) // factorial(n - k)

@functools.lru_cache(maxsize=None)
def combinations(n: int, k: int) -> int:
    """Calculates the number of combinations C(n, k).

    Args:
        n: The total number of items.
        k: The number of items to choose.

    Returns:
        The number of possible combinations.

    Raises:
        ValueError: If n < 0, k < 0, or k > n.
    """
    if n < 0 or k < 0:
        raise ValueError("n and k must be non-negative.")
    if k > n:
        raise ValueError("k cannot be greater than n.")
    return permutations(n, k) // factorial(k)
