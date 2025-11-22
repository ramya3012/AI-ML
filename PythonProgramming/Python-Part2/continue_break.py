#Using break statement in while loop and terminating the loop when i is multiple of 6
'''
i=1

while(i<=10):
    if (i%6==0):
        break
    print(i)
    i+=1

print('Outside loop now')


#Using continue statement in while loop to skip multiples of 3

i=1

while(i<=10):
    if(i%3==0):
      i+=1
      continue
    print(i)
    i+=1

print('Outside loop now')



#Print all odd numbers from 1 to 10

i=1

while (i<=10):
    if(i%2 ==0):
        i+=1
        continue
    print(i)
    i+=1


#Instead of putting i+=1 in both if and else block, we can put it once after if block

i=0

while (i<10):
    i+=1
    if(i%2==0):
        continue
    print(i)


#Print all odd numbers from 1 to 10 without using continue statement
i=1
  
while (i<=10):
    print(i)
    i+=2
'''

