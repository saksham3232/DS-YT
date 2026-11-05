"""Check whether a number is prime."""

from math import isqrt


def is_prime(number: int) -> bool:
    """Return True when number is a prime number."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for divisor in range(3, isqrt(number) + 1, 2):
        if number % divisor == 0:
            return False
    return True


if __name__ == "__main__":
    value = int(input("Enter a number: "))
    result = "prime" if is_prime(value) else "not prime"
    print(f"{value} is {result}.")
