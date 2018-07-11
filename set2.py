a=int(input("Enter number:"))
b=a
d=0
while(a>0):
    c=a%10
    d=d*10+c
    a=a//10
if(b==d):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
