def FahToCel(f):
    return (f - 32) * 5.0 / 9.0

print(FahToCel(70))

def RecursiveFactorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * RecursiveFactorial(n-1)
    
print(RecursiveFactorial(19))
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

def LetterGrade(average = 0):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"  
print(LetterGrade())

def foo(z, x = 10, y = 5):
    return x + y + z
print(foo(3, 2, 20))