#Write a program that prints the multiplication table of a given number up to 10.
number=int(input('Enter the Number: '))
if number>0:
   for i in range(1,11):
    print(f'{number}*{i}= {i*number}')
else:
  print('Number is Invalid')