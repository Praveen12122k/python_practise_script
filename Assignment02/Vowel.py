#Write a program to check whether a character entered by the user is a vowel or consonant.
char=input('Enter the Character: ').lower()
if len(char)==1 and char.isalpha():
    if char in ["a", "e", "i", "o", "u"]:
        print(f"{char} is Vowel")
    else: 
         print(f"{char} is Consonant")    
else: 
    print("Enter Only the Character")