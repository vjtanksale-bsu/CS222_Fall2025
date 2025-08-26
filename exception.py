def main():
    x = 5
    try:
        z = 10 / x
    except ZeroDivisionError:
        print("You are dividing by zero")
    else:
        print("All good.")
main()