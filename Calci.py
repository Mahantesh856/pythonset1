def add(num1, num2):
    return num1+num2
def subs(num1, num2):
    return num1-num2
def multi(num1 , num2):
    return num1*num2
def div(num1, num2):
    return num1/num2

select = input("Select the operation of Calci:")

num1 = int(input("Enter the number 1:"))
num2 = int(input("Enter the number 2:"))
if select == '1':
    print(add(num1,num2))
elif select == '2':
    print(subs(num1,num2))
elif select == '3':
    print(multi(num1, num2))
elif select == '4':
    print(div(num1, num2))
else:
    print("Invalid Input")
