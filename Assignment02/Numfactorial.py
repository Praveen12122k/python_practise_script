#Write a program that calculates the factorial of a number using a loop.
number=int(input("Enter the Number: "))
fact=1
if number>0:
  for i in range(1,number+1):
     fact=fact*i
  print(f"Factorial of {number} is {fact}")
else:
   print("Entered Number is Invalid")