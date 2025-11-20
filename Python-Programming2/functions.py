def hello(): #function definition
    print("Hello, World!")

hello() #function call


#sum of two numbers

def sum_two_numbers(a,b): #function definition with parameters
    sum = a + b
    return sum  #returning the sum

result=sum_two_numbers(5,10) #function call with arguments
print("The sum is:",result)

print("The sum of 20 and 30:",sum_two_numbers(20,30)) #function call inside print statement


#Average of three numbers

def avg(a,b,c):
    sum=a+b+c
    return sum/3
    
print(avg(1,2,3))


#default values and non-default values in function parameters

def sum(a,b=1):
    return a+b

print(sum(5))  #b takes default value 1
print(sum(5,10))  #b takes value 10 passed during function call


#lambda function 

sum=lambda a,b:a+b
print("The sum using lambda function is:",sum(10,20))


#factorial of a number using function

def calc_factorial(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
    return fact

num=int(input('Enter a number to find factorial:'))
print('The factorial of',num,'is:',calc_factorial(num))