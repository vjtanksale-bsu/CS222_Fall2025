def IsEven(n):
    return n % 2 == 0
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def MaxMin(numbers):
    return (max(numbers), min(numbers))
