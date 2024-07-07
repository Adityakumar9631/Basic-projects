print("Welcome to the tip calculator")
print("What was total bill? ")
n=int(input())
print("How much percent tip would you like to give?")
a=int(input())
k=(n*a)/100
b=k+n
print("How many people to split the Bill?")
c=int(input())
d=b/c
print("Each person should pay",d)
