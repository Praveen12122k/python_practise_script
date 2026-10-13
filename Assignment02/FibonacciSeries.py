#Write a program that prints the Fibonacci series up to n terms using a loop.
number=int(input("Enter the Number: "))
a=0
b=1
for i in range(number):
    next=a+b
    print(a)
    a=b
    b=next