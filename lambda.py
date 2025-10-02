add = lambda x, y: x + y
print(add(3,5))
temperatures =[212, 32, 100]
print(list(map(lambda f: (f - 32) * 5.0/9.0, temperatures)))
numbers = [3,1,4,1,5,9,2,6,5,3,5]
print(sorted(numbers, reverse=True))
midterm = {'Carol':92, 'Alice':95, 'Bob':88, 'Eve':100, 'Dave':70}
sortedScores = sorted(midterm.items(), key=lambda x : x[1], reverse=True)
print(sortedScores)
points =[(1,3,10),(2,1,20),(4,2,15)]
print(sorted(points,key= lambda x : x[2]))
