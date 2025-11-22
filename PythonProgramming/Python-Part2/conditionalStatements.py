'''
age=int(input('Enter age:'))

if age>=18:
    print('You are eligible to vote')
else:
    print('You cant vote')


#elif

color=input('Enter color:')

if color=='red':
   print('Stop')
elif color=='green':
    print('Go')
elif color=='yellow':
    print('look')
else:
    print('Wrong color for traffic lights')




#Practice Questions

age=int(input('Enter age:'))

if (age<13):
    print('Child')
elif (age >=13 and age<18): #13-18
    print('teenager')
else:
    print('adult')


#Login
username=input('Enter your username:')
password=input('Enter your password:')

if (username=='admin' and password=='pass'):
    print('LOGIN successful!')
elif (username!='admin'):
    print('Invalid username')
else:
    print('Invalid password')


#Multiple of 5
number=int(input('Enter number:'))

if (number % 5==0):
    print('Multiple of 5')
else:
    print('Not multiple of 5')


#Odd or Even

number=int(input('Enter the number:'))

if(number % 2 == 0):
  print('Number is even')
else:
    print('Number is odd')

    '''


#Nesting

username=input('Enter username:')
password=input('Enter password:')

if (username=='admin' and password=='pass'):
    print('LOGIN successful!')
else:
    if(username!='admin'):
        print('Invalid username')
    else:
        print('Invalid password')

  