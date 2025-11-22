'''
count =1 
while (count<=5):
    print('Hello, World!',count)
    # print('Count is:', count)
    count +=1

print('After loop ended',count)


i=5
while (i>=1):
    print(i)
    i-=1
    
    
n=int(input('Enter any number'))
i=1

while (i<=10):
    print("The product of n* i is", n*i)
    i+=1
    
    
#Print all odd numbers from 1 to 10

i=1

while (i<=10):
    if(i%2 ==0):
        i+=1
        continue
    
    print(i)
    i+=1

'''







# def avg(a,b,c):
#     average=(a+b+c)/3
#     return average
    
# print(avg(1,2,3))

'''
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact = fact * i
    return fact
    
    
print(fact(6))
        
'''
'''

salary =int(input('Enter salary'))


if (salary<30000):
    tax= salary * 0.05
elif (salary>=30000 and salary<70000):
    tax=salary *0.15
else:
     tax=salary*0.25
     
print("Final tax rate", tax)



def sum(a,b):
    for i in range(a,b+1):
        if(i%2==0):
 return i
     
print(sum(1,10))
            
'''

