from math import *
from numpy import *
import gzip, base64
from io import StringIO
liststudent = []
listcourse = []
listmark = []

def numberstudent():
    global numberstudent
    numberstudent = int(input("Number studne:"))
def numbercourse():
    global numbercourse
    numbercourse = int(input("number course;"))
def numberrecord():
    global numberrecord
    numberrecord = int(input(" Number of Record: "))


def ifexistnameStudent(name):
    for student in liststudent:
        if name == student.name:
            return True
def ifexistnameCourse(name):
    for course in listcourse:
        if name == course.name:
            return True
def averagemark(name):
    arrmark = []
    
    for i in range(len(listmark)):
        if name == listmark[i].studentname:
            arrmark.append(listmark[i]).mark)
    arrmarknp = array(arrmark)
    avenragemark = average(arrmarknp)
    print("diem trung binh cua " + name + str( averagremark))

class student ():
  def __init__(self, id, name, ):
        self.id = id
        self.name = name
        
    def getstudentinfo(self):
        print("ID student : " + self.id)
        print("Name student : " + self.name)
       
    def setstudentinfo(self, id, name, dob):
        self.id = id
        self.name = name
class course():
     def _init_ (self, id, name):
         self.id = id 
         self.name = name 
     def courseinfo(self):   #get
         print("Id :" + self.id)
         print("Name : " + self.name)
     def coursein4(self,id,name):   #set 
         self.id = id
         self.name = name 
class Mark():
     def _init_(self,studentname,coursename,mark):
         self.studentname=studentname
         self.coursename=coursename
         self.mark=mark
     def mark (self):  #get
         print("studnettuname : " + self.studentname)
         print("couname : " + self.coursename)
         print("mark : " + self.mark)
     def marK(self,studentname,coursename,mark):      #set 
         self.studnentname=studentname
         self.coursename=coursename
         self.mark=mark
         
def liststudent ():
    for i in range (numstudent):
        liststu.append("s" + str(i))
def infostudent():
    for i in range (numberstudent):
        idstudent = input("Enter Student ID: ")
        namestudent = input("Enter Student Name: ")
        liststudent[i] =Student(idstudent, namestudent)
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
    
def studentaverage():
    nametemp = input("Student Name you want to get Average: ")
    averagemark(nameTemp)
 
def handelfile():
    fstudent = open("students.txt", "a")
    for student in liststudent:
        fstudent.write(student.id)
        fstudent.write("\n")
        fstudent.write(student.name)
        fstudent.write("\n")
    fstudent.close()

    fcourse = open("courses.txt", "a")
    for course in listcourse:
        fcourse.write(course.id)
        fcourse.write("\n")
        fcourse.write(course.name)
        fcourse.write("\n")
    fcourse.close()
    #File Marks
    fmark = open("marks.txt", "a")
    for mark in listmark:
        fmark.write(mark.studentName)
        fmark.write("\n")
        fmark.write(mark.courseName)
        fmark.write("\n")
        fmark.write(str(mark.mark))
        fmark.write("\n")
    fmark.close()

    f1 = open("students.txt", "r")
    print(f1.read())
    f2 = open("courses.txt", "r")
    print(f2.read())
    f3 = open("marks.txt", "r")
    print(f3.read())

#Main
index = 0
numberstudent()
createliststudent()
setstudent()
printstudentlist()

print("\n")
numbercourse()
createlistcourse()
setcourse()
printcourselist()

print("\n")
numberrecord()
for i in range(numberrecord):
    createlistmark()
    setmark()
printmarklist()
studentaverage()
handelfile()

