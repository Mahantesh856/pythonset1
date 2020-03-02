l =[]
sum = 0
for i in range(10):
    num = int(input("Enter the number:"))
    l.append(num)
    sum+=num
avg = sum/10
print(avg)
for i in range(10):
    if(l[i]<avg):
        print("lower than avg:"+ l[i])
    elif(l[i]>avg):
        print("higher than avg:"+ l[i])
    else :
        print("equal to avg:"+ l[i])
