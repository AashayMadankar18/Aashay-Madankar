# PROGRAM 1 :- Python Collections :- List :- List is a collection which is ordered and changable
'''# to print a list
mylist = ["Abhi","Ashok","Ashish","Robin","Pragyaan"]
print(mylist) 

# to print a specific position
mylist = ["Abhi","Ashok","Ashish","Robin","Pragyaan"]
print(mylist[0])

#to print last position 
mylist = ["Abhi","Ashok","Ashish","Robin","Pragyaan"]
print(mylist[-1])

# range in list
mylist = ["Abhi","Ashok","Ashish","Robin","Pragyaan"]
print(mylist[1:3])

# list is changable
mylist = ["Abhi","Ashok","Ashish","Robin","Pragyaan"]
mylist[2] = "Suresh"
print(mylist)
 
# to remove name from a list
mylist = ["Abhi","Ashok","Ashish","Robin","Pragyaan"]
mylist.remove("Ashok")
print(mylist)

# to remove the new list and copy the previous list
mylist = ["Abhi","Ashok","Ashish","Robin","Pragyaan"]
newlist = mylist.copy()
print("mylist is = ",mylist)
print("newlist is = ",newlist)'''

# PROGRAM 2 :- Tuple :- Tuple is a collection which is ordered and unchangable
'''myTuple = ("Abhi","Ashok","Ashish","Robin","Pragyaan")
print(myTuple)

# Range in Tuple
myTuple = ("Abhi","Ashok","Ashish","Robin","Pragyaan")
print(myTuple[1:3])

# Length of Tuple
myTuple = ("Abhi","Ashok","Ashish","Robin","Pragyaan")
print(len(myTuple))'''

# PROGRAM 3 :- SET :- Set is a collection which is not in a order and unindexed. Set is changable
''' # to print a set 
mySet = {"Abhi","Ashok","Ashish","Robin","Pragyaan"}
print(mySet)

# Changable
mySet = {"Abhi","Ashok","Ashish","Robin","Pragyaan"}
myset[1] = "Virat"
print(mySet)

# Length of Set
mySet = {"Abhi","Ashok","Ashish","Robin","Pragyaan"}
print(len(myset))

# to remove name from set
mySet = {"Abhi","Ashok","Ashish","Robin","Pragyaan"}
mySet.remove("Ashok")
print(mySet)

# to clear the set
mySet = {"Abhi","Ashok","Ashish","Robin","Pragyaan"}
mySet.clear()
print(mySet)

#to create newSet and copy previous set
mySet = {"Abhi","Ashok","Ashish","Robin","Pragyaan"}
newSet = mySet.copy
print("mySet is = ",mySet)
print("newSet is = ",newSet)'''

# Program 4 :- Dictionary :- In Dictionary the data is stored in keys and values pair
'''myDict={"Name" : "Ash","ClgName" : "PCE","RollNo" : 130}
print(myDict)

a = myDict["Name"]
print(a)'''

# Program 5 :- else - if 
# no is odd or even 
'''a = int(input("Enter any number = "))
if a%2 == 0:
    print("Entered number is even")
else:
    print("Entered number is odd")'''

# Program 6 :- Nested if 
# costliest car
'''a = int(input("Enter 1st car's price = "))
b = int(input("Enter 2nd car's price = "))
c = int(input("Enter 3rd car's price = "))
if a>b:
    if a>c:
        print(a,",a is the costliest car.")
    else:
        print(c,",c is the costliest car.")
else:
    if b> c:
        print(b,",b is the costliest car.")
    else:
        print(c,",c is the costliest car.")'''

#program 7 :- logical and operator :
'''s1 = int(input("marks entered in sub 1 = "))
s2 = int(input("marks entered in sub 2 = "))
s3 = int(input("marks entered in sub 3 = "))
if s1>40 and s2>40 and s3>40 and s4>40:
    print("student is pass")
else:
    print("student failed")'''

# program 8 :- 
'''mylist = ["ganga","yamuna","saraswati","kaveri","krishna","bramhaputra"]
for i in mylist:
    print(i)'''

# program 9 :-
'''mylist = ["ganga","yamuna","saraswati","kaveri","krishna","bramhaputra"]
for i in mylist:
    print(i)
    if i == "kaveri":
        break'''

#program 10 :- Functions :-
'''def func(fname,lname):
    print("Hola" , fname , lname)
func(fname = "Mr",lname = "Johnson")'''

#program 11 :-
'''def func(name):
    for i in name:
        print(i)
name_of_a = "Rock"
func(name_of_a)'''

# Program 12 :- 
'''def absoulte_value(num):
    if num >= 0:
        return num 
    else:
        return -num
print(absoulte_value(18))
print(absoulte_value(-2))'''

# Program 13
'''def new_func():
    x = 4
    print("inside func = ",x)
x = 8
new_func()
print("outside func = ",x)'''

# Program 14 :- Parameters
'''def function(name,  message = "Happy morning"):
    print("Hello", name + ', ' + message)
function("Abhinandan")
function("Arya", "How you doin?")'''

# Program 15
'''def function(*names):
    for name in names:
        print("Hello",name)
function("Suresh","Naresh","Ramesh","Jaish")'''

#Program 16
'''def x(a,b,c):
    print(a,b,c)
m = (18,45,33)
x(*m)'''

#program 17 :- Modules
'''import mymodule
mymodule.greeting("Bhai")'''

#Program 18 :-
'''import mymodule as mx
a = mx.person1["age"]
print(a)'''

# Program 19 :-
'''import math
print("the value of pi is = ",math.pi)'''

# Program 20:-
'''import math as m
print("the value of pi is = ",m.pi)'''

#program 21 :-
'''import math as m
print("the square root of 625 = ",m.sqrt(625))'''

#program 22 :-
'''import math as m
print("the factorail of 13 = ",m.factorial(13))'''

# Program 23 :-
'''import math as m
print("The value of Sin1 = ",m.sin(1))'''

# Program 24 :-
'''import math as m
print("the value of log10 10 = ",m.log10(10))'''

# Program 25 :- class
'''class Individual:
    "This is an individual class"
    age = 18
    def greet(self):
        print('Namaste')
print(Individual.age)
print(Individual.greet)
print(Individual.__doc__)'''

# Program 30 :-
'''class Boy:
    "Boy belongs to the species human."
    age = 18
    def greet(self):
        print('Namaste Ram')
Ram = Boy()
print(Boy.greet)
Ram.greet()'''

# Program 31 :-
'''class Man:    
    def introduce_self(self):
        print("My name is = " + self.name)
r1 = Man()
r1.name = "Ram"
r1.color = "Bhagwa"
r1.introduce_self()'''

# Program 32 :- 
'''class Man:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def introduce_self(self):
        print("My name is = " + self.name)
r1 = Man("Ram" , "Saffaron")
r1.introduce_self()'''

# Program 33 :-
'''class School:
    def __init__(self,name, subject, exam):
        self.name = name
        self.subject = subject
        self.exam = exam
    def about_school(self):
        print("My School Name is " + self.name)
        print("My favourite subject is " + self.subject)
        print("My Exams approaching are " + self.exam)
s1 = School("Tejswini Vidya Mandir." , "English.", "Terminal Exam.")
s1.about_school()'''

# Program 34 :-
'''class City:
    def __init__(self, name, state, country):
        self.name = name
        self.state = state 
        self.country = country
    def regarding_city(self):
        print("The Name of City is " + self.name)
        print("The State in which the city lies is " + self.state)
        print("The Country in which the City located is " + self.country)
c1 = City("Nagpur" , "Maharashtra" , "India")
c1.regarding_city()'''

# Program 35 :-
'''class Institute:
    def __init__(self, name, instructor, coaching):
        self.name = name
        self.instructor = instructor
        self.coaching = coaching
    def information_institute(self):
        print("The name of the institute is " + self.name)
        print("The instructors here is " + self.instructor)
        print("The coaching given is of " + self.coaching )
i1 = Institute("APS" , "Prashant Sir and Ashish Sir" , "Computer Languages")
i1.information_institute()'''

# Program 36 
'''class Movie:
    def __init__(self , name, song):
        self.name = name
        self.song = song
m1 = Movie("Chhichore" ,"vo din bhi kya din thee")
print(m1.name)
print(m1.song)'''

# Program 37 :- Inheritance 
'''class School:
    def student1(self):
        print("Student 1 is studying")
    def student2(self):
        print("Student 2 is studying")
class Institute(School):
     def student3(self):
        print("Student 3 is studying")
     def student4(self):
        print("Student 4 is studying")
a1 = A()
a1.student1()
a1.student2()
b1 = B()
b1.student1()'''

'''# Program 38 :-
class Covid:
    def Virus1(self):
        print("Virus 1 is Spreading")
    def Virus2(self):
        print("Virus 2 is Spreading")
class Corona(Covid):
    def Virus3(self):
        print("Virus 3 is spreading")
    def Virus4(self):
        print("Virus 4 is Spreading")
c1 = Covid()
c1.Virus1()
c1.Virus2()
c2 = Corona()
c2.Virus2()
c2.Virus3()'''

# Program 39 :- Multi level inheritance
'''class School:
    def student1(self):
        print("Student 1 is studying")
    def student2(self):
        print("Student 2 is studying")
class Coaching(School):
    def student3(self):
        print("Student 3 is Studying")
    def student4(self):
        print("Student 4 is Studying")
class Tuition(Coaching):
        def Student5(self):
            print("Student 5 is Studying")
a1 = School()
a1.student1()
a1.student2()
b1 = Coaching()
b1.student1()
b1.student4()
c1 = Tuition()
c1.student1()
c1.student4()
c1.student5()'''

# Program 40 :
'''class Covid:
    def virus1(self):
        print("Virus 1 is spreading")
    def virus2(self):
        print("virus 2 is spreading")
class Corona(Covid):
    def virus3(self):
        print("Virus 3 is spreading")
    def virus4(self):
        print("Virus 4 is spreading")
class ChineseVirus(Corona):
        def virus5(self):
            print("Virus 5 is spreading")
a1 = Covid()
a1.virus1()
a1.virus2()
b1 = Corona()
b1.virus1()
b1.virus4()
c1 = ChineseVirus()
c1.virus1()
c1.virus4()
c1.virus5()'''

# Program 41 :- Multiple inheritance
'''class State:
    def region1(self):
        print("Region 1 has river flowing")
    def region2(self):
        print("Region 2 has mountains")
class City():
    def region3(self):
        print("Region 3 has valleys")
    def region4(self):
        print("Region 4 has Dams")
class Taluka(A,B):
        def region5(self):
            print("region 5 has Streams")
a1 = State()
a1.region1()
a1.region2()
b1 = City()
b1.region3()
b1.region4()
c1 = Taluka()
c1.region1()
c1.region()
c1.region5()'''

# Program 42 :-
'''class Goods:
    def vehicle1(self):
        print("Vehicle 1 is running")
    def vehicle2(self):
        print("Vehicle 2 is running")
class Passenger():
    def vehicle3(self):
        print("Bus is carrying passengers")
    def vehicle4(self):
        print("SUV is carrying Passengers")
class Transport(Goods,Passenger):
        def vehicle5(self):
            print("Truck is carrying goods")
a1 = Goods()
a1.vehicle1()
a1.vehicle2()
b1 = Passenger()
b1.vehicle3()
b1.vehicle4()
c1 = Transport()
c1.vehicle1()
c1.vehicle4()
c1.vehicle5()'''

# Program 43 :- Polymorphism - operator overloading
'''a = 18
b = 45
print(int.__add__(a,b))'''

# Program 44 :- 
'''class Student:
    def __init__(self,subject1,subject2):
        self.subject1 = subject1
        self.subject2 = subject2
    def __add__(self, other):
        subject1 = self.subject1 + other.subject1
        subject2 = self.subject2 + other.subject2
        s3 = Student(subject1,subject2)
        return s3
s1 = Student(45,55)
s2 = Student(99,78)
s3 = s1 + s2
print("Marks of Student in Subject1 = ",s3.subject1)
print("Marks of Student in Subject2 = ",s3.subject2)'''

# Program 45 :-
'''class Number:
    def __init__(self,integer1,integer2):
        self.integer1 = integer1
        self.integer2 = integer2
    def __mul__(self, other):
        integer1 = self.integer1 * other.integer1
        integer2 = self.integer2 * other.integer2
        n3 = Number(integer1,integer2)
        return n3
n1 = Number(8,4)
n2 = Number(4,2)
n3 = n1 * n2
print("Product of two integers = ",n3.integer1)
print("Product of two integers = ",n3.integer2)'''

# Program 46:-Method Overloading  :-
'''class Worker:
    def __init__(self,load1,load2):
        self.load1 = load1
        self.load2 = load2
    def sum(self,a=None,b=None,c=None):
        w = 0
        if a!=None and b!=None and c!=None:
            w = a+b+c
        elif a!=None and b!=None:
            w = a+b
        else:
            w = a
        return w
w1 = Worker(4,5)
print(w1.sum(7,9,2))'''

#Program 47 :-
'''class Integer:
    def __init__(self,dig1,dig2):
        self.dig1 = dig1
        self.dig2 = dig2
    def sum(self,l=None,m=None,n=None):
        i = 0
        if l!=None and m!=None and n!=None:
            i = l+m+n
        elif l!=None and m!=None:
            i = l+m
        else:
            i = l
        return i
i1 = Integer(44,45)
print(i1.sum(4,1))'''

# or
'''class Integer:
    def __init__(self,dig1,dig2):
        self.dig1 = dig1
        self.dig2 = dig2
    def sum(self,l=None,m=None,n=None):
        i = 0
        if l!=None and m!=None and n!=None:
            i = l+m+n
        elif l!=None and m!=None:
            i = l+m
        else:
            i = l
        return i
i1 = Integer(44,45)
print(i1.sum(4))'''

# Program 48 :- Method Overriding :-
'''class Movie:
    def act(self):
        print("the drama was good")
class Script(Movie):
    pass
a1 = Script()
a1.act()'''

#Program 49 :-
class A:
    def show(self):
        print("in A Show")
class B(A):
    pass
a1 = B()
a1.show()

