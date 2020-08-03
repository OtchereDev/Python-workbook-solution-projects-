"""
This is the third chapter of The Python Workbook 
the solution to the exercise
'Loop Exercise'
"""

#Exercise 61
# print('Let calculate the average of your collection of values')
# print('Please enter "0" if you dont have any more input')

# input_=True
# value=0
# n=0

# while input_:
#     user_=int(input('What is the value of the item:\n\t'))
    
#     if user_==0:
#         print('Thank you for your input, calculaing your average')
#         input_=False
#     else:
#         n+=1
#         value+=user_

# if value==0:
#     print('Your total average is',value)
# else:
#     average=value/n
#     print('The total average is',average)

#Exercise 62
# prices=[4.95,9.95,14.95,19.95,24.95]
# print('Let calculate the discount')

# for price in prices:
#     discount=price *0.6
#     new_price=price - discount
#     print('Original price: %.2f'%price)
#     print('Discount: %.2f'%discount)
#     print('New price: %.2f \n'%new_price)

#Exercise 63
# deg_cel= [x for x in range(0,101,10)]

# print('Degree Celsius\tDegree Fahrenit')
# for i in deg_cel:
#     fah= (i*1.8)+32
#     print(i,"\t\t",fah)
    
#Exercise 64
#to-do

#Exercise 65
# from math import sqrt
# print('let calculate the perimeter of the polygon')

# perimeter=0

# user_x=float(input('Enter the x part of the cordinate:\t'))
# user_y=float(input('Enter the y part of the cordinate:\t'))

# old_x= user_x
# old_y= user_y

# user_xx=float(input('Enter the x part of the coordinate: (blank to quit):\t'))

# try:
#     while user_xx != "":
#         x=user_xx
#         y= float(input('Enter the y of the cordinate:\t'))

#         distance=sqrt((old_x-x)**2+(old_y-y)**2)
#         perimeter+=distance

#         old_x=x
#         old_y=y

#         user_xx=float(input('Enter the x part of the coordinate: (blank to quit):\t'))
# except ValueError:
#     distance=sqrt((user_x-x)**2+(user_y-y)**2)
#     perimeter+=distance

#     print('The perimeter of the polygon is',perimeter)

#Exercise 66
# result=0
# cont_=True

# while cont_:
#     input_=input('Enter your letter grade in caps (eg. A):\n\t')

#     if input_=='A+' or input_=='A':
#         result+=4.0
#     elif input_=='A-':
#         result+=3.7
#     elif input_=='B+':
#         result+=3.3
#     elif input_=='B':
#         result+=3.0
#     elif input_=='B-':
#         result+=2.7
#     elif input_=='C+':
#         result+=2.3
#     elif input_=='C':
#         result+=2.0
#     elif input_=='C-':
#         result+=1.7
#     elif input_=='D+':
#         result+=1.3
#     elif input_=='D':
#         result+=1.0
#     elif input_=='F' or input=='':
#         result+=0
#     else:
#         print('Your letter grade is incorrect.')
#         break
    
#     input_c=input('Do you have any othe grade to enter (enter y for Yes or n for n):\n\t')
#     if input_c=='':
#         break
#     else:
#         continue

# print('your total grade point is',result)

#Exercise 67
# print('To help determine your total admission cost enter the age of each individual in your group')

# cost=0
# cont_=True

# age=int(input('What is the age of the first person:\n\t'))

# while cont_:
#     if age <= 2:
#         cost+=0
#     elif age >=3 and age <=12:
#         cost+=14
#     elif age>=65:
#         cost+=18
#     else:
#         cost+=23
#     try:
#         age=int(input('What is the age of the next person:\n\t'))
#     except ValueError:
#         break

# print('Your total cost of admission is', cost)

#Exercise 68
# bits=input('Please enter the bit:\n\t')

# while bits != '':
#     if bits.count('0') + bits.count('1') != 8 or len(bits)!=8:
#         print('That not correct, provide an 8 bits')
        
#     else:
#         ones=bits.count('1')
    
#         if ones%2==0:
#             print('The parity is 0')
#         else:
#             print('The parity is 1')

#     bits=input('Please enter the bit:\n\t')

#Exercise 69
# print('Let do some approximation of pi')
# iteration = 1000000
# multiplier = 1.0
# start_deno=2.0
# pi = 3.0

# for i in range(1,iteration+1):
#     pi+=((4.0/(start_deno*(start_deno+1)*(start_deno+2))*multiplier))

#     start_deno+=2
#     multiplier*=-1
# print(pi)

#Exercise 70
# message=input('Enter the message:\n\t')
# shift=int(input('Enter the shift value:\n\t'))

# deciphed_message=''

# for i in message:
#     if i>='a' and i <='z':
#         position=ord(i)-ord('a')
#         position=(position+shift)%26
#         new_letter= chr(position+ord('a'))
#         deciphed_message+=new_letter
#     elif i>='A' and i<='Z':
#         position=ord(i)-ord('A')
#         position=(position+shift)%26
#         new_letter= chr(position+ord('A'))
#         deciphed_message+=new_letter
#     else:
#         deciphed_message+=i

# print('The real message is',deciphed_message)


#Exercise 71
# user_=int(input('Enter the value of x:\n\t'))

# guess=1

# not_good= True

# while not_good:
#     f_x=guess**2-user_
#     fi_x=2*user_
#     squrt= (guess-(f_x/fi_x))
#     # print(squrt)
#     guess=squrt
#     # print(guess)

#     if abs(((guess*guess)-user_))<=10e-12:
#         break
    
# print(squrt)

#Exercise 72 
# user_=input('Enter your message:\n\t')

# ispalidrome=True

# for i in  range(0,len(user_)//2):
#     if user_[i] != user_[len(user_)-i-1]:
#         ispalidrome= False

# if ispalidrome==True:
#     print(user_,'that is a palidrome')
# else:
#     print(user_,'is not a palidrome')
    
# Exercise 73
# user_=input('Enter your message:\n\t')

# punt='.,'
# new_user_=''

# for i in user_:
#     if i not in punt:
#         new_user_+=i

# new_user_=new_user_.replace(" ",'')

# ispalidrome=True

# for i in  range(0,len(new_user_)//2):
#     if new_user_[i] != new_user_[len(new_user_)-i-1]:
#         ispalidrome= False

# if ispalidrome==True:
#     print(user_,'that is a palidrome')
# else:
#     print(user_,'is not a palidrome')

#Exercise 74
# print("    ",end='')
# for i in range(1,11):
#     print("%4d"%i,end='')
# print()
# for i in range(1,11):
#     print('%4d'%i, end='')
#     for j in range(1,11):
#         result=i*j
#         print('%4d' %result, end="")
#     print()

#Exercise 75
# user_1=int(input("Please enter m:\n\t"))
# user_2=int(input("Please enter n:\n\t"))

# d=min(user_1,user_2)

# while user_1%d !=0 or user_2%d !=0:
#     d=d-1
# print(d)

#Exercise 76
# user_=int(input('Enter an integer greater than or equal to two:\n\t'))

# factor=2

# while factor<=user_:
#     if user_%factor==0:
#         user_=user_//factor
#         print(factor)
#     else:
#         factor+=1
    
#Exercise 77
# user_=int(input('Enter the number in base 2:\n\t'))

# count=-1
# for i in str(user_):
#     count+=1

# base_ten=0
# for j in str(user_):
    
#     result=int(j)*(2**count)
#     count-=1
#     base_ten+=result
#     if count<0:
#         break

# print('the base 10 of the ',user_,' is ',base_ten)

#Exercise 78
# user_=int(input('Enter the number in base 10:\n\t'))

# result=""
# q=user_

# while True:
#     r=q%2
#     result=str(r)+result
#     q=q//2
#     if q==0:
#         break

# print(result)

#Exercise 79
from random import randint

# maxi=randint(1,100)
# count=0

# print('We start with',maxi)

# for i in range(1,100):
#     new=randint(1,100)
#     if new>maxi:
#         maxi=new
#         count+=1
#         print(new,"<== updated")
#     else:
#         print(new)

# print('The maximum number is',maxi)
# print('The number of update is',count)

#Exercise 80

# flips=''
# prob=''
# count=0
# run = True
# simu=10


# while run:
#     flip=randint(1,2)
#     if flip==1:
#         prob+='H  '
#     else:
#         prob+='T  '
#     flips+=str(flip)
#     count+=1
    
#     if flips[-3:]==str(111):
#         run=False
#     elif flips[-3:]==str(222):
#         run=False
#     else:
#         continue

#     print(prob,'(',count,"flips)")


