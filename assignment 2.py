#task 1
a=int(input("enter a number:"))
if a%2==0:
    print(a,"the number is even")
else:
    print(a,"the number is odd")
#task 2
sum=0
for i in range(1,51,1):
    sum+=i
print("the sum of numbers from 1 to 50 is:", sum)