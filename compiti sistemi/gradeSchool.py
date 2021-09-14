roster = {}

def addStudent(name, grade):
    if not grade in roster:
        roster[grade] = [name]
    
    else:
        roster[grade].append(name)
        roster[grade].sort()


def getStudentsGrade(grade):
    return grade, roster[grade]


def getAllStudents():
    string = ""
    listApp = []

    for grade in roster:
        listApp.append(f"grade {grade}: {roster[grade]}")

    listApp.sort()

    for k in listApp:
        string += ", " + k

    return string




def main():
    addStudent("Paolo", 2)
    addStudent("Gianni", 3)
    addStudent("Lucia", 2)
    addStudent("Giacomo", 1)
    addStudent("Anna", 2)
    addStudent("Bob", 1)
    addStudent("Piero", 4)

    print(f"Students in grade {getStudentsGrade(1)}")

    print(f"All students{getAllStudents()}")


if __name__ == "__main__":
    main()