#Write a program that takes a salary as input. Using conditional statements, calculate the tax based on these rules: If salary < 30,000 → 5%, If salary is 30,000–70,000 → 15%, If salary > 70,000 → 25%

# salary =int(input('Enter salary'))


# if (salary<30000):
#     tax= salary * 0.05
# elif (salary>=30000 and salary<70000):
#     tax=salary *0.15
# else:
#      tax=salary*0.25
     
# print("Final tax rate", tax)

''''
#Write a function that takes two integers and prints all even numbers between them (inclusive

def sum(a,b):
    for i in range(a,b+1):
        if(i%2==0):
            print(i)
     
# sum(1,10)


# return exits the function immediately - so it would only print/return the first even number (2) and stop the loop.


# Since you want to print all even numbers, don't use return at all. Just use print(i) inside the loop, and it will print each even number as it finds them (2, 4, 6, 8, 10).

# return is only used when you want to send a value back to the caller and exit the function. In your case, you want the loop to continue through all numbers.



# Q3: Write a function that prints the digits of a number n
# For eg: n = 312, there are 3 digits in it: 3, 1 and 2 & we need to print them

def print_digits(n):
    while n > 0:
        digit = n % 10  # Get the rightmost digit
        print(digit)
        n = n // 10     # Remove the rightmost digit using integer division
   
      
# print_digits(312)


#Print digits in ascending order using recursion n=312 → output: 3 1 2

def print_ascending_digits(n):
    if n==0:
       return 
    digit=n%10
    n=n//10
    print_ascending_digits(n) #recursive call
    print(digit)

# print_ascending_digits(312)





# How it works:
# This function uses recursion to print digits in order (3, 1, 2). The key is that print(digit) happens after the recursive call.

# Step-by-step execution for print_ascending_digits(312):
# Call 1: print_ascending_digits(312)
# n = 312
# n == 0? No, so continue
# digit = 312 % 10 = 2 (extract rightmost digit)
# n = 312 // 10 = 31 (remove rightmost digit)
# Recursive call: print_ascending_digits(31) ← goes here first
# print(2) ← waits to execute
# Call 2: print_ascending_digits(31)
# n = 31
# n == 0? No, so continue
# digit = 31 % 10 = 1
# n = 31 // 10 = 3
# Recursive call: print_ascending_digits(3) ← goes here first
# print(1) ← waits to execute
# Call 3: print_ascending_digits(3)
# n = 3
# n == 0? No, so continue
# digit = 3 % 10 = 3
# n = 3 // 10 = 0
# Recursive call: print_ascending_digits(0) ← goes here first
# print(3) ← waits to execute
# Call 4: print_ascending_digits(0)
# n = 0
# n == 0? Yes!
# return ← stops and goes back
# Now the function "unwinds" (executes the waiting print statements):
# Returns from Call 4 → back to Call 3 → prints 3 ✓
# Returns from Call 3 → back to Call 2 → prints 1 ✓
# Returns from Call 2 → back to Call 1 → prints 2 ✓
# Output:
# Why it works:
# The recursion goes deep first (extracting digits from right to left: 2→1→3)
# The print statements execute on the way back (unwinding: 3→1→2)
# This reverses the order, giving us left-to-right digits!




# Write a function to return the  number of digits in a number,.


def count_numbers(n):
    count=0
    while n!=0:
        n=n//10
        count+=1
    return count
  
# number = int(input('Enter number'))
  
# print(count_numbers(number))  # Print the returned value


# initial state:
# n = 312
# count = 0
# Loop iteration 1:
# n != 0? Yes (312 ≠ 0), so enter loop
# n = n // 10 → n = 312 // 10 = 31 (removes rightmost digit: 2)
# count += 1 → count = 1 (found 1 digit)
# Loop iteration 2:
# n != 0? Yes (31 ≠ 0), so continue loop
# n = n // 10 → n = 31 // 10 = 3 (removes rightmost digit: 1)
# count += 1 → count = 2 (found 2 digits)
# Loop iteration 3:
# n != 0? Yes (3 ≠ 0), so continue loop
# n = n // 10 → n = 3 // 10 = 0 (removes rightmost digit: 3)
# count += 1 → count = 3 (found 3 digits)
# Loop exits:
# n != 0? No (0 = 0), so exit loop



#Write a function to return the sum of digits of a number n


def sum_of_digits(n):
    sum=0
    while n!=0:
        digit=n%10
        sum+=digit
        n=n//10
    return sum

# number =int(input('Enter number'))
# print(sum_of_digits(number))



#Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)


#Design a program to continuously input a number from user & print if it is positive or negative until the user enters "Quit"

while True:
    user_input = input("Enter a number (or 'Quit' to exit): ")
    
    if user_input == "Quit":
        print("Exiting program...")
        break
    
    number = int(user_input)
    
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")
 

#Letʼs createa Simple calculator that performs arithmetic operations. 
# Create a function that performs addition, subtraction, multiplication, or division based on the parameter. Q8 Calculator calculator(a, b, operation) operation [parameter can have values ,, &. operation ‘+’ ‘-’ '*' ‘/’

def calculator(a,b,operation):
    if(operation=='+'):
        result=a+b
    elif(operation=='-'):
        result=a-b
    elif(operation=='*'):
        result=a*b
    else:
        result=a/b
    return result
    
print(calculator(1,3,'/'))


# Alternative using match-case (Python 3.10+)

def calculator(a, b, operation):
    match operation:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b
        
print(calculator(10, 2, '*'))
'''

#Write a function that returns if n is a prime number and  otherwise,using a loop. 
# is_prime(n)TruenFalse
# [-Hint
# 1.We only check prime for 2 or numbers greater than 2. 2 is the smallest prime number.
# 2.A number,will always get divided by atleast one number in range[2,n-1]
# Eg: -For number 9 weʼll check in range(2,8) & itʼll get divided by 3. 
# So 9 is non-prime & weʼll return false for it. 9 For number 7 weʼll check in range(2,6) & it wonʼt get divided by any. So is prime & weʼll return true for it.




def isPrime(n):
    for i in range(2,n-1):
        if n%i==0:
         return False
    return True

print(isPrime(9))



#Letʼs create a Number Guessing Game. Given a secret number (already decided by you), write a program that asks the user to guess it and prints:
# • if the guess is above the number "Too high"
# • if the guess is below "Too low"
# • if the guess matches "Correct!"

# Version 1: Single guess
secret_number = 42
input_number = int(input("Enter number so that we can compare with secret number: "))

if input_number > secret_number:
    print('Too high')
elif input_number < secret_number:
    print('Too low')
else:
    print('Correct!')


# Version 2: Multiple guesses (better game)
# secret_number = 42
# while True:
#     input_number = int(input("Guess the number: "))
    
#     if input_number > secret_number:
#         print('Too high')
#     elif input_number < secret_number:
#         print('Too low')
#     else:
#         print('Correct!')
#         break  # Exit when guessed correctly

