def add(n1,n2):
    n1+=n2
    return n1
def sub(n1,n2):
    n1-=n2
    return n1
def multi(n1,n2):
    n1*=n2
    return n1
def div(n1,n2):
    n1/=n2
    return n1
def mods(n1,n2):
    n1%=n2
    return n1
def expo(n1,n2):
    n1**=n2
    return n1
def flo(n1,n2):
    n1//=n2
    return n1
n1 = int(input("Enter the number1:"))
n2 = int(input("Enter the number2:"))
print(add(n1,n2))
print(sub(n1,n2))
print(multi(n1,n2))
print(div(n1,n2))
print(mods(n1,n2))
print(expo(n1,n2))
print(flo(n1,n2))
