# Write a Python program that prints numbers from 1 to 20. Stop printing when the number 13 is reached using the break statement.
number=int(input("Enter the Number: "))
for i in range(21):
 if(i==number):
  break
 print(i)