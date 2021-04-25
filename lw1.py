stu = {}
def countrstudent():
    count = int(input("Hom many student"))
    return count

def stuinfo():
    print("Enter information ; ")
    id = input("Id : ")
    name = input("Name: ")
    H = {"id":id,"name":name}
    return H 
    
    
def liststu(Stu):
	for H in Stu:
		print(f"id {H['id']},name is {H['name']} ")

students = []
count = countrstudent()
for i in range(0,count):
	H = stuinfo()
	students += [ H ] 
    
cou = {}
def CotCourse():
	count = int(input("How many course are there in the semester ?"))
	return count

def Courseinfo():
	print("Enter Course Infor : ")
	id = input(" ID : ")
	name = input(" Name : ")
	B = {"id":id,"name":name,}
	return B
def Courses_List(Courses):
	for B in Courses:
		print(f"id {B['id']},name is {B['name']} ")



 
Courses = []
count = CotCourse()
for i in range(0,count):
	B =  Courseinfo()
	Courses += [ B ] 

sumfor = input ("enter student Id to input mark")
while True:
    if sumfor not in stu:
        sum=input("wrong")
    else:
        break
mark = input("mark : ")
sum = {}
def mark(id,course,mark):
    sum[id]={course: mark}
    



    



