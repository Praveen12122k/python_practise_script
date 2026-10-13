#Write a Python program that takes a positive integer N from the user and calculates the sum of the first N natural numbers using a loop.
number=int(input("Enter the Number: ")) 
sum=0
for i in range(1,number+1):
    sum=sum+i
print(f"Sum of Number: {sum}")
