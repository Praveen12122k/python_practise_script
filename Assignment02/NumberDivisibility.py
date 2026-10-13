#Write a program to check if a number is divisible by both 3 and 5.
number=int(input('Enter the Number: '))
if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is divisible by both 3 and 5.")
else:
    print(f"{number} is not divisible by both 3 and 5.")