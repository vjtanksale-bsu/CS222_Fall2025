def main():
    midterm = [90, 80, 100, 75, 82]
    midterm.append(50)
    midterm.insert(1, 70)
    print(len(midterm))
    print(midterm[2])
    print(min(midterm))
    print(max(midterm))
    print(midterm)
    midterm.remove(90)
    print(midterm)
main()