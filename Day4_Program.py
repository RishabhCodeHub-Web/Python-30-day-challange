 #type conversion

a = 55
b = 55.65
sum = (a+b)
print (sum) # in python you are add aur do any mathmatic thing python give you answer in float value. Like :- 55+55.65 => 110.65 



#type casting 
# a = "99"              # Because of double quorts 99 change in number (intigers) to text (string).

a = int ("99")          # But in type casting it is a possible, reason is int that in input after a that is make it string to intigers. If you want to change in 
b = 99                  # intigers to float you can you just need to wite 'float' instead of 'int'.
print (type(a))
print (a+b) 

a = 6.22                # Even if it is a float but we can change it in (int) to help of type casting
a = int(a)
print (type (a))


#  Input in Python

name = input ("Enter you Name")
print ("welcome", name)

val = input ("Enter some value")
print ((type), val)


name = input ("enter you name")
age = input ("enter your age")
mark = input ("endter your mark")
print ("enter you name ", name)
print ("enter you age ",age)
print ("enter you mark ", mark)



first = int(input("enter first"))
second = int (input("enter second"))
print ("sum = ", first + second)


side = float(input (" enter the side"))
print ("area = ", side * side)