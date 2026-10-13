#Write a program that takes a person’s age and classifies them into:
age=int(input("Enter the Age: "))
if age>0 and age<13:
    print("Child")
elif age>=13 and age<=19:
    print("Teenager")
elif age>=20 and age<=59:
    print("Adult")
elif age>=60:
    print("Senior")
else:
    print("Age is in Negative")