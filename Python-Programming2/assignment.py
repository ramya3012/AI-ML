#Write a program that takes a salary as input. Using conditional statements, calculate the tax based on these rules: If salary < 30,000 → 5%, If salary is 30,000–70,000 → 15%, If salary > 70,000 → 25%

salary =int(input('Enter salary'))


if (salary<30000):
    tax= salary * 0.05
elif (salary>=30000 and salary<70000):
    tax=salary *0.15
else:
     tax=salary*0.25
     
print("Final tax rate", tax)


#Write a function that takes two integers and prints all even numbers between them (inclusive

def sum(a,b):
    for i in range(a,b+1):
        if(i%2==0):
            print(i)
     
sum(1,10)


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
   
      
print_digits(312)




