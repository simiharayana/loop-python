i=int(input("enter the number:-"))
x=i
s=0
while i>0:
    s+=i%10
    i//=10
if x%5==0:
    print("yes this is a hursad number!!")
else:
    print("not a husad number!!")