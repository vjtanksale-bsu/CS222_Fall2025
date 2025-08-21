def main():
    average = float(input("Enter class average score: "))
    if average >= 60:
        print("Pass")
    else:
        print("Fail")
    if average >= 90:
        print("A")
    elif average >= 80:
        print("B")
    elif average >= 70:
        print("C")
    elif average >= 60:
        print("D")
    else:
        print("F")
main()