def BreakExample():
    for counter in range(5):
        if counter == 3:
            break
        print(counter)
# BreakExample()
def ContinueExample():
    for counter in range(5):
        if counter == 2:
            continue
        print(counter)
ContinueExample()

def main():
    counter = 5
    while counter > 0:
        print("CS 222")
        counter -= 2
    for counter in range(20, 10, -3):
        print(counter)
# main()