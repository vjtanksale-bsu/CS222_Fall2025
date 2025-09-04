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
    afc = [
        ["Colts", "Jaguars", "Titans", "Texans"],
        ["Patriots", "Jets", "Dolphins", "Bills"],
        ["Browns", "Bengals", "Steelers", "Ravens"],
        ["Chargers", "Broncos", "Chiefs", "Raiders"]
    ]
    print(afc[2])
    print(afc[2][1])
    print(afc[2][1][0])

main()