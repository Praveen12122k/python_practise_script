#Write a Python program to count the number of digits in a given integer using a loop.
number=int(input("Enter the Number: "))
count=0
while number>0:
  number=number//10
  count=count+1
print(count)  