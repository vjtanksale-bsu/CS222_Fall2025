def main():
    try:
        studentList = open("students.txt", 'r')
        students = studentList.readlines()
        studentList.close()
        #print(students)
        #for line in students:
            #print(line)
        fileOutput = open("output.txt", 'w')
        for line in students:
            parts = line.split(',')
            #print(parts[0])
            if parts[2] == "Math":
                fileOutput.write(parts[1] + " " + parts[0] + "'s GPA is " + parts[3])
                #print(line)
        fileOutput.close()
    except FileNotFoundError:
        print("File not found")
main()
