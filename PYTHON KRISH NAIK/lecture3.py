#python operators --> logical ,equality,comparision,bitwise and arithmatic

a=True
b=False

print(a and b)
print(a or b)
print (not(a and b))

age =int (input("enter the age:"))
if age >18 and age <=35:
    print("Mid age")


#equality operators

# is,is not,== and !=

a ="Gautam"
b="Srivastava"

print(a==b) #checks the value

#if id value of 2 variables are same,means they are pointing to same object

print(id(a))

# a is b -->means two variables point to the same object (memory location)

lst=[1,2,3]
lstd=[1,2,3,4]

print(id(lst))
print(id(lstd))

print(id(lst) is not id(lstd))

#comparision operators (<,<=,>,>= )

marks= int(input("enter the marks:"))
if marks >=35:
    print("Passed")
elif marks <=50 and marks>45:
    print("First class")
elif marks <35:
    print("Fail")


#arithmatic operators -> +,-,*,/(gives value in float),// ->integer divison(no decimal gives the floor value),% 