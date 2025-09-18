def main():
    bsu = "Ball State University"
    #print(bsu[2])
    #bsu[2] = 'x'
    print(bsu[:5])
    print(bsu.startswith("Ball State U"))
    print(bsu.upper())
    print(bsu.isalnum())
    print(bsu.isupper())
    print(bsu.find("t"))
    print(bsu.find("hudfbgvhfdb"))
    print(bsu.rfind("t"))
    print(bsu.replace("a", "x"))
    print(bsu)
    print(bsu.count("t"))
main()