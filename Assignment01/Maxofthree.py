number_one=int(input('Enter First Number: '))
number_two=int(input('Enter Second Number: '))
number_three=int(input('Enter Third Number: '))

largest=number_one;
if number_two > largest:
   largest = number_two;
if number_three > largest:
  largest = number_three;
print(f'Largest Number is {largest}')     