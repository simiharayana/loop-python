# sum=number of queb
i=int(input("enter the num:-"))
b=i
sum=0
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if b==sum:
    print(b,"armstrong")
else:
    print("not")
