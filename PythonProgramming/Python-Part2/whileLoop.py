''''
count =1 
while (count<=5):
    print('Hello, World!',count)
    # print('Count is:', count)
    count +=1

print('After loop ended',count)




#Print 1 to 5

i=1 
while (i<=5):
    print("the value of i:",i)
    i+=1


#Print 5 to 1 (Print 1 to 5 in reverse order)
i=5
while (i>=1):
    print(i)
    i-=1

#Print multiplication table of a number entered by user
n=int(input('Enter any number:'))
i=1

while (i<=10):
    print("The product of n* i is", n*i)
    i+=1

'''
#Print multiplication table of a number entered by user if i starts from 0
n=int(input('Enter any number:'))
i=0

while (i<10):
    print("The product of n* i is", n*(i+1))
    i+=1