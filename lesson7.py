# Задание 1

string=input(("Enter a word:"))

if(string==string[::-1]):
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")

print()

#Задание 2

string=input(("Enter any text (up to 1000 characters):"))

print(' '.join(string.split()))
