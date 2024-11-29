n = int(input("Enter the number:"))
a = 0
b = 1
print("The Fibonacci Series is:")
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c
