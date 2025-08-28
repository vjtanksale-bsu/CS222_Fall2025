def main():
    students = ["Alice", "Bob", "Carol", "Dave", "Eve"]
    print(len(students))
    print(students[2])
    print(students[4][2])
    for name in students:
        print(name)
    for name in students:
        for character in name:
            print(character)
main()