ans=5+10.0
print(type(ans)) #<class 'float'>

a=10
b=5

print(a/5)
#2.0
print(type(a/5))
#<class 'float'>


ans1=int(5+10.0) #casting
print("Casting",ans1,type(ans1))

ans2=5+10.0 #Auto conversion
print("Auto Conversion",ans2,type(ans2))


val=int("123")
print(type(val))

val=bool(10)

print('Bool for positive numbers',val,type(val))

val=bool(-10)

print('Bool for negative numbers',val,type(val))

val=bool(0)

print('Bool for 0',val,type(val))