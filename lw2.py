liststudent = []
listcourse = []
listmark = []

#student
def numstudent():
    global numstudent
    numstudent = int(input("How many student"))
 #course
def numcourse():
    global numcourse
    numcourse = int(input("how many course"))
#Class student
class Student():
     def _init_ (self, id, name):
         self.id = id 
         self.name = name 
     
     def studentinfo(self):   #get
         print("Id : "+ self.id)
         print("name :" + self.name)
     def stuin4(self,id,name):  #set 
         self.id=id
         self.name=name
#class stundent
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
#class mark
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
        liststudent[i] = Student(idstudent, namestudent)
def printStuList():
    print("student list")    
    for i in range (numstudent):
        liststudent[i].studentinfo()

def listcou():
    for i in range (numcourse):
        listcourse.append("s"+ str(i))
        listcourse[i].courseinfo()

def listmark():
    global checkstudent
    global checkcourse
    checkstudent = input("pick student : ")
    checkcourse = input("pick course : ")



    
       
        