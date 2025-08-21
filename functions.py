def FahToCel(f):
    return (f - 32) * 5.0 / 9.0

print(FahToCel(70))

def factorial(n):
    answer = 1
    while n >= 1:
        answer = answer * n
        n -= 1
    return answer

print(factorial(10))

def greatest(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
print(greatest(15, 10, 17))