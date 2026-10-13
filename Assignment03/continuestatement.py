#Write a Python program to print numbers from 1 to 20, but skip all numbers that are divisible by 3 using the continue statement.
for i in range(21):
    if(i%3==0):
        continue
    print(i)