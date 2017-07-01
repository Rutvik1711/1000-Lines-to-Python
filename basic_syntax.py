# @author Rutvik Shah
import math
import random
import os
#This script contains basic python commands

partition = "----------------------------------------------------------------"
print "Hello, Python"
print partition+"[1]"
#PLEASE UNDERSTAND ENVIRONMENT VARIABLES AND COMMAND LINE ARGUMENTS ?

#use ; for multiple statements on same line
a=1;b=2;c=3;d=4

#multi-line statements : continuation character '\'
e = a + b + \
    c + \
    d
print e

#multi-line statements with [] or {} need not need continuation character
arr = [1,2,3,4,5,
       6,7,8,9,10]
print arr
print partition+"[2]"

#use '--text--' or "--text--" for single line word or sentence
#use """--text--""" for multi-line paragraphs
word = 'word'
sentence = "this is a sentence"
paragraph = """this paragraph extends
in multiple lines and uses
triple quotes"""
print word
print sentence
print paragraph
print partition+"[3]"

#to wait for user
# raw_input('Press Enter to Exit')
# print partition

#variables, assignment and multiple assignment
p = 1       #integer
q = 1.001   #floating point
r = 'hello' #string
print p,q,r
l,m,n = 1,1.001,'hello'
print l,m,n
s=t=u=1
print s,t,u
print partition+"[4]"

#Python basic data types : Numbers, String, List, Tuple, Dictionary

#Numbers
var1 = 10               #integer
var2 = 100000000000L    #long
var3 = 1.0001           #float
var4 = 3 + 4j           #complex
print var1,var2,var3,var4
print partition+"[5]"

#String
str = "This is a sample python string. "
print str               #print string
print str[1]            #prints second character as indexing starts with 0
print str[3:9]          #prints characters from 4th to 10th
print str[3:]           #print characters starting from 4th
print str*3             #prints given string 3 times
print "Hello, " + str   #appends Hello, to str and then prints it
print partition+"[6]"

#List
myList = ['Hello',23,17.28,5+4j,'Hello',12,'Hello']
myShortList = ["abcd"]
print myList
print myList[0]   #count from left
print myList[-2]  #count from right
print myList[0:2]
print myList[1:]
print myShortList*3
print cmp(myList,myShortList); #List Comparision
print cmp(myShortList,myList);
print cmp(myList,myList)
print myList.count('Hello')
print myList + myShortList
myList.append('ABCD')
print myList
myList.extend(myShortList)
print myList
print myList.pop(len(myList)-1)             #removes with index and returns it
print myList.remove(myList[len(myList)-1])  #removes with object but doesn't return
myList.reverse()
print myList
#myList.sort() CUSTOM SORT?
print myList
print myList
myList[0] = 'xyz' #we can Update Lists
del myList[0]     #we can Update Lists
print partition+"[7]"

#Tuple   Note: only difference between tuple and list is that tuples are
#              read-only and cannot be updated
myTuple = ('Hello',23,17.28,5+4j)
myShortTuple = ('abcd','pqrs')
print myTuple
print myTuple[0]
print myTuple[0:2]
print myTuple*3
print myTuple + myShortTuple
print myTuple
#myTuple[0] = '1000' Invalid
myTuple = myShortTuple + myTuple #valid
print cmp(myTuple,myShortTuple)
print partition+"[8]"

#Dictionary : It is similar to hash map i.e., has key-value pair
#Note: Keys in a Dictionary should be immuatable so Tuples can qualify as keys but not Lists
dict = {}
dict['one'] = "This is One"
dict[2]     = "This is Two"
myDict = {'String':'Hello','Integer':123,'Floating':3.14,'Complex':3+4j,'List':myList};
myShortDict = {'String':'Bye','Integer':99};
print dict
print dict['one']
print dict[2]
#delete
del dict[2]  #removes one entry
dict.clear() #removes all entries
del dict     #deletes entire Dictionary
print myDict
print myDict['Complex']
print myDict['List']
print cmp(myDict,myShortDict)
print myDict.keys()
print myDict.values()
print myDict.items()
print myDict.get('PQR','Not Available here!') #arg2 is default value if key is not found
#similar to get but if key is not present then it will set arg1-arg2 key-value pair
print myDict.setdefault('PQR','Default')
print myDict
#create  new dictionary with keys-values from sequence
names=('George','Gary','Gilbert')
height=(123,140,190)
dict = dict.fromkeys(names,height) #note : here keys will not take corresponding values
print dict
print partition+"[9]"

#Set
mySet = {1,2,'abcd'}
print mySet
print partition+"[10]"

#Data Conversion
print int(8.14)
print int('8')
print int('1000',2)
print float('1.23')
print float(1)
print long(123)
print long('123456')
print complex(3,4)
print tuple('Hello')
print list((1,2,3,4,5))
print hex(32)
print oct(32)
print partition+"[11]"

#Basic Operators

#Arithmetic Operators
print 1+2,2*4,4-1,24/3,8%5
print 2**3,3**2  #Exponent
print 11//3,-11//3#Floor Division
print partition+"[12]"

#Comparision Operators
print 3==3
print 3!=4,3<>4
print 3>3,2<3
print 3>=3,4<=4
print partition+"[13]"

#Assignment Operators
a=3
print a
a+=3
print a
a-=3
print a
a/=3
print a
a*=9
print a
a%=7
print a
a**=2
print a
a=-11
a//=3
print a
print partition+"[14]"

#Bitwise Operators
a = 16
b = 15
print a&b
print a|b
print a^b
print ~a,~b
print a<<1,a>>1
print partition+"[15]"

#Membership Operators
a=1
b=6
List = [1,2,3,4,5]
print a in List
print b not in List
print partition+"[16]"


#Decision Making
a=2
if a==3 :
    print "a=3"
elif a==2 :
    print "a=2"
else :
    print "a=?"
print partition+"[17]"


#Loops

#While
count = 0
while count<3 :
    count += 1
    print count

#For Loops
for letter in 'Hello World':
    print letter
languages = ['C','C++','JAVA','PYTHON']
for language in languages:
    print language
for index in range(len(languages)):
    print languages[index]
#same as above but memory allocation is different
for index in xrange(len(languages)-2):
    print languages[index]
print partition+"[18]"

#Loop control statements
#break
var = 10
while var>0:
    print var
    var-=1
    if var==5:
        break
print partition+"[19]"
#continue
while var>0:
    print var
    var-=1
    if var==5:
        break
print partition+"[20]"
#pass
#It is like a null statement : where a statement is required synatctically
#                              but as such no code is required

#Mathematical Functions
a=10;b=-10;c=1.75;d=-1.75
print abs(b),abs(d)
print math.ceil(c),math.ceil(d)
print cmp(a,c),cmp(c,a),cmp(a,abs(a))
print math.exp(2)
print math.floor(c),math.floor(d)
print math.log(e),math.log10(10)
print max(a,b),min(a,b)
print math.modf(c),math.modf(d)
print pow(2,4)
print round(c),round(d)
print math.sqrt(2)
print partition+"[21]"

#Defining a custom function
def add(a,b):
    return a+b
def _add(a,b):
    a+=5
    return a+b
# Note : All paramaters in Python are passed by reference unlike C,C++
print add(10,20);
print _add(10,20);
#keyword arguments & default arguments
def printInfo(name,age=35) :
    print name,age
    return
printInfo(age=20,name="xyz") #order doesn't matter
printInfo(name="xyzw")
#variable length arguments
def printSum(arg1,*VARIABLES) :
    total = arg1;
    for var in VARIABLES:
        total+=var
    return total
print printSum(10,20,30,40,50,60,70);

#Anonymous Functions
#They are not created by normal def keyword but using lambda keyword
#Can take any number of args but returns one value in form of expression
#have there own local namespace so cannot access any other parameters other than its parameter list
mult  = lambda arg1,arg2 : arg1*arg2
print mult(10,10);
print partition+"[22]"

#functions for generating random numbers

#choice function to select numbers randomly from a given list,tuple or string
print random.choice([1,2,3,4,5,6,7,8,9]);
print random.choice((1,2,3,4,5,6,7,8,9));
print random.choice('Hello_World!');

#randrange returns a random number from a range
# arg1 : start   arg2 : stop  step : steps to be added in a num to decide random number
print random.randrange(100,500,5);

#random function returns a float random number between 0 and 1
random.seed(17);
print random.random();

#shuffle to shuffle a list or a tuple
List = [1,2,3,4,5,6,7,8,9]
random.shuffle(List)
print List

#uniform function generates a random float between arg1 and arg2
print random.uniform(10,20)
print partition+"[23]"

#String Manipulation
String1 = "Hello World!"
print String1[6:],String1[:6]
print "Hello\vWorld" #Vertical Tab
print "Hello\tWorld" #Horizontal Tab
#print "Hello\rWorld"#Carriage Return
print 'H' in 'Hello'
print 'H' not in 'Hello'
print r'\n',R'\n'  #Raw String: Supresses escape sequences

name = 'xyz'
age  = 17
print "I am %s and I am %d years old" %(name,age)
#Format Symbols : %c:character %i:signed decimal %u:unsigned decimal
#                 %x:hexadeximal %o:octal %e:exponent %f:float
print 'hello'.capitalize()
print 'Hello World'.center(10,'-') #word centered on certain characters
print 'Missisippi'.count('is',0,len('Missisippi')) # number of times substring occurs
encode = 'HelloWorld'.encode('base64','strict') #encoding
print encode
print encode.decode('base64','strict')
print encode.endswith('\n',0,len(encode))
print 'Hello World'.endswith('ld',0,len('Hello World'))
#similar function starts with
print 'Hello\tWorld'.expandtabs(20) #increase spaces in Tab
query = "Hi Siri, Open Whatsapp on my phone"
print query.find('Whatsapp',0,len(query))   #finds substring and returns index
print query.find('abcd')
#use rfind() to search backwards
#print query.index('abcd') #same as find but raises exception
#use rindex() to search backwards
print '#dacacj%$^^'.isalnum() #checks alpha numeric
print '13432421432'.isdigit() #checks if string conatins only digits
print 'hello'.islower()
print 'HelloWorld'.lower()
#similar function isupper() and upper()
print 'HelloWorld'.swapcase()
print '     '.isspace() #returns true if string conatins whitespaces only
print '           What a beautiful morning it is !'.lstrip() #removes leading whitespaces
print 'What a beautiful morning it is !'           .rstrip() #removes trailing whitespaces
print 'What a beautiful morning it is !'.split(" ",3) #splits string using delimiter with no of strings specified
print 'What a beautiful morning it is !'.split(" ") #splits string using delimiter
print max('Hello World') #returns max alphabet according to ASCII
print max('Hello world')
print 'check thsi out, coz thsi is gr8'.replace('thsi','this')
print partition+"[24]"

#File I/O

#Read from keyboard
idiom = raw_input("Enter an idiom")
print idiom

#File Reading and Writing Modes
# r,rb,r+,rb+
# w,wb,w+,wb+
# a,ab,a+,ab+

myFile = open("myFile.txt","w")
print myFile.name,myFile.closed,myFile.mode
para = raw_input("Tell me some about yourself...(In 10 words)\n")
myFile.write(para)
myFile.close()
myFile = open("myFile.txt","r")
print myFile.read()
myFile.close()

#Tell and Seek
# tell : tells you current position within the file where we start
# seek : helps us to go a specified position in the file to do I/O
myFile = open("myFile.txt","r")
print myFile.tell()
#myFile.seek(3,0) means read three bytes from beginning of file
#myFile.seek(3,1) means read three bytes from current position
myFile.seek(len(para)-3,2) #means read 3 bytes from end of file
print myFile.tell()
str = myFile.read()
print str
myFile.close()
print partition+"[25]"

#Rename and Delete File
os.rename("myFile.txt","myNewFile.txt")
os.remove("myNewFile.txt")

#Object Oriented Programming
class Student:
    'Class to store details of students in a school'
    studentCount = 0
    __count = 0 #private data member

    #constructor
    def __init__(self,name,rollNo):
        self.name = name
        self.rollNo = rollNo
        Student.studentCount+=1

    #functions
    #Note: Each method in class should have first argument as self
    #      We don't need to add self while calling function using object
    def displayStudent(self):
        print self.name,self.rollNo

    def displayStudentCount(self):
        print self.studentCount,self.__count

    #printable string representation of class
    def __str__(self):
        return 'Student(%s, %d)' % (self.name,self.rollNo)

    #destructor
    def __del__(self):
        print "Destructor is called"

stu1 = Student("XYZ",007)
stu1.displayStudent()
stu1.displayStudentCount()
print stu1
print hasattr(stu1,'name')
print getattr(stu1,'name')
setattr(stu1,'name',"PQR")
print "Private Attribute:",hasattr(stu1,'__count') #cannot be accessed
#delattr(stu1,'name') to delete attribute
stu1.displayStudent()
#Built-in class attributes
print "Dict  :",Student.__dict__;
print "Doc   :",Student.__doc__;
print "Bases :",Student.__bases__;
print "Name  :",Student.__name__;
print "Module:",Student.__module__;
del stu1

class Parent:        # define parent class
   parentName = "Parent"
   def __init__(self):
      print "Parent Constructor Called..."

   def parentMethod(self):
      print "Parent Method Called..."

   def setAttr(self, name):
      Parent.parentName = name

   def getAttr(self):
      print "Parent Attribute :", Parent.parentName

class Child(Parent): # define child class
   def __init__(self):
      print "Child Constructor Called..."

   def childMethod(self):
      print 'Child Method Called'

child = Child()                 # instance of child
child.childMethod()             # child calls its method
child.parentMethod()            # calls parent's method
child.setAttr("Parent-Child")   # again call parent's method
child.getAttr()                 # again call parent's method
print issubclass(Child,Parent),isinstance(child,Child) #checks if it is subclass and instance of particular class
print partition+"[26]"
