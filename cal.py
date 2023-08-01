# a=int(input("Enter first number"))
# b=int(input("Enter second number"))
# print(" Enter operation - + * /")
# ch=input()
# if ch=="+":
#     print(a+b)
# elif ch=="-":
#     print(a-b)

# elif ch=="*":
#     print(a*b)

# elif ch=="/":
#     print(a/b)
count=1
for num in range(3,51):
        for i in range(2,num):
            if(num%i)==0:
               count+=1
               break
            # else:
            #     count+=1
            #     break
print("There are" ,50-count,"prime numbers bw 2 to 50")

