def max(a,b,c):
    if(a>b)and(a>c):
        largest = a
    elif(b>c):
        largest = b
    else:
        largest = c
        return largest

a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
c = int(input("enter the value ofc:"))
print(max(a,b,c))