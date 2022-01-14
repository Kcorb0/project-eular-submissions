# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!


def factorial_dig_sum(n):

    result = n

    while n > 1:
        n -= 1
        result = result * n

    return sum([int(x) for x in str(result)])

print(factorial_dig_sum(100))