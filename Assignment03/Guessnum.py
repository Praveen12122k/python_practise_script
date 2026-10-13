"""Write a Python program where the secret number is 7. Continuously ask the user to guess the number using a loop.
If the user enters the correct number, print "Congratulations! You guessed it correctly." and stop the loop using break.
If the user enters a negative number, print "Negative numbers are not allowed. Try again." and skip the remaining statements in that iteration using continue.
Otherwise, print "Wrong guess. Try again."""
flag=True
while flag:
 Guess_number=int(input("Guess the number: "))
 if Guess_number==7:
        print('Congratulations! You guessed it correctly.')
        break
 elif Guess_number!=7 and Guess_number>0:
        print('Wrong guess. Try again.')  
        continue
 elif Guess_number<=0:
        print('Negative numbers are not allowed. Try again.')  
        continue