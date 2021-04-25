def numberstudent():
    global numberstudent
    numberstudent = int(input("how many student :"))
def numbercourse():
    global numbercourse
    numbercourse = int(input("how many course : "))
def ifexitstudent(name):
    for student in liststudent:
        if name == student.name:
            return True
def ifexitcoursr(name):
    for course in listcourse:
        if name == course.name:
            return True
def amark(name):
    amark = []
    for i in range(len(listmark)):
        amark.append(listmark[i].mark)
    amarkn = array(amark)
    amark = average(amarkn)
    print("averager mark for"+name+ str(amark))
