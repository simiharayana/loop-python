# i=2
# while i<=20:
#     print(i)
#     i+=2



a=int(input("enter till you want to print your table: "))
i=1
while i<=a:
    print("next table is:",i)
    j=1
    while j<=10:
        print(i,"*",j,"=",j*i)
        j+=1
    i+=1
