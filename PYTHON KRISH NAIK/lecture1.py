#python overview done in first video now its second video to start
#learning about anaconda navigator and jupyter notebook

#Basics of Python

print("Hello world")
print("Welcome to Python Programming")

# --> for single line comments(good to write)

''' 
welcome to my coding phase
this is used for multiline comments

'''

#variable declaration

#---> in python,no datatype needed to be added

a=10
type(a)
#used to check the datatype of the variable
print(type(a))

c="GAUTAM"
print(type(c))

#variable declaratio rules are same as in c and c++
first_name = "Sharma"
print(first_name)

#int,char,float,bool,string are some of data type

a=10
b=20

print(a+b)

#floating point numbers

s=190.5
print(type(s))

#changing the datatype of one variable to another datatype->typecasting
 
print(int(s)) #typecast --> float to int

print(float(b)) #int to float


#true or false-> boolean 
a1=True
b1=False

print(type(a1),type(b1))

a1 = a1 and b1
print(a1)


a1 = a1 | b1 # or operator
print(a1)

#strings in python

name1="Gautam"
print(name1)
print(type(name1))

name1+="Srivastava" #concat string

print(name1)

name1 += 1
print(name1) #would give out error -->instead do strong typing 

name1 + str(1) #dynamic or strong typing
print(name1)

#complex numbers in python -> how to define it

complex = 1.0 - 2.3j
#real and imaginary part

print(complex)
print(complex.real,complex.imag)

#string formatting

a=100
print("The value is -",a)

first_name="K"
last_name="N"

print("The first name is {0} and last name is {1}".format(first_name,last_name)) #placeholder  with the format having first and the last name

#0 means the first element and 1 means the last element -->goes by sequence

#input type

res=input("enter the name:")
print(res)

a=input("Enter the value of first number:")
b=input("Enter the second numer:")

print(int(a)+int(b)) #for not concatinating just type casting and aading both numbers
