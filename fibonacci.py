n = int(input("Enter the number:"))
a = 0
b = 1
next_no = b  
count = 1

while count <= n:
    print(next_no, end=" ")
    count += 1
    a, b = b, next_no
    next_no = a + b
print()
