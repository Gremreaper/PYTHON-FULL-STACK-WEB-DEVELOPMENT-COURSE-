#loops and control statements

#if statement-for control flow

value=int(input("enter the number:")) #initially it was string but now we have changed to integer 
if value >=18:
    print("eligible")
else:
    print("Not eligible")


#if,if-else,nested if else
 

if bool(value % 2) == False:
    print("its an even number")
else:
    print("its an odd number")


age=float(input("Enter the age:"))
if(age<18):
    print("Your age {} is not eligible".format(age))
else:
    print("Your age {} is eligible".format(age))



#multiple if-else case

number = int(input("enter the value:"))
if(number >1 and number <5):
    print("The number {} is good".format(number))
elif (number>=6 and number <=9):
    print("The number {} is okay".format(number))
else:
    print("The number {} is very poor".format(number))


# and or & both are same

#nested if else case

age = float (input("enter the age:"))
if(age<18):
    print("Minor Age")
    if(age<15):
        print("You are in School")
    else:
        print("You are in College")
elif (age>=18 and age <=25):
    print("Mid Age")
elif(age>45 and age<=50):
    print("Senior Mid Age")
else:
    print("Senior Citizen")




#loops for the iteration of work --> start,end conditon and work to be done

#for,while,do while and break,continue statements

lst=[1,2,3,4,5,6,7] #its a list
for i in lst:
    print(i)
    print(pow(i,2))

# find the sum of all the elements in the list

lst=[1,2,3,4,5,6,7,8]
sum=0
for i in lst:
    sum = sum +i

print("The value of sum is {}".format(sum))

#task is to find the sum of even and odd numbers

lst=[1,3,4,7,9,3,2]
sum1=0,sum2=0
for i in lst:
    if(bool(i%2)==False):
        sum1 = sum1 +i
    else:
        sum2= sum2 +i

print("The sum of even numbers is: {} and for odd numbers is:{}".format(sum1,sum2))


#while loop in Python --> till conditon is true,loop continues

i = 10
even_sum = 0
odd_sum = 0

while i != 0:
    if i % 2 == 1:
        odd_sum += i
        if(i==4):
            continue
        elif(i>4):
            break
    else:
        even_sum += i
    i -= 1 

print(even_sum, odd_sum) 

#print all the numbers in the reverse pattern


