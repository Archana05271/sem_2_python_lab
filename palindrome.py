def palindrome(string):
    rev=string[::-1]
    print("Reversed String is:",rev)
    if string==rev:
        return True
    else:
        return False
string=input("Enter String:")
if palindrome(string):
    print("The String is a palindrome.")
else:
    print("The String is not a palindrome.")
