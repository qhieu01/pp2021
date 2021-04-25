from math import *
from numpy import * 
liststudent = []
listcourse = []
listmark = []





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

class student():
    def __init__(self, id, name, dob):
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
     def _init_(self,sname,cname,mark):
         self.sname=sname
         self.cname=cname
         self.mark=mark
     def mark (self):  #get
         print("Stuname : " + self.sname)
         print("couname : " + self.cname)
         print("mark : " + self.mar)
     def marK(self,sname,cname,mark):      #set 
         self.sname=sname
         self.cname=cname
         self.mark=mark

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


index = 0
numberstudent()
listStudent()
setstudent()
printstudentlist()

print("\n")
numbercourse()
createlistcourse()
setcourse()
printcourselist()

print("\n")
numbertecord()
for i in range(numbertecord):
    createlistmark()
    setmark()
printmarklist()
studentaverage()