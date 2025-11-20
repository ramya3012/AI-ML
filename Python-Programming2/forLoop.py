#forLoop

string='hello'

for var in string:
    print(var)


#Check if 'o' exists in the string 'hello'
if  'o' in string:
    print('o exists in string')


#Print 0 to 4 : range(5) generates numbers from 0 to 4

for i in range(5):
    print(i)

#Print 1 to 5 : range(5) generates numbers from 0 to 4 - just increment by 1

for i in range(5):
    print(i+1)


#Count the number of i's in the word 'artificial intelligence'
word ='artificial intelligence'

count =0

for char in word:
    if(char=='i'):
        count+=1
print('The count of i in the word is:',count)



word='artificial intelligence is our future'

count =0

for char in word:
    if(char =='a'or char=='e' or char=='i' or char=='o' or char=='u'):
        count+=1

print('The number of vowels in the sentence is:',count)