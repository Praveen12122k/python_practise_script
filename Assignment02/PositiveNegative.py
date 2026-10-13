#Write a Python program that checks whether a given number is positive, negative, or zero.
number=int(input("Enter the Number: "))
if number>0:
    print(f"{number} is Postive")
elif number<0:
    print(f'{number} is Negative')
else:
    print(f'Zero')