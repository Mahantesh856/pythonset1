
def bitand(n1,n2):
    temp =  n1 & n2
    return temp
def bitnot(n1):
    return ~n1
def bitor(n1,n2):
    temp = n1|n2
    return temp
def bitxor(n1,n2):
    temp = n1^n2
    return temp
def bitright(n1,n2):
    temp = n1>>n2
    return temp
def bitleft(n1,n2):
    temp = n1<<n2
    return temp

n1 = int(input("Enter the number1:"))
n2 = int(input("Enter the number2:"))
print(bitand(n1,n2))
print(bitor(n1,n2))
print(bitnot(n1))
print(bitxor(n1,n2))
print(bitright(n1,n2))
print(bitleft(n1,n2))
