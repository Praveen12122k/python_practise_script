#Write a Python program that calculates the sum of the first n natural numbers using a loop.
number=int(input('Enter the Number: '))
total=0
if number>0:
    for i in range(number+1):
       total=total+i
    print(total)   
else:
    print("Number is Zero")