#Write a Python program to print the following pattern using nested loops.
count=int(input('Enter the Start Pattern Count: '))

for i in range(count):
    for j in range(i+1):
        print("*",end=" ")
    print()  
   
       