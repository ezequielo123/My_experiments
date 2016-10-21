from statistics import mean as m

admins = {'Python':'Pass123', 'user2':'pass2'}
studentDict = {'Jeff':[78,88,93],
               'Alex':[92,76,88],
               'Sam':[89,92,93]}

def enterGrades():
    nameToEnter = input('Studen Name: ')
    gradeToEnter = input('Grade: ')

    if nameToEnter in studentDict:
        print('Adding grade...')
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('Student does not exist')

    print(studentDict)


def removeStudent():
    nameToDelete = input('Studen Name: ')

    if nameToDelete in studentDict:
        print('Removing student')
        del studentDict[nameToDelete]
    else:
        print('Student does not exist')

    print(studentDict)

def studentAVGs():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)

        print(eachStudent, 'has an average grade of ', avgGrade)
    
    

def main():
    print("""
    Welcome to Grade Central

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average
    [4] - Exit
    """)

   
    action = input('What would you like to do today? (Enter a number) ')

    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        studentAVGs()
    elif action == '4':
        exit()
    else:
        print('No vaild choice was given, try again')


login = input('Username: ')
passw = input('Password: ')

if login in admins:
    if admins[login] == passw:
        print('Welcome,',login)
        while True:
            main()
    else:
        print('Invalid password')
else:
    print('Invalid username')
