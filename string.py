def count_letter(string):
    upper_count=0
    lower_count=0
    for char in string:
        if char.isupper():
            upper_count+=1
        elif char.islower():
            lower_count+=1
    print("No of upper case:",upper_count)
    print("No of lower case:",lower_count)
string=input("Enter  string:")
count_letter(string)
