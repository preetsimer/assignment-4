#question 1
l=[]
n=int(input("Enter size of list "))
print("Enter list elements ")
for i in range(1,n+1):
    a=input()
    l.append(a)
l.reverse()
print(l)


#question 2
str1=input("Enter a string ")
str2=""
l=len(str1)
for i in range(0,l):
    c=str1[i]
    if c.isupper()==True:
        str2=c+str2
print("The upper case letters from the string are ",str2[::-1])


#question 3
n=input("Enter a number ")
le=len(n)
li=[]
for i in range(0,le):
    d=n[i]
    d=int(d)
    li.append(d)
print(li)    



#question 4
str1=input("Enter a String ")
str2=str1[::-1]
if str2==str1:
    print("Palindrome String")
else:
    print("Not a palindrome String")

    
#question 5
import copy
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
#Using normal assignment operator to copy:
d = c
print (id(c)," == ",id(d))          # True - d is the same object as c
print (id(c[0])," == ",id(d[0]))   # True - d[0] is the same object as c[0]
#Using a shallow copy:
d = copy.copy(c)
print (id(c) ," == ", id(d) )         # False - d is now a new object
print (id(c[0])," == ",id(d[0]))    # True - d[0] is the same object as c[0]
#Using a deep copy:
d = copy.deepcopy(c)
print (id(c)," == ", id(d) )         # False - d is now a new object
print (id(c[0]) ," == ", id(d[0]))    # False - d[0] is now a new object

'''
Difference Between Shallow copy and Deep copy:

A shallow copy constructs a new compound object and then (to the extent possible)
inserts references into it to the objects found in the original.
The new variable refers to the original variable. In this case, if the new one
altered the changes are reflected on the original variable as well.

A deep copy constructs a new compound object and then, recursively,
inserts copies into it of the objects found in the original.
Now changes made on deeply copied variable will not affect the original one.
'''
    
    






          
