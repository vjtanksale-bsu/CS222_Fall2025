def main():
    try:
        studentList = open("students.txt", 'r')
        students = studentList.readlines()
        studentList.close()
        #print(students)
        #for line in students:
            #print(line)
        for line in students:
            parts = line.split(',')
            #print(parts[0])
            if parts[2] == "Math":
                print(line)
    except FileNotFoundError:
        print("File not found")
main()
