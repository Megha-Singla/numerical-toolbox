#OOP in python (very imp, in interviews)
a=10
b=90
sum=10+90
print(sum)
#First we make class and then objects(basically real world.)
#CLASSS AND OBJECT IN PYTHON
#class is a blueprint for creating objects.
#creating class(blueprint of gaadi)
class Student:
    name="Karan"   #Every student name is karan.
#creating object(instance of class)(gaadi bhi toh bnani padegi)
s1=Student()
print(s1.name)
s2=Student()
print(s2.name)

class Car:                #Class creation
    color="black"
    brand="mercedes"
car1=Car()                #Object creation
print(car1.color)
print(car1.brand)

#__init__Function (invoke at the time of object creation)
#This function always executes either we write it or not, in the case we donot
# write it then python will automatically create it.(constructor)
#init means initialisation. Ex:
class Student:
    def __init__(self,name,age,income):    #in INIT, which is a constructor.
                                #self argument is always passed.
        self.name=name
        self.age=age
        self.income=income
        print("adding new student in database")

s1=Student("Megha","22","15K")
print(s1.name)
print(s1.age)
print(s1.income)

s2=Student("Chirag","19","20LPA")
print(s2.name)
print(s2.age)
print(s2.income)

s3=Student("Garima","27","17LPA")
print(s3.name)
print(s3.age)
print(s3.income)

#the self parameter is a reference to the current instance of the class,
#and is used to access variables that belong to the class.
#ATTRIBUTES: data stored for object(name, age, income)



# Constructor: it is a function which is called by itself when we create an object.  (Why we need this?)
#write configuration related code meaning jiska access hm user ko nhi dena chahte. jese ki koi website chalte wqt 
#vo AUTOMATICCALY internaet k saath connect ho jata h kyoki ye code init function m likha gya tha.


#There are 2 types of constructors: default and parameterised constructor.
#In default only self attribute is present and in parametrised 
#along with self others are also prsent.
#However, based on our need  we only make parameterised 
# constructor and that is enough.
class Student:
    def __init__(Self):
        pass

    def __init__(self,name,age,income):    #in INIT, which is a constructor.
                                #self argument is always passed.
        self.name=name
        self.age=age
        self.income=income
        print("adding new student in database")

s1=Student("Megha","22","15K")
print(s1.name, s1.age, s1.income)

#Attributes(any value or data) 
#2 types( class and instance)
#CLASS AND INSTANCE ATTRIBUTES
#class attribute: which is same for every object 
#instance attribute: which is different for every object. defined by self.___
#self is object reference.

#Ex: college name is class attribute and name, age are instance attribute.
class Student:
    college_name="ABC college"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("adding a new database")

s1=Student("Megha", 22)
print(s1.name, s1.age)
s2=Student("Chirag",19)
print(s2.name, s2.age)

#Instance attribute always have higher priority than class attribute.




#METHODS (Actually there are 2 things one is property and other is function.)
#(example: properties of car is its color, model.. and function are: how it start,
#how it stop, how the engine works..etc.)
#METHODS ARE NOTHING BUT THE FUNCTIONS THAT BELONG TO OBJECT.



#WHAT WE LEARNT TILL NOW:
#define class and object
#create constructor(init function)(self parameter is always passed in it.)
#creating attributes(2 types (class attribute(that are same for all objects)
#  and object attribute(different for every object.)) )
#different functions in class are called methods.(again always have to write self first.)

#Ques: Create student class that takes name and marks of 3 subjects
#as argument in constructor. Then craete a method to print the average.

class student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3

    def ave(self):
        av=(self.marks1+self.marks2+self.marks3)/3
        return av

s1=student("megha", 76,98,96)
print(s1.name)
print(s1.marks1)
print(s1.marks2)
print(s1.marks3)
print(s1.ave())

s1.name="Chi"
print(s1.name)



#Static method(basically it is used to make a function static meaning
#where we don't want to pass self.)(use: @staticmethod)   (for class attributes which is common for all objects.)
#example:
class student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3

    def ave(self):
        av=(self.marks1+self.marks2+self.marks3)/3
        return av

    @staticmethod
    def hello():
        return "hello"




#4 pillars of OOPS:
#1. ABSTRACTION 2.ENCAPSULATION 3.INHERITANCE 4.POLYMORPHISM

#1. ABSTRACTION:
#Hinding the unnecessary information from the user. Just show him what he want.
#Example:
class cars:
    def __init__(self):
        self.brk=False
        self.acc=False
        self.clutch=False

    def start(self):
        self.brk=True
        self.clutch=True
        self.acc=True
        print("Car started..")

car1=cars()
car1.start()


#2. ENCAPSULATION:
#WRAPPING DATA AND FUNCTIONS INTO A SINGLE UNIT(ObJECT).

#We know that in OOPS there is class and it's object and in class there are attributes(property) and methods(function).
#Object can access all attributes and methods.
#NOW THING IS HM ATTRIBUTE KI VALUE CLASS K BHAR SE CHANGE KR SKTE H.

#now leet us consider an example. 
class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0

    def deposit(self, amount):
        self.balance+=amount
        print("amount deposited is", amount)
        print("available balance is", self.balance)

    def withdraw(self, amount):
        self.balance-=amount
        print("amount withdrawn is", amount)
        print("available balance is", self.balance)


obj1=Atm()
obj1.balance="hehehe"   #kisi junior programmer ne bhar se code change kr diya
obj1.deposit(909)   #code crashes showing cannot add string to integer value

#To prevent this we use encapsulation:
# Step1: Make balance a private attribute  using __balance 
# i.e.  now attribute is....      self.__balance=0        in init
#Ques: can we now access it from outside ? ANS: yes, using...   _Atm__balance   
#so what's the point is that now this balnce will not pop up itself when you type (obj1.) .



class Atm:
    def __init__(self):
        self.pin=""
        self.__balance=0      #making this attribute private

    def deposit(self, amount):
        self.__balancebalance+=amount
        print("amount deposited is", amount)
        print("available balance is", self.__balance)

    def withdraw(self, amount):
        self.__balance-=amount
        print("amount withdrawn is", amount)
        print("available balance is", self.__balance)


obj1=Atm()
obj1.balance="hehehe"   #kisi junior programmer ne bhar se code change kr diya
obj1.deposit(909)          #no issues it will run


#Ques: What if we genuinely want to change attribute value from outside?
#USE getter and Setter method:



class Atm:
    def __init__(self):
        self.pin=""
        self.__balance=0      #making this attribute private

    def deposit(self, amount):
        self.__balance+=amount
        print("amount deposited is", amount)
        print("available balance is", self.__balance)

    def withdraw(self, amount):
        self.__balance-=amount
        print("amount withdrawn is", amount)
        print("available balance is", self.__balance)

    def get_balance(self):
        print(self.__balance)

    def set_balance(self, new_value):
        self.__balance=new_value
        print(self.__balance)



obj1=Atm()
obj1.balance="hehehe"   #kisi junior programmer ne bhar se code change kr diya
obj1.deposit(909)          #no issues it will run
obj1.set_balance("1000")  #we can change it    then what is the point of previous thing how we save it i.e.
#what if junior  programmer do
obj1.set_balance("heheh")   

# so fix set method smartly
# i.e
def set_balance(self, new_value):
    if new_value==int:
        self.__balance=new_value
        print(self.__balance)
    else:
        print("pitega kiya")





#Quess2: Create account class with 2 attributes- balance and account number.
# Create method for debit, credit and printing the balance.
class account:
    def __init__(self, balance, acc_no):
        self.balance=balance
        self.acc_no=acc_no

    def bal(self):
        return self.balance
    def debit(self, amt):
        self.balance-=amt
        print( "the amount debit is", amt)
        print("the amount left is", self.get_bal())

    def credit(self,amt):
        self.balance+=amt
        print("the amount credited is", amt)
        print("Remaining amount is", self.get_bal())


   
        
    

a1=account(20000,539910)
print(a1.bal())
a1.debit(1000)
a1.credit(2000)




