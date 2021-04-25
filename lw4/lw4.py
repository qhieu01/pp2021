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