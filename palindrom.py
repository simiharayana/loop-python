i=int(input("enter the number: "))
p=0
x=i 
while i>0:
    p=(p*10)+(i%10)
    i//=10
print(p)
if (x==p):
    print("yes number is palindrom! ")
else:
    print("not")