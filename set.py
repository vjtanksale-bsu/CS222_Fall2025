def main():
    fruits = {"apple", "banana", "cherry"}
    print(fruits)
    fruits.add("orange")
    print(fruits)
    fruits.add("banana")
    print(fruits)
    miscellaneous = {"Alice", 50, True, "Bob", 100, 55.23, True}
    print(miscellaneous)
    for m in miscellaneous:
        print(m)
main()