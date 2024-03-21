s1 = "hello how are you"
s2 = "hello how is"

s1 = s1.split(" ")
s2 = s2.split(" ")

for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)
n1 = 0
n2 = 1
ans = 0+1

n1 = 1
n2 = 2
ans = 1+2

n1 = 2
n2 = 3
ans = 2+3

# ! Find the 8th fibanochi number
num = 8
n1 = 0
n2 = 1
for val in range(num):
    ans = n1+n2
    n1 = n2
    n2 =ans
print(ans)


# ! Constructors

# Eg:2
# unparameterised constructor
class profile:
    def __init__(self):
        print("hello world")


obj = profile()
obj.__init__()

# ? Eg:3
# Parameterised Constructor
class profile:
    def __init__(self, id ,name ,age):
        print(id,name, age)
       
obj = profile(1,"bharath", 21)

# ? Eg:4
class c1:
    email = "sid@gmail.com"

    def m1(self):
        name = "sid"
        place = "cbe"
        print(name, place)
        print(self.email)
object = c1()
object.m1()

# ? Eg:5
class c1:
    email = "bharath@gmail.com"
    def m1(self):
        name = "bharath"
        age = 20
        return name, age
    def display(self):
       # ! print(name, age)
       # ! print(self.name, self,age)
       print(self.m1())
object = c1()
object.display()


# Eg:6
# To use the variable inside the constructor in another methods
class class1:
    def __init__(self):
        self.name = "sid"
        self.email = "sid@gmail.com"
        # return name, email # error ---> cnnot use return with constructor
       
    def display(self):
        print(self.name, self.email)

c1 = class1()
c1.display()

# -----> Inheritance
# The process of utilising the methods and attributes of parent class
# Throught the object of child class it is called as inheritance

# ? 5 types of Inheritance
# Single Inheriatance
# Multiple Iheritance
# Hybrid Inheritance
# Heirrichal Inheritance

# Single Inheritance
# It has only one parent class and only one child class

# Eg:1
class parent:
    def m1 (self):
        print("Iam parent class")

       
class child:
    def m2(self):
        print("Iam child class")
obj1  = parent()
obj1.m1()

# Eg:2
class c1:
    def ___init__(self):
        print("Iam constructor from parent class")
class child1(c1):
    pass

obj = child1()

# Eg:3
class parent:
    name = "afzal"


class child(parent):
    name = "afzal"

    def display(self):
        print(self.name)

d = child()
d.display()


# !  Multilevel inheritance

# ? Eg:1
class voice:
    def sound(self):
        print("All  the animals have their own voices")

class dog (voice):
    def dog_voice(self):
        print("bark")

class cat (dog):
    def cat_voice(self):
        print("Meow")
       
       
       
class parrot(cat):
    def parrot_voice(self):
        print("speak")

all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()

# ! Multiple Inheritance
# It has multiple parent and 1 child
# Eg:1
##class while_petrol:
##    def function_w(self):
##        print("used to Airplane")
##
##class Organic_petrol:
##    def function_o(self):
##        print("used for Bike, cars")
##
##class petrol(while_petrol, Organic_petrol, premium_petrol):
##    def defanition(self):
##        print("Petrol types")
##
##p=petrol()
##p.defanition()
##p.function()
##p= petrol()
##p.defanition()
##p.functon_o()
# ! Eg:2
# MRO ----> Method resoultion order
class addition:
    def add(self, a,b):
        print(a+b)

class substract:
    def sub(self, a,b):
        print(a-b)

class multiply:
    def mul (self, a,b):
        print(a*b)

class division(addition, substract, multiply):
    def div(self, a, b):
        print(a/b)

calc = division()
calc.add(3, 4)
calc.mul(5, 2)

# ! Heritance Inheritance
class catagory:
    def weight(self, weight):
        print(weight)

class Tomato:
    def tomato_specs(self):
        color = "black"
        taste ="neutral taste"

class carrot:
    def carrot_specs(self):
        color="orange"
        taste = "sweet"

c = carrot()
c.carrot_specs()
c.weight("30gms")

t = Tomato()
t.tomato_specs()
t.weight("20 gms")

# ! hybrid Inheritance
 # The combination of above 4 inheritance is called Hybrid inheritance
class c1:
    def m1(self):
        print("Class1")
        
class c2:
    def m2(self):
        print("class2")
        
class c3:
    def m3(self):
        print("Class 3")
        
class c4:
    def m4(self):
        print("Class 4")
        
class c5:
    def m5(self):
        print("Class 5")
        
class c6:
    def m6(self):
        print("Class 6")

# ! Hybrid Inheritance
# ? The combination of above 4 inheritance is called Hybrid Inheritance
class c1:
    def m1(self):
        print("Class 1")

class c2(c1):
    def m2(self):
        print("Class 2")

class c3(c2):
    def m3(self):
        print("Class 3")

class c4(c2):
    def m4(self):
        print("Class 4")
        
    def m3(self):
        print("i am m3 from c4")

class c5(c3):
    def m5(self):
        print("Class 4")  

class c6(c5, c4, c2, c1):
    def m6(self):
print("Class 4")
        
obj = c6()
obj.m3()

# ! -------> Polymorphism
# poly - many, morph--> form
# A function which has the ability t perform more than 1 functionality
# then it is considered to be as polymorphism

# * Polymorphism in builtin functions
# len() --> which is used to find the length of list, tuple, dict etc...
# index()
# max()
# min()
# count()
# pop()


# * Ploymorphism in operators
#-----> +
# print(8+8)
# print("k"+'l')
# print([1,2,3]+[4,5,6])

# *
# print(6*7)
# l1 = [1,2,3,4]
# print(*l1)
# def f1(*args)
# l1= [1,2,3,4]
# print(l1*10)

# polymorphism in classes
# We can achieve polymorphism in 2 ways
# 1.) Method overloading
# 2.) Method overriding

