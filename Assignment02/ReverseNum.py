#Write a Python program to reverse the digits of a number using a loop.
number=int(input("Enter the Number: "))
reverse=0
while number>0:
  reverse=reverse*10+number%10
  number=number//10
print(reverse)  