"""
This is the fourth chapter of The Python Workbook 
the solution to the exercise
'Function Exercise'
"""
from math import sqrt
#Exercise 81
# print('Let calculate the hypotenus, You will provide me' \
#     +'with the length of two short part of the triangle\n')

# user_a=int(input('What is the length of the first short part:\n\t'))

# user_b=int(input('What is the length of the second short part:\n\t'))

# def cal_hypo(user_a,user_b):
#     hypo=sqrt(user_a**2+user_b**2)
#     print('the hypotenus of the triangle is %.4f'%hypo)

# if __name__ == "__main__":
#     cal_hypo(user_a,user_b)

#Exercise 82
# base_fare=4

# change_fare=0.25

# base_distance=140

# user_=int(input('Enter the distance travel in kilometers:\n\t'))

# total_fare=0

# def calc_fare(user_):
#     distance=user_*1000
#     if distance<=base_distance:
#         total_fare=base_fare
#     else:
#         distance=distance-base_distance
#         total_fare=base_fare+(distance*change_fare)
#     print('your total fare is',total_fare)
# if __name__ == "__main__":
#     calc_fare(user_)

#Exercise 83
# base_shipment=10.95

# change= 2.95

# user_=int(input('Enter the quantity of the product:\n\t'))

# total_cost=0

# def total_shipment(user_):
#     if user_==1:
#         total_cost=base_shipment
#     else:
#         total_cost=base_shipment+((user_-1)*change)
#     print('the total shipment is $%.2f' %total_cost)

# if __name__ == "__main__":
#     total_shipment(user_)

#Exercise 84

# print('provide me with three different number and i will tel you the median\n')

# user_a=int(input('What is your first value:\n\t'))
# user_b=int(input('What is the second value:\n\t'))
# user_c=int(input('What is the third value:\n\t'))

# def median(a,b,c):
#     if a > b:
#         if a < c:
#             medi = a
#         elif b > c:
#             medi = b
#         else:
#             medi = c
#     else:
#         if a > c:
#             medi = a
#         elif b < c:
#             medi = b
#         else:
#             medi = c

#     print("The median is", medi)

# median(user_c,user_b,user_a)

#Exercise 85
# user_=int(input('Enter the integer for it ordinary number:\n\t'))

# def ordinary(a):
#     if a==1:
#         return 'First'
#     elif a==2:
#         return 'Second'
#     elif a==3:
#         return 'Third'
#     elif a==4:
#         return 'Fourth'
#     elif a==5:
#         return 'Fifth'
#     elif a==6:
#         return 'Sixth'
#     elif a==7:
#         return 'Seventh'
#     elif a==8:
#         return 'Eighth'
#     elif a==9:
#         return 'Nineth'
#     elif a==10:
#         return 'Tenth'
#     elif a==11:
#         return 'Eleventh'
#     elif a==12:
#         return 'Twelveth'
#     else:
#         return ''

# if __name__ == "__main__":
#     if ordinary(user_)=='':
#         print('This is out of range')
#     else:
#         print('The ordinary number responding to the integer is'\
#             ,ordinary(user_))

#Exercise 86
# user_=int(input('Enter the day of you want:\n\t'))
# print('\n\non the',ordinary(user_),'day christmas\nMy true love gave to me')

# def chorus(a):
#     if a>=12:
#         print('12 drummers drumming')
#     if a>=11:
#         print('Eleven pipers piping')
#     if a>=10:
#         print('Ten lords a leaping')
#     if a>=9:
#         print('Nine ladies dancing')
#     if a>=8:
#         print('Eight maids a milking')
#     if a>=7:
#         print('Seven swans a swimming')
#     if a>=6:
#         print('Six geese a laying')
#     if a>=5:
#         print('Five gold rings, badam-pam-pam')
#     if a>=4:
#         print('Four calling birds')
#     if a>=3:
#         print('Three French hens')
#     if a>=2:
#         print('Two turtle doves')
#     if a==1:
#         print('A'," partridge in a pear tree")
#     else:
#         print('And a',' partridge in a pear tree')
#     # print('partridge in a pear tree')
# chorus(user_)

# def main():
#     for i in range(1,13):
#         chorus(i)
# main()

#Exercise 87
# user_=input('Enter a string to be centralize on your screen:\n')
# user_w=int(input('What is the width of your screen:\n\t'))

# def centalize(a,b):
#     user_l=len(a)
#     half_user_l=user_l//2
#     half_w=b//2
#     start=half_w-half_user_l
#     print(' '*start,user_)

# def main():
#     centalize(user_,user_w)

# main()

#Exercise 88
# print('Your will provide me with three side length')
# print('And i will determine whether is can used for a triangle\n')
# user_a=int(input('Enter the first length:\n\t'))
# user_b=int(input('Enter the second length:\n\t'))
# user_c=int(input('Enter the third length:\n\t'))

# def triangle(a,b,c):
#     if (a>(b+c)) or (b>(a+c)) or (c>(b+a)):
#         print('A triangle cannot be formed')
#     else:
#         print('A triangle can be formed')

# def main():
#     triangle(user_a,user_b,user_c)
# main()

#Exercise 89
# def capitalize(s):
#     result=s.replace(' i ',' I ')
    
#     if len(s) >0:
#         result = result[0].upper()+\
#             result[1:len(result)]

#     pos=0
#     while pos< len(s):
#         if result[pos]=='.' or result[pos]=='!' or result[pos]=='?':
#             pos=pos+1
#             while pos <len(s) and result[pos]==' ':
#                 pos=pos+1 
#             if pos<len(s):
#                 result=result[0:pos]+\
#                     result[pos].upper()+\
#                         result[pos+1:len(result)]

#         pos=pos+1

#     return result


# def main():
#     s=input('Provide your sentence:\n\t')
#     capitaled=capitalize(s)
#     print('The capitalized word is:',capitaled)

# main()

#Exercise 90
# def isInteger(a):
#     a=a.strip()

#     if (a[0]=='+' or a[0]=='-') and a[1:].isdigit():
#         return True
#     if a.isdigit():
#         return True
#     return False

# def main():
#     a=input('Enter a string:\n\t')
#     if isInteger(a):
#         print('That string represent an integer')
#     else:
#         print('That string does not represent an integer')

# if __name__ == "__main__":
#     main()

#Exercise 91
# def precedence(s):
    
#     if s[0]=='+' or s[0]=='-':
#         return '1'
#     elif s[0]=='*' or s[0]=='/':
#         return '2'
#     elif s[0]=='^':
#         return '3'
#     else:
#         return '-1'

# def main():
#     user_=input('Enter the string:\n\t')
#     output=precedence(user_)
#     print(output)

# if __name__ == "__main__":
#     main()
        
#Exercise 92
# def isPrime(a):
#     if a<=1:
#         return False
#     for i in range(2,a):
#         if a%i==0:
#             return False
    
#     return True

# def main():
#     user_=int(input('Please provide the number:\n\t'))
#     if isPrime(user_):
#         print('The number',user_,'is a prime number')
#     else:
#         print('The number',user_,'is not a prime number')

# if __name__ == "__main__":
#     main()

#Exercise 93
# def nextPrime(a):
#     nextPrimen=a+1
#     if  isPrime(a):
#         while (nextPrimen>a) :
#             if isPrime(nextPrimen):
#                 return nextPrimen
#                 break
#             else:
#                 nextPrimen+=1

#     return False

# def main():
#     user_=int(input('what is number:\n\t'))
#     check=nextPrime(user_)
#     if check!= False:
#         print('the next prime number is',check)
#     else:
#         print('Number aint a prime')

# if __name__ == "__main__":
#     main()

#Exercise 94
# from random import randint,choice
# long_n= 9
# short_n= 7
# acsii_short = 33
# acsii_long = 126
# def randomPassword():
#     pass_length=randint(short_n,long_n)
#     password=''
#     while len(password)<=pass_length:
#         new_pass=chr(randint(acsii_short,acsii_long))
#         password+=new_pass
    
#     return password

# def main():
#     new_password=randomPassword()
#     print('Your random password is',new_password)


# if __name__ == "__main__":
#     main()

#Exercise 95
import string
# license_len=randint(6,7)


# def random_license():
#     licensen=''
#     if license_len==7:
#         for i in range(3):
#             new_letter=str(randint(0,10))
#             licensen+=new_letter
#         for i in range(4,8):
#             new_letter=choice(string.ascii_letters)
#             licensen+=new_letter
#     else:
#         for i in range(3):
#             new_letter=choice(string.ascii_letters)
#             licensen+=new_letter
#         for i in range(4,7):
#             new_letter=str(randint(0,10))
#             licensen+=new_letter
#     return licensen

# def main():
#     numb=random_license()
#     print('Your license number is',numb)

# if __name__ == "__main__":
#     main()

#Exercise 96
# def passwordCheck(a):
#     upper_check=False
#     lower_check=False
#     number_check=False

#     for i in a:
#         if i>='A' and i<='Z':
#             upper_check=True
#         elif i>='a' and i<='z':
#             lower_check=True
#         elif i>='0' and i<='9':
#             number_check=True

#     if len(a)>=8 and upper_check and lower_check and number_check:
#         return True


# def main():
#     user_=input('Enter your password:\n\t')
#     if passwordCheck(user_):
#         print('Your password is good')
#     else:
#         print('Your password is bad')

# if __name__ == "__main__":
#     main()

#Exercise 97
# def random_pass_check():
#     count=0
#     stop=True
#     while stop:
#         password=randomPassword()
#         isgood=passwordCheck(password)
#         count=+1
#         if isgood:
#             print('Your strong random password is',password)
#             print('It took about',count,'times to get it')
#             stop=False

# def main():
#     random_pass_check()

# if __name__ == "__main__":
#     main()


#Exercise 98
# def hex2int(n):
    
#     n=n.upper()
#     length=len(n)-1
#     base_ten=0
#     for j in n:
#         if j =='A':
#             result=10*(16**length)
#         elif j=='B':
#             result=11*(16**length)
#         elif j=='C':
#             result=12*(16**length)
#         elif j=='D':
#             result=13*(16**length)
#         elif j=='E':
#             result=14*(16**length)
#         elif j=='F':
#             result=15*(16**length)
#         else:
#             result=int(j)*(16**length)
#         length-=1
#         base_ten+=result
#         if length<0:
#             break

#     return base_ten

# n=hex2int('16a45f8')
# print(n)

# def int2hex(n):
    
#     if n.isdigit()==False:
#         return 'Invalid parameter,check and re-enter'
#     else:
#         value=int(n)
#         base_hex=''
#         while True:
#             remainder=value%16
#             if remainder==10:
#                 base_hex='A'+base_hex
#             elif remainder==11:
#                 base_hex='B'+base_hex
#             elif remainder==12:
#                 base_hex='C'+base_hex
#             elif remainder==13:
#                 base_hex='D'+base_hex
#             elif remainder==14:
#                 base_hex='E'+base_hex
#             elif remainder==15:
#                 base_hex='F'+base_hex
#             else:
#                 base_hex=str(remainder)+base_hex
#             value=value//16
#             if value==0:
#                 break

#         return base_hex

# n=int2hex('23741944')

# print(n)

#Exercise 99
# def base_10_to_16(n):
#     value=int(n)
#     base_hex=''
#     while True:
#         remainder=value%16
#         if remainder==10:
#             base_hex='A'+base_hex
#         elif remainder==11:
#             base_hex='B'+base_hex
#         elif remainder==12:
#             base_hex='C'+base_hex
#         elif remainder==13:
#             base_hex='D'+base_hex
#         elif remainder==14:
#             base_hex='E'+base_hex
#         elif remainder==15:
#             base_hex='F'+base_hex
#         else:
#             base_hex=str(remainder)+base_hex
#         value=value//16
#         if value==0:
#             break

#     return base_hex
    

# def base_10_to_n(n,base):
#     base_n=""
#     q=n

#     while True:
#         r=q%base
#         base_n=str(r)+base_n
#         q=q//base
#         if q==0:
#             break

#     return base_n

# def base_16_to_10(n):
#     base_ten=hex2int(n)
#     return base_ten  

# def base_n_to_10(n,base):
#     count=-1
#     for i in str(n):
#         count+=1

#     base_ten=0
#     for j in str(n):
        
#         result=int(j)*(base**count)
#         count-=1
#         base_ten+=result
#         print(result)
#         if count<0:
#             break
#     return base_ten

# def base_n_to_16(n,base):
#     base_ten=base_n_to_10(n,base)
    
#     print(base_ten)
#     value=int(base_ten)
    
#     base_hex=''
#     while True:
#         remainder=value%16
        
#         if remainder==10:
#             base_hex='A'+base_hex
        
#         elif remainder==11:
#             base_hex='B'+base_hex
            
#         elif remainder==12:
#             base_hex='C'+base_hex
            
#         elif remainder==13:
#             base_hex='D'+base_hex
            
#         elif remainder==14:
#             base_hex='E'+base_hex
            
#         elif remainder==15:
#             base_hex='F'+base_hex
                
#         else:
#             base_hex=str(remainder)+base_hex
            
        
#         value=value//16
#         if value==0:
#             break

#     return base_hex
    

# def base_16_to_n(n,base):
#     base_ten= hex2int(n)
#     base_n=base_10_to_n(base_ten,base)
#     return base_n

# def base_n_to_n(n,base_1,base_2):
#     base_ten=base_n_to_10(n,base_1)
#     base_n=base_10_to_n(base_ten,base_2)
#     return base_n


# def main():
#     user_n=input('Provide the number to be converted:\n\t')
#     current_base=int(input('What is the current base of the number:\n\t'))
#     new_base=int(input('What base do you want do want to convert it to:\n\t'))

#     if current_base ==16 and new_base==10:
#         user_n=str(user_n)
#         new_number=base_16_to_10(user_n)
#     elif current_base==10 and new_base==16:
#         user_n=int(user_n)
#         new_number=base_10_to_16(user_n)
#     elif current_base==10 and (new_base>=2 and new_base<=15):
#         user_n=int(user_n)
#         new_number=base_10_to_n(user_n,new_base)
#     # elif (current_base>=2 and current_base<=15) and new_base==10:
#     #     user_n=int(user_n)
#     #     new_number=base_n_to_10(user_n,10)
#     elif current_base==16 and (new_base>=2 and new_base<=15):
#         new_number=base_16_to_n(user_n,new_base)
#     elif (current_base>=2 and current_base<=15) and new_base==16:
#         user_n=int(user_n)
#         new_number=base_n_to_16(user_n,new_base)
#     elif (current_base>=2 and current_base<=15) and (new_base>=2 and new_base<=15):
#         user_n=int(user_n)
#         new_number=base_n_to_n(user_n,current_base,new_base) 
#     elif current_base<2 or current_base>16:
#         new_number=-1
#     elif new_base <2 or new_base >16:
#         new_number=-2


#     if new_number==-1:
#         print('The current base of the number is out of range\n')
#         print('The base should be between 2 to 16')
#     elif new_number==-2:
#         print('The converting base of the number is out of range\n')
#         print('The base should be between 2 to 16')
#     else:
#         print('The number',user_n,'in base',current_base,\
#             'converted to base',new_base,'is', new_number)
    

# if __name__ == "__main__":
#     main()

    

#Exercise 100

# def days_in_month(year,month):

#     if year%400==0:
#         leap='Yes'
#     elif year%100==0:
#         leap='No'
#     elif year%4==0:
#         leap='Yes'
#     else:
#         leap='No'

#     if leap=='No':
#         if month in (1,3,5,7,8,10,12):
#             return '31'
#         elif month in (4,6,9,11):
#             return '30'
#         elif month==2:
#             return '28'
#         else:
#             return 'invalid'
#     else:
#         if month in (1,3,5,7,8,10,12):
#             return '31'
#         elif month in (4,6,9,11):
#             return '30'
#         elif month==2:
#             return '29'
#         else:
#             return 'invalid'
        

# def main():
#     year=int(input('Please enter the year:\n\t'))
#     month=int(input('Please enter the month:\n\t'))
#     day=days_in_month(year,month)
#     print('The number of days in the month',month,'in the year',\
#         year,'is',day,'days')

# if __name__ == "__main__":
#     main()

#Exercise 101
# def fraction_reducer(first_int,second_int):

#     d=min(first_int,second_int)

#     while first_int%d !=0 or second_int%d !=0:
#         d=d-1
#     return d


# def main():
#     numerator=int(input('What is the numerator of the fraction:\n\t'))
#     denominator=int(input('What is the denominator of the fraction:\n\t'))

#     reducer=fraction_reducer(numerator,denominator)
#     reduced_numerator=numerator//reducer
#     reduced_denominator = denominator//reducer
    
#     print(f'the reduced fraction to the lowest form is {reduced_numerator}/{reduced_denominator}')

# main()


#Exercise 102
# tsp_to_tbsp=3
# tsp_to_cup=48


# def reduceMeasure(num,unit):
#     unit=unit.lower()

#     if unit=='teaspoon' or unit=='teaspoons':
#         teaspoons=num
#     elif unit=='tablespoon' or unit=='tablespoons':
#         teaspoons=num*tsp_to_tbsp
#     elif unit=='cup' or unit=='cups':
#         teaspoons=num*tsp_to_cup
    

#     cups= teaspoons//tsp_to_cup
#     teaspoons=teaspoons-(cups*tsp_to_cup)
#     tablespoons=teaspoons//tsp_to_tbsp
#     teaspoons=teaspoons-(tablespoons*tsp_to_tbsp)

#     result =''
#     if cups >0:
#         result=result +str(cups)+' cup'
#         if cups>1:
#             result=result+'s'
    
#     if tablespoons>0:
#         if result !='':
#             result+=', '
#         result+=str(tablespoons)+' tablespoon'

#         if tablespoons>1:
#             result+='s'
        
#     if teaspoons>0:
#         if result=='':
#             result+=', '
        
#         result+=str(teaspoons)+ ' teaspoon'
#         if teaspoons >1:
#             result+='s'

#     if result=='':
#         result= '0 teaspoons'

#     return result


# def main():
#     user_num=int(input('What is the quantity of the ingredient:\n\t'))
#     user_unit=input('What is the unit of the of the quantity:\n(cups,tablespoons,teaspoons)\n\t')

#     converted_quantity=reduceMeasure(user_num,user_unit)
#     print('The converted unit are '+converted_quantity)

# main()


#Exercise 103
# def magicDate(day,month,year):
#     if day*month==year%100:
#         return True
    
#     return False
    

# def main():
#     for years in range(1900,2000):
#         for months in range(1,13):
#             for days in range(1,int(days_in_month(years,months))+1):
#                 if magicDate(days,months,years):
#                     print(days,'/',months,'/',years,'is a magic date')


# main()