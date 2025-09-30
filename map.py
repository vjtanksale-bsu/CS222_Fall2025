def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
#print(squared_numbers)
print(list(squared_numbers))

fruits = ['apple', 'banana', 'cherry']
wordLength = map(len, fruits)
print(list(wordLength))

def ConvertToUpper(s):
    return s.upper()
names = ['alice', 'bob', 'carol', 'dave', 'eve']
upperNames = map(ConvertToUpper, names)
print(list(upperNames))