def liststu ():
    for i in range (numstudent):
        liststu.append("s" + str(i))

def student():
    for i in range (numstudent):
        idstudent = input("Enter Student ID: ")
        namestudent = input("Enter Student Name: ")
        liststudent[i] =cStudent(idstudent, namestudent)
def printstuList():
    print("student list")    
    for i in range (numstudent):
        liststudent[i].studentinfo()

def createlistcourse():
    for i in range(numbercourse):
        listcourse.append("s" + str(i))

def setcourse():
    for i in range(numbercourse):
        print( + str(i+1) + "st course" )
        id_course = input("Enter Course ID: ")
        name_course = input("Enter Course Name: ")
        listcourse[i] = course(id_course, name_course)


def ListMark():
    global checkstudent
    global checcourse
    checkstudent = input("Pick Student: ")
    checkcourse = input("Pick Course: ")
    if (ifexistnamestudent(checknamestudent) and ifexistnamecourse(checknamecourse)):
    
        print("Index: " + str(index))
    
    else:
        print("Not exist Student or Course")

def setmark():

    global index
    mark = float(input("Mark: "))
    listmark[index] = marktable(checknamestudent, checknamecourse, floor(mark))
    index += 1




def studentAverage():
    nametemp = input("pick stundent ")
    amark(nametemp)
