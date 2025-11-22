for i in range(5):
    print(i)  #0,1,2,3,4

for i in range(1,6):
    print(i)  #1,2,3,4,5

for i in range(1,10,2):
    print(i)  #1,3,5,7,9

for i in range(2,10,2):
    print(i)  #2,4,6,8:



# Sum of n natural numbers

sum =0

for i in range(1,6):
    sum +=i

print('The sum is:',sum)  #15 (1+2+3+4+5)


# Print sum of n natural numbers entered by user

n=int(input('Enter a number:'))
sum=0

for i in range(1,n+1):
    sum +=i
print('The sum is:',sum)


