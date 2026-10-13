#Write a Python program that takes a number as input and prints its multiplication table from 1 to 10 using a loop.
number=int(input("Enter the Number: "))
for i in range(1,11):
    print(f"{number} * {i}: {number*i}")