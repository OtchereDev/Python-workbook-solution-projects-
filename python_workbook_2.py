"""
This is the second chapter of The Python Workbook 
the solution to the exercise
'If Statement Exercise'
"""

#Exercise 34
# print('Enter any a number and i will tell you if it is even\n')
# user_input=int(input('What is your number:\n\t'))

# if user_input%2 == 0:
#     print('That an even number!!')
# elif user_input%2 ==1:
#     print('that an odd number!!')
# else:
#     print('I dont know what you doing')

#Exercise 35
# age_input=int(input('Enter your age:\n\t'))

# if age_input < 0:
#     print('Your age cannot be negative!!')
# elif age_input<=2:
#     h_age=age_input*10.5
# elif age_input > 2:
#     h_age=(10.5*2)+(age_input-2)*4

# print("The equivalent of your human age in dog is %.3f" %h_age)

#Exercise 36
# user_input=input('Enter an alaphabet:\n\t')
# if user_input not in ['a','e','o','i','u']:
#     print('that is a consonant!!')
# else:
#     print('that is a vowel')

#Exercise 37
# print('I will tell you the name of the side by the number you enter\n')
# print('The number must be between 3 to 10\n')

# user_input=int(input('Enter your number:\n\t'))
# if user_input<3:
#     print('Remember your rule')
# elif user_input==3:
#     print('that is a triangle')
# elif user_input==4:
#     print('That is a rectangle')
# elif user_input==5:
#     print('That a pentagon')
# elif user_input==6:
#     print('That is a hexagon')
# elif user_input==7:
#     print('that is a heptagon')
# elif user_input==8:
#     print('that is an octagon')
# elif user_input==9:
#     print('That is a nonagon')
# elif user_input==10:
#     print('That is a decagon')
# else:
#     print('You are out of range')

#Exercise 38
# print("Enter the first three letter of the month's (eg.January = Jan)\n")
# print('I will provide you with the number of days in the months\n')
# user_input=input('Which month do you want:\n\t')

# if user_input in ['jan','mar','may','jul','aug','oct','dec']:
#     print('%s has 31 days'%user_input)
# elif user_input in ['sep','apr','jun','nov']:
#     print('%d has 30days' % user_input)
# elif user_input=='feb':
#     print('Feb has 28day or 29day in a leap year')
# else:
#     print('Check your input')

#Exercise 39
# Jackhammer = 130 
# Gas_lawnmower = 106 
# Alarm_clock = 70 
# Quiet_room = 40

# user_input=int(input('Enetr your sound level in dB: (provide digits only)\n\t'))

# if user_input<Quiet_room:
#     print('Below a quiet room level!')
# elif user_input==Quiet_room :
#     print('The level is Quiet room')
# elif user_input>Quiet_room and user_input<Alarm_clock:
#     print('That level is between Quiet room and Alarm Clock')
# elif user_input ==Alarm_clock:
#     print('That level is Alarm Clock')
# elif user_input>Alarm_clock and user_input<Gas_lawnmower:
#     print('That levl is between Alarm clock and Gas lawnmower')
# elif user_input==Gas_lawnmower:
#     print('that level is Gas lownmover')
# elif user_input>Gas_lawnmower and user_input<Jackhammer:
#     print('That level is between Gas lawnmower and Jackhammer')
# elif user_input==Jackhammer:
#     print('That level is Jackhammer')
# else:
#     print('that is above jackhammer level')

#Exercise 40
# print('I will tell what type of triangle you have\n')
# print('You will tell me the length of the three side')

# side_1=int(input('What is the first side:\n'))
# side_2=int(input('what is the second side:\n'))
# side_3=int(input('What is the third side:\n'))

# if side_1==side_2 and side_2==side_3:
#     print('That is an equilateral triangle')
# elif side_1==side_2 or side_2==side_3 or side_3==side_1:
#     print('That is a isoleces triangle ')
# else: 
#     print("That is an scalene triangle")

#Exercise 41
# C4=261.63 
# D4=293.66 
# E4=329.63 
# F4=349.23 
# G4=392.00 
# A4=440.00 
# B4=493.88

# user_input=input('Please enter the note (such as D4):\n\t')

# letter=user_input[0]
# number=int(user_input[1])

# if letter=="C":
#     freq=C4
# elif letter=="D":
#     freq=D4
# elif letter=="E":
#     freq=E4
# elif letter=="F":
#     freq=F4
# elif letter=="G":
#     freq=G4
# elif letter=="A":
#     freq=A4
# elif letter=="B":
#     freq=B4 

# note_freq= freq/2**(4-number)

# print('the frequency of the you entered is',note_freq)

#Exercise 42
# C4=261.63 
# D4=293.66 
# E4=329.63 
# F4=349.23 
# G4=392.00 
# A4=440.00 
# B4=493.88

# user_input=float(input('Please enter the frequency:\n\t'))
# if user_input>=C4-1 and user_input<=C4+1:
#     print('C4')
# elif user_input>=D4-1 and user_input<=D4+1:
#     print('D4')
# elif user_input>=E4-1 and user_input<=E4+1:
#     print('E4')
# elif user_input>=F4-1 and user_input<=F4+1:
#     print('F4')
# elif user_input>=G4-1 and user_input<=G4+1:
#     print('G4')
# elif user_input>=A4-1  and user_input<=A4+1:
#     print('A4')
# elif user_input== B4-1 and user_input<= B4+1:
#     print('B4')
# else:
#     print('Not in range')

#Exercise 43
# user_input=input('What banknote are you holding(enter as such $1):\n\t')

# if user_input=='$1':
#     figure="George Washington"
# elif user_input=='$2':
#     figure="Thomas Jefferson"
# elif user_input=='$5':
#     figure="Abraham Lincolnn"
# elif user_input=='$10':
#     figure="Alexander Hamilton"
# elif user_input=='$20':
#     figure="Andrew Jackson"
# elif user_input=='$50':
#     figure="Ulysses S. Grant"
# elif user_input=='$100':
#     figure="Benjamin Franklin"
# else:
#     figure=''

# if figure=='':
#     print('The note does not exist')
# else:
#     print('The personality on the banknote is',figure)

#Exercise 44
# January_1 ='New year’s day' 
# July_1 ='Canada day'
# December_25='Christmas day'

# user_input=input('Enter the month and the day (such as July 6):\n\t')

# if user_input=='January 1':
#     holiday=January_1
# elif user_input=='July 1':
#     holiday = July_1
# elif user_input=='December 25':
#     holiday==December_25
# else:
#     holiday=''

# if holiday=='':
#     print('No corresponding holiday')
# else:
#     print('The holiday that corresponds to the date is ',holiday)

#Exercise 45
# user_input=input('Which color does the first column begin with (eg Black or White):\n\t')

# if user_input not in ['Black','White']:
#     print('The chess board color out of range (it either Black or White)')
# else:    
#     input_=input('Enter your chess position (such as d4):\n\t')

#     if user_input=="Black":
#         if input_[0] in ['a','c','e','g'] and (int(input_[1])%2==0):
#             position='white'
#         elif input_[0] in ['a','c','e','g'] and (int(input_[1])%2!=0):
#             position='black'
#         elif input_[0] in ['b','d','f','h'] and (int(input_[1])%2!=0):
#             position='white'
#         elif input_[0] in ['b','d','f','h'] and (int(input_[1])%2==0):
#             position='black'
#         elif input_[0] not in ['a','c','e','g','b','d','f','h']:
#             position='not in'
#         elif input_[1] not in [x for x in range(1,9)]:
#             position='not in'
#     elif user_input=="White":
#         if input_[0] in ['a','c','e','g'] and (int(input_[1])%2==0):
#             position='black'
#         elif input_[0] in ['a','c','e','g'] and (int(input_[1])%2!=0):
#             position='white'
#         elif input_[0] in ['b','d','f','h'] and (int(input_[1])%2!=0):
#             position='black'
#         elif input_[0] in ['b','d','f','h'] and (int(input_[1])%2==0):
#             position='white'

#     if position=='not in':
#         print('The chess position is not valid. Re-enter the correct position')
#     else:
#         print("You are on the color that correspond to your position is",position)

#Exercise 46
# spring=['march','april','may','june']
# summer=['june','july','august','september']
# fall=['september','october','november','december']
# winter=['december','january','febuary','march']
# print('i will tell the season of the year if you provide me the date\n')
# user_m=input('Enter the month (eg. Decemeber):\n\t')
# user_d=int(input('Enter the day (eg 10):\n\t'))

# if user_m in winter:
#     season='winter'
#     if user_m=="march" and user_d >=20:
#         season='spring'
# elif user_m in spring:
#     season='spring'
#     if user_m=='june' and user_d>=21:
#         season='summer'
# elif user_m in summer:
#     season='summer'
#     if user_m=='september' and user_d>=22:
#         season='fall'
# elif user_m in fall:
#     season='fall'
#     if user_m=='december' and user_d >=21:
#         season='winter'

# print('the season that corresond with the date is',season)

#Exercise 47
# user_m=input('Enter your birth month:\n\t')
# user_d=int(input('Enter your birth day:\n\t'))

# if (user_m=='December' and user_d>=22 ) or (user_m=='January' and user_d <= 19):
#     horoscope='Capricorn'
# elif (user_m=='January' and user_d>=20) or (user_m=='Feburary' and user_d<=18):
#     horoscope='Aquarius'
# elif (user_m=='Feburary' and user_d>=19) or (user_m=='March' and user_d<=20):
#     horoscope='Aries'
# elif (user_m=='April' and user_d>=20) or (user_m=='May' and user_d<=20):
#     horoscope='Taurus'
# elif (user_m=='May' and user_d>=21) or (user_m=='June' and user_d<=20):
#     horoscope='Gemini'
# elif (user_m=='June' and user_d>=21) or (user_m=='July' and user_d<=22):
#     horoscope='Cancer'
# elif (user_m=='July' and user_d>=23) or (user_m=='August' and user_d<=22):
#     horoscope='Leo'
# elif (user_m=='August' and user_d>=23) or (user_m=='September' and user_d<=22):
#     horoscope='Virgo'
# elif (user_m=='September' and user_d>=23) or (user_m=='October' and user_d<=22):
#     horoscope='Libra'
# elif (user_m=='October' and user_d>=23) or (user_m=='November' and user_d <=21):
#     horoscope='Scorpio'
# elif (user_m=='November' and user_d>=22) or (user_m=='December' and user_d<=21):
#     horoscope='Sagittarius'

# print('Your horoscope is',horoscope)

#Exercise 48
# user_y=int(input('Enter your birth year:\n\t'))

# if user_y%12==0:
#     zodiac='Monkey'
# elif user_y%12==1:
#     zodiac='Rooster'
# elif user_y%12==2:
#     zodiac='Dog'
# elif user_y%12==3:
#     zodiac='Pig'
# elif user_y%12==4:
#     zodiac='Rat'
# elif user_y%12==5:
#     zodiac='Ox'
# elif user_y%12==6:
#     zodiac='Tiger'
# elif user_y%12==7:
#     zodiac='Rabbit'
# elif user_y%12==8:
#     zodiac='Dragon'
# elif user_y%12==9:
#     zodiac='Snake'
# elif user_y%12==10:
#     zodiac='Horse'
# elif user_y%12==11:
#     zodiac='Sheep'

# print('Your zodiac is',zodiac)

#Exercise49

# user_=float(input('What is the magnitude of the the earthquake:\n\t'))

# if user_<2.0:
#     level='Micro'
# elif user_>=2.0 and user_<3.0:
#     level='Very minor'
# elif user_>=3.0 and user_<4.0:
#     level='Minor'
# elif user_>=4.0 and user_<5.0:
#     level='Light'
# elif user_>=5.0 and user_<6.0:
#     level='Moderate'
# elif user_>=6.0 and user_<7.0:
#     level='Srong'
# elif user_>=7.0 and user_<8.0:
#     level='Major'
# elif user_>=8.0 and user_<10.0:
#     level='Great'
# elif user_>=10.0:
#     level='Meteoric'
# else:
#     level=''

# if level=='':
#     print('Incorrect input, check and enter the correct magnitude')
# else:
#     print('The magnitude of',user_,'is consider as',level)

#Exercise 50
# from math import sqrt

# print('Let calculate the number of real root in the quadratic equation\n')
# print('the quadratic equation is like  f(x)=ax2+bx+c\n')
# print('You will provide the a, b, c of the equation\n')
# user_a=float(input('Enter the value of "a":\n'))
# user_b=float(input('Enter the value of "b":\n'))
# user_c=float(input('Enter the value of "c":\n'))
# values=[]
# try:
#     deter=sqrt((user_b**2)-(4*user_a*user_c))
#     if deter == 0.0:
#         root='1'
#         value=((-user_b+deter)/(2*user_a))
#         values.append(value)
#     elif deter>0:
#         root='2'
#         value_a=((-user_b+deter)/(2*user_a))
#         values.append(value_a)
#         value_b=value=((-user_b-deter)/(2*user_a))
#         values.append(value_b)
# except ValueError:
#     root='0'
#     value=''

# if value=='':
#     print('The number of root of the quadratic equation is',root)
# else:
#     print('The number of root of the quadratic equation is',root,'and the value is',str(values))

#Exercise 51
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
#     elif input_=='F':
#         result+=0
#     else:
#         print('Your letter grade is incorrect.')
#         break
    
#     input_c=input('Do you have any othe grade to enter (enter y for Yes or n for n):\n\t')
#     if input_c=='n':
#         break
#     else:
#         continue

# print('your total grade point is',result)

#Exercise 52
# input_=float(input('Enter your gradepoint:\n\t'))

# if input_<0 and input_>=0:
#     result='F'
# elif input_>=1.0 and input_<1.3:
#     result='D'
# elif input_>=1.3 and input_<1.7:
#     result='D+'
# elif input_>=1.7 and input_<2.0:
#     result='C-' 
# elif input_>=2.0 and input_<2.3:
#     result='C'
# elif input_>=2.3 and input_<2.7:
#     result='C+'
# elif input_>=2.7 and input_<3.0:
#     result='B-'
# elif input_>=3.0 and input_<3.3:
#     result='B'
# elif input_>=3.3 and input_<3.7:
#     result='B+'
# elif input_>=3.7 and input_<4.0:
#     result='A-'
# elif input_>=4.0:
#     result='A+'

# print('Your letter grade is',result)

#Exercise 53
# 0.0 Unacceptable performance 0.4 Acceptable performance 0.6 or more Meritorious performance
# input_=float(input('Enter your rating (it should be 0.0,0.4,0.6 or more):\n\t'))

# if input_==0.0:
#     meaning='Unacceptable performance'
# elif input_==0.4:
#     meaning='Acceptable performance'
# elif input_>=0.6:
#     meaning='Meritorious performance'
# else:
#     meaning=''

# if meaning=='':
#     print('Incorrect rating. It must be 0.0, 0.4, 0.6 or more')
# else:
#     raised=input_*2400
#     print('the meaning of your rating is',meaning)
#     print('your raise at the year will be $',raised)

#Exercise 54

# input_=int(input('Enter the wavelength:\n\t'))

# if input_>=380 and input_<450:
#     color='Violet'
# elif input_>=450 and input_<495:
#     color='Blue'
# elif input_>=495 and input_<570:
#     color='Green'
# elif input_>=570 and input_<590:
#     color='Yellow'
# elif input_>=590 and input_<620:
#     color='Orange'
# elif input_>=620 and input_<750:
#     color='Red'
# else:
#     color=''

# if color=='':
#     print('The wavelength is not visible to human eye')
# else:
#     print('The color that is related to wavelength is',color)

#Exercise 55
# print('Let me help you find the name of the electromagnetic wave\n')
# print('You would privide the frequency of the wave in this format')
# print('a x 10^b (An example of frequency is 3 x 10^6, so the a =3 and b=6)\n') 

# input_a=int(input('What is the value of a:\n\t'))
# input_b=int(input('What is the value of b:\n\t'))

# result=input_a*10**input_b

# if result <(3*10**9):
#     wave='Radio wave'
# elif result >= (3*10**9) and result <(3*10**12):
#     wave='Microwaves'
# elif result>=(3*10**12) and result<(4.3*10**14):
#     wave='Infrared light'
# elif result>=(4.3*10**14) and result<(7.5*10**14):
#     wave='Visible Light'
# elif result>=(7.5*10**14) and result<(3*10**17):
#     wave='Xray'
# else:
#     wave='Gamma ray'

# print('The electromagnetic wave associated with wavelength is',wave)

#Exercise 56
# print('To calculate your bill you need to provide\
#     number of minutes and text messages used in a month')
# input_c=int(input('Enter the number of minutes used:\n\t'))
# input_m=int(input('Enter the number of text message used:\n\t'))

# if input_c<=50 and input_m<=50:
#     phone_bill=15.00
#     support=0.44
#     tax=(phone_bill+support)*0.05
#     extra=0
# elif input_c>50 and input_m<=50:
#     extra=(input_c-50)*0.25
#     phone_bill=15.00
#     support=0.44
#     tax=(phone_bill+support+extra)*0.05
# elif input_c<=50 and input_m>50:
#     extra=(input_m-50)*0.15
#     phone_bill=15.00
#     support=0.44
#     tax=(phone_bill+support+extra)*0.05
# else:
#     extra=((input_m-50)*0.15)+((input_c-50)*0.25)
#     phone_bill=15.00
#     support=0.44
#     tax=(phone_bill+support+extra)*0.05

# total=phone_bill+extra+support+tax

# print('Your phone bill for this month is :')
# print('\tphone bill: %.2f'%phone_bill)
# print('\tsupport charges: %.2f'%support)
# print('\textra: %.2f'%extra)
# print('\ttax: %.2f'%tax)
# print('Total: %.2f'%total)

#Exercise 57

# input_year=int(input('Please enter the year:\n\t'))

# if input_year%400==0:
#     leap='Yes'
# elif input_year%100==0:
#     leap='No'
# elif input_year%4==0:
#     leap='Yes'
# else:
#     leap='No'

# if leap=='No':
#     print('OOps, It is not a leap year')
# else:
#     print('Yaayy, It is a leap year')

#Exercise 58
# print('Tell me a date and i will tell you, it successor')
# print('You will provide the day, month and year (all in digits)')
# print('eg. 28/10/2012 the day is 28, the month is 10 and year is 2012')

# d=int(input('Enter the day:\n\t'))
# m=int(input('Enter the month:\n\t'))
# y=int(input('Enter the year:\n\t'))

# if (d<30 and m in [4,6,9,11]) or (d<29 and m==2) or \
#     (d<31 and m in [1,3,5,7,8,10,12]):
#     d+=1
#     m=m
#     y=y
# elif (d ==30 and m in [4,6,9,11]) or (d==29 and m==2) or \
#     (d==31 and m in [1,3,5,7,8,10]):
#     d=1
#     m+=1
#     y=y
# elif (d==31 and m==12):
#     d=1
#     m=1
#     y+=1
# else:
#     d=''

# if d=='':
#     print('The date is not valid')
# else:
#     print(f'The successor date is {d}-{m}-{y}')

#Exercise 59
# print('Let me tell you whether your plate is the old format or not')

# input_=input('Please enter your license plate:\n\t')

# if len(input_)<6 or len(input_)>6:
#     formatt='wrong'
# elif b'input_[0:3].isalpha' and b'input_[-3:].isdigit':
#     formatt='old'
# elif b'input_[0:3].isdigit' and b'input_[-3:].isalpha':
#     formatt='new'
# else:
#     formatt='incorrect'

# if formatt=='wrong':
#     print("Please enter the length of license id you enter is incorect and re-enter")
# elif formatt=='incorrect':
#     print('The format you enter does not exist')
#     print('It can eith start with three alphabet and end with three number')
#     print('Or start with three number and end with three alphabet')
# else:
#     print('The format of your license plate is',formatt)

#Exercise 60
# from random import randrange
# print('Please place your bets!!\n')
# user_bet=randrange(0,38)
# user_bet=37
# if user_bet==37 or user_bet==0:
#     pay=user_bet
#     if user_bet==37:
#         pay='00'
# else:
#     pay=user_bet

# if (user_bet in range(1,10) and user_bet%2==1) or\
#     (user_bet in range(12,19) and user_bet%2==0) or\
#         (user_bet in range(21,28) and user_bet%2==1) or\
#             (user_bet in range(30,37) and user_bet%2==0):
#             color='Red'
# else:
#     color='Black'

# if user_bet%2==0:
#     e_o='Even'
# else:
#     e_o='Odd'

# if user_bet in range(1,19):
#     between='1 to 18'
# else:
#     between='19 to 36'

# if user_bet==37:
#     print('The spin result is 00 ...')
# else:
#     print('The spin result is %d ...'%user_bet)
# if user_bet==37 or user_bet==0:
#     print('Pay',pay)
# else:
#     print('Pay %d'%pay)
#     print('Pay %s'%color)
#     print('Pay %s'%e_o)
#     print('Pay %s'%between)

