def main():
    midterm = {
        "Alice": 90, 
        "Bob" : 93, 
        "Carol" : 70, 
        "Dave" : 100, 
        "Eve" : 97
    }
    #print(midterm["Bob"])
    #print(midterm.values())
    #print(midterm.keys())
    #for m in midterm.values():
    #    print(m)
    #print(len(midterm))
    for k, v in midterm.items():
        #print(k)
        #print(v)
        if k == "Carol":
            print(v)
    exams = {
        "Alice" : [100, 75, 80],
        "Bob" : [50, 50, 10]
    }
    #print(len(exams))
    print(exams["Bob"][2])
    
main()