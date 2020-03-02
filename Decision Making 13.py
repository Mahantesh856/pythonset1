print("enter the number user")
n1 = int(input("Enter the number 1:"))
n2 = int(input("Enter the number 2:"))
n3 = int(input("Enter the number 3:"))
n4 = int(input("Enter the number 4:"))
max =0

if((n1>n2) and (n3>n4)):
    if(n1>n3):
        max =n1
    else:
        max = n3
if((n2>n1) and (n3>n4)):
    if(n2>n3):
        max =n2
    else:
        max = n3
if((n2>n1) and (n4>n3)):
    if(n2>n4):
        max =n2
    else:
        max = n4
if((n1>n2) and (n4>n3)):
    if(n1>n4):
        max =n1
    else:
        max = n4
print(max)
n11 = int(input("Enter the number 5:"))
if(max>n11):
    print(max)
else:
    print(n11)
