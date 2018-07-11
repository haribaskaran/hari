
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")a=int(input("Enter number:"))
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
