i=int(input("enter the number: "))
r=0
while i>0:
    r=(r*10)+(i%10)
    i//=10
print(r)
