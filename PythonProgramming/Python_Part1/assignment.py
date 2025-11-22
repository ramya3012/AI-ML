'''
# 1.Write a program that asks the user for their name and age,then prints a sentence like:
   #Hello Shradha, you are 21 years old!

name=input("Enter your name:")
age=int(input('Enter your age:'))

print("Hello",name, "you are",age,"years old!")

# 2. Take two numbers as input from the user and print their sum,difference,product,and quotient

a= int(input('Enter first number:'))
b= int(input('Enter second number:'))

sum = a + b
difference = a - b
product = a * b
quotient= a/b

print("sum of 2 numbers:" , sum)
print("difference of 2 numbers:" , difference)
print("product of 2 numbers:" , product)
print("quotient of 2 numbers:" , quotient)



#3.Ask the user to enter two integers and one float. Convert them all to floats and print their average.

num1=float(input("Enter num1:"))
num2=float(input("Enter num2:"))
num3=float(input("Enter num3:"))

Average=((num1+num2+num3)/3)
print("Average of numbers:", Average)

#4.The user enters a string containing a number(e.g.,).
# Convert it to:"45"•an integer •a float •a string again.  Print all three values with their types

number =input('Enter a number:')
int_val=int(number)
float_val=float(number)
str_val=str(number)
print("Int conversion",int_val,type(int_val))
print("Float conversion",float_val,type(float_val))
print("String conversion",str_val,type(str_val))



# 5.Evaluate and print the result of the following expression:                         
# x =10+3*2**2 .Based on what you learnt in the lecture explain why the output is what it is.

x =10+3*2**2 
print(x)

#bcoz as per lecture exponent has highest priority so it will be evaluated first
  #10+3*4 =10+12=22

#6.Write a program to swap values of two numbers entered by the user

a=input("Enter number a:")
b=input("Enter number b:")

print("Numbers before swapping a and b ", "a:",a ,"b:",b)
temp=a
a=b
b=temp
print("Numbers after swapping 2 numbers","a:",a ,"b:",b)

#7.Ask the user for a temperature in Celsius(stringinput).
# Convert it to float,then calculate and print temperature in Fahrenheit.
# Conversionformula:FahrenheitTemp=(CelsiusTemp∗(9/5))+32

celsius_temperature= float(input("Enter the temperature in Celsius"))
 
fahrenheit_temp=(celsius_temperature*(9/5))+32
print('Fahrenheit temp' ,fahrenheit_temp)



#8.Take the radius(r) as user input and print the area. 
# Use the formula:π*r2 (value of π=3.14)
 
r= float(input("Enter the radius:"))
Area=3.14*(r**2)
print("Area of circle",Area)

#9.Ask the user for: Principal(P),Rate(R),Time(T). 
# Convert all to float and compute simple interest.SI=(P∗R∗T)/100.

P= float(input("Enter Principal:"))
R= float(input('Enter Rate of Interest:'))
T=float(input('Enter Time:'))

SI =(P * R * T)/100
print('Simple Interest:',SI)

'''
#10.Take a decimal number as input(like 45.78)and output its:
# integer part-45
# •fractional part-.78

number=float(input("Enter number"))
integer_part=int(number)
fractional_part= (number) % 1 

print("integer_part",integer_part)
print("fractional_part",fractional_part)
