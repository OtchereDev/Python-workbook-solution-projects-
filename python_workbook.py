"""
This is the first chapter of The Python Workbook 
the solution to the exercise
'Introduction to python'
"""
#Exercise 2
# user_input=input("Please enter your name: \n\t")

# print("Good morning ",user_input)
# print("You are welcome to weMuve transportation, ",user_input)

#Exercise 3
# user_width=float(input("Please enter the width of the room (in meters):\n\t"))
# user_length=float(input("Please enter the length of the room (in meters):\n\t"))

# def area_calc():
#     length=user_length
#     width=user_width
#     area=length*width
#     print("The area of the room is ",area," meters")

# area_calc()

#Exercise 4
# user_width=float(input("Please enter the width of the farm (in feets):\n\t"))
# user_length=float(input("Please enter the length of the farm (in feets):\n\t"))

# def arae_in_acres():
#     area=user_width*user_length
#     acres=area/43560
#     print("The total acres of the farm is ",acres,"acres")

# arae_in_acres()

#Exercise 5
# is_1l=float(input("How many bottle hold 1 litre or less:\n\t"))
# is_above1l=float(input("How many bottle hold more than 1 litre:\n\t"))

# def discounting():
#     small_b=is_1l*0.10
#     big_b= is_above1l*0.25
#     refund=small_b+big_b
#     print(f"You have a refund of ${refund}. Thankyou")

# discounting()

#Exercise 6
# price=int(input("please enter the price of the food:\n\t"))

# tax=0.06*price
# tip_=0.18*price

# grand_price=price+tax+tip_

# print(f"The total cost is ${price}+${tax}+${tip_} = {grand_price}")

#Exercise 7
# print("Welcome math buddy")
# n=int(input("Enter the number for the positive sum calculation:\n\t"))

# sum=n*(n-1)/2

# print("The sum of the ",n," positive number is ", sum)

#Exercise 8
# widgets_w=75
# gizmos_w=112

# widget_n=int(input('Please enter the number of widgets in the order:\n\t'))
# gizmos_n=int(input("Please enter the number of gizmos in the order:\n\t"))

# total_w=(widget_n*widgets_w)+(gizmos_w* gizmos_n)

# print("The total weight of your order is",total_w," grams")

#Exercise 9
# interest= 0.04

# principal=int(input("Please enter the amount in your account:\n\t"))

# first_year=principal+(principal*interest)
# second_year=first_year+(first_year*interest)
# third_year= second_year+(second_year*interest)

# total_interest=third_year-principal

# print("Your principal at the end of the first year is ", first_year)
# print("Your principal at the end of the second year is ", second_year)
# print("Your principal at the end of the third year is ", third_year)
# print("Your total interest at the end of the third year is ",total_interest)

#Exercise 10
import math

# a=int(input("Please enter the first number:\n\t"))
# b=int(input("Please enter the second number\n\t"))

# print("the sum of a and b is ", a+b)
# print("the difference of a and b is ", a-b)
# print("the quotient of a and b is ",a/b)
# print("the reminder of a divide by b is ",a%b)
# print("the log10 of a is ",math.log10(a))
# print("the a raise the power b", a**b)

#Exercise 11
# conversion=235.215

# input_=int(input("please enter the fuel efficency you want to convert? (in Mile per gallon)\n\t"))

# n=conversion*input_

# print("The fuel efficiency in liters-per-hundred kilometers (L/100km) is %.2f L/100km" % n)

#Exercise 12
# print("Please provide all the input in degrees\n\n")
# t1=math.radians(int((input("Please enter the latitude of the first point:\n\t"))))
# g1=math.radians(int(input("Please enter the longitude of the first point:\n\t")))
# t2=math.radians(int(input("Please enter the latitude of the second point:\n\t")))
# g2=math.radians(int(input("Please enter the longitude of the second point:\n\t")))

# distance=6371.01*math.acos(math.sin(t1)*math.sin(t2)\
#     +math.cos(t1)*math.cos(t2)*math.cos(g1-g2))

# print(distance)

#Exercise 13
# cent_per_tonnie=200
# cent_per_lonnie=100
# cent_per_quarter=25
# cent_per_dime=10
# cent_per_nickel=5

# cents=int(input("Please enter the number of cents:\n\t"))

# print(f"{cents // cent_per_tonnie} tonnies will be given")

# cents=cents % cent_per_tonnie

# print(f"{cents//cent_per_lonnie} lonnies will be given")

# cents=cents%cent_per_lonnie

# print(f"{cents//cent_per_quarter} quarters will be given")

# cents=cents%cent_per_quarter

# print(f"{cents//cent_per_dime} dime will be given")

# cents=cents%cent_per_dime

# print(f"{cents//cent_per_nickel} nickel will be given")

#Exercise 14
# one_foot=12
# one_inch=2.54

# input_foot=float(input("please enter your height in the foots:\n\t"))
# input_inch=float(input("please enter your height in inches:\n\t"))

# conv_=(input_foot*one_foot+input_inch)*one_inch
# print("Your height in centimeters:\t",conv_)

#Exercise 15
# input_=float(input("Please enter the measurement in foot:\n\t"))

# inches= input_*12
# yards=input_*0.333333
# miles=input_*0.000189394

# print("the measurement in inches is %d inches" %inches)
# print("the measurement in yards is %d yards" %yards)
# print("the measurement in miles is %.10f miles" %miles)

#Exercise 16
# print("Hello maths buddy")
# print("let me help you compute the area of the circle \
#     and the volume of a sphere")
# input_=float(input("please enter the radius:\n\t"))

# area=math.pi*(input_**2)
# volume=4/3*(math.pi*(input_**3))

# print("The area of the circle is %.3f" %area)
# print("The volume of the sphere is %.3f" %volume)

#Exercise 17
# j_to_k=2.777e-7
# water_capacity=4.186
# input_=float(input("Please enter the mass of the water:\n\t"))
# temp=int(input("Please enter the change in temperature:\n\t"))

# q=input_*water_capacity*temp

# price=(q*j_to_k)*8.9

# print("the amount of energy is %d joules" %q)
# print("It will cost %.5f cents" %price)

#Exercise 18
# print("Hello Math buddy \n")
# print("Let compile the volume by providing me with the radius and height")
# r=float(input("What is the radius:\n\t"))
# h=float(input("What is the height:\n\t"))

# area=math.pi*r
# volume=area*h

# print("The volume of the structure is %.2f cm^3" %volume)

#Exercise 19
# a=9.8
# vi =0

# print("Let me help you compute the final speed\n")
# print("You will provide the height at which"+\
# "the substance is falling from\n")
# d=float(input("What is the height\n\t"))

# calc=vi+(2*a*d)

# vf=math.sqrt(calc)

# print("The final speed of the substance is %.2f m/s" %vf)

#Exercise 20
# R=8.314

# pressure=int(input('Please proveide the pressure of the gas:\n\t'))
# volume=int(input("Please provide the volume of the gas:\n\t"))
# temp_=int(input("Please provide the temperature in degree Celsius:\n\t"))

# temp_k=temp_+273.15
# a=pressure*volume
# b=temp_k*R

# n_amount=a/b

# print("The amount of gas in moles is %.6f moles" %n_amount)

#Exercise 21
# print("Let do some maths!!\n")
# print("let calculate the area of a triangle\n")
# print("You woud provide me with the height and the width\n")

# a=int(input("what is the width of the triangle:\n\t"))
# b=int(input("What is the height of the triangle:\n\t"))

# area=0.5*a*b

# print(f"the volume of the triangle is {area}")

#Exercise 22
# print("Let calculate the area of the triangle")
# print("this program require all the side of the triangle is known")

# s1=int(input("what is the first side of the triangle:\n\t"))

# s2=int(input("what is the second side of the triangle:\n\t"))

# s3=int(input("what is the third side of the triangle:\n\t"))

# s=(s1+s2+s3)/2

# area_i=s*(s-s1)*(s-s2)*(s-s3)

# area_f=math.sqrt(area_i)

# print("The area of the triangle is %.2f" %area_f)

#Exercise 23
# print("Let calculate the area of all polygons\n")
# print("you would provide me with the length of the"+\
# " side and the number of the side of the polygon\n")

# n=int(input("What is the length of the sides:\n\t"))
# s=int(input("What is the number of side of the polygon:\n\t"))

# formula_a= n*(s**2)
# formula_b= 4*(math.tan(math.pi/n))

# formula=formula_a/formula_b

# print("The area of the polygon is %.5f" %formula)

#Exercise 24
# print("Let calculate the duration to second\n")
# print("you would provide the number of days, hours,minute and second")

# d=int(input("Enter the number of days\n\t"))
# h=int(input("Enter the number of hours:\n\t"))
# m=int(input("Enter the number of minutes:\n\t"))
# s=int(input("Enter the number of seconds:\n\t"))

# day=d*86400
# hour=h*3600
# minute=m*60

# total=day+hour+minute+s

# print(f"The total duration in seconds is {total} s")

#Exercise 25
# print("Provide me with the seconds and i will provide the day format\n")

# n=int(input("What is the number of seconds:\n\t"))

# day=n//8600
# n=n%8600

# hour=n//3600
# n=n%3600

# minute=n//60
# n=n%60

# print(f"The date format is {day} days {hour} hours {minute} minutes {n} second")

#Exercise 26
# from time import asctime

# time=asctime()

# print("Time says %s" %time)

#Exercise 27
# print("Let calculate your body mass index (BMI)\n")
# print("You will provide your weight and height")

# weight_=int(input("what is your weight (in pounds):\n\t"))
# height_=int(input("what is your height (in inches):\n\t"))

# bmi=(weight_/height_**2)*703

# print('Your BMI is %d' %bmi)

#Exercise 28

# Temp_air=int(input('Enter the air temperature (in degree Celsius):\n\t'))
# wind_speed=int(input('Enter the wind speed (inkilometers per hour):\n\t'))

# Wind_chill_index =13.12+(0.6215*Temp_air)-(11.37*(wind_speed**0.16)) \
#     +(0.3965*Temp_air*(wind_speed**0.16))  

# print("the wind chill index is %d"%Wind_chill_index)

#Exercise 29
# print('Let convert the temperature to degree Fahrenheit and degree Kelvin\n')
# n=int(input('Enter the temperature (in degree Celsius):\n\t'))

# degree_k= n+273.15
# degree_f = (n * 1.8)+32

# print("The equivalent of the temperature in degree Kelvin is %.3f K"%degree_k)
# print('The equivalent of the temperature in degree Fahrenhiet is %.3f F'%degree_f)

#Exercise 30
# psi=0.145
# mom=7.50062
# pressure=int(input("What is the pressure (in kilopascal):\n\t"))
# pressure_mom=pressure*mom
# pressure_psi= pressure*psi

# print("The pressure in  pounds per square inch is ",pressure_psi,"\n")
# print("The pressure in millimeters of mercury is ", pressure_mom)

#Exercise 31
# n=input("Enter any 4 number and i will find the sum of it:\n\t")

# n_1=int(n[0])
# n_2=int(n[1])
# n_3=int(n[2])
# n_4=int(n[3])

# total= n_1+ n_2+ n_3+ n_4

# print("the sum total is %d" %total)

#Exercise 32
# print('You will provide me with three integer to sort\n')

# n_1=int(input('What is the first integer:\n\t'))
# n_2=int(input('What is second integer:\n\t'))
# n_3=int(input('What is the third integer:\n\t'))

# max_=max(n_1,n_2,n_3)
# min_=min(n_1,n_2,n_3)
# mid_=n_1+n_2+n_3-max_-min_

# print(f'the max number is {max_}, the min number is {min_}, the middle number is {mid_}')

#Exercise 33
# bread=3.49
# day_old= bread-(bread*0.6)

# input_=int(input("Enter the number of day old bread that where sold:\n\t"))

# total_old=input_*day_old

# total_bread=input_*bread

# total_discount= total_bread - total_old

# print("The total cost of all sold day old bread is $%5.2f"% total_old)
# print("The total cost if they were sold on the same day is $%5.2f"%total_bread)
# print("The total discount is %5.2f"%total_discount)
