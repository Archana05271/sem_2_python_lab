my_dict = {}
n= int(input("Enter the elements:"))
for i in range(n):
    key = input(f"Enter key : ")
    value = int(input(f"Enter value : "))
    my_dict[key] = value
total = sum(my_dict.values())
print(my_dict)
print(total)
