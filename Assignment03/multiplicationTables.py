# Write a Python program using nested loops to print the multiplication tables of 1, 2, and 3 from 1 to 10.
table=int(input('Enter the Total Table: '))
for i in range(1,table+1):
    print(f"Tables of {i}") 
    for j in range(1,11):
     print(f"{i} * {j}: {i*j}")
    print() 