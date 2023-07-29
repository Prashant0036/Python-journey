#1. sqrt
# from ast import Num
# import math
# n=64
# print(math.sqrt(n))

# #2.
# base=2
# height=3
# area_of_tr=0.5*base*height
# print(area_of_tr)

# #3 
# a=2
# b=8
# c=3
# #d=underroot b squre - 4ac
# d=(b**2)-(4*a*c)
# if d>0:
#     print(d)
#     x1=(-1*b + math.sqrt(d))/(2*a)
#     x2=(-1*b - math.sqrt(d))/(2*a)

#     print("roots are ",x1,x2)
# else:
#     print("imaginary")

# #4
# a=2
# b=3
# temp=a
# a=b
# b=temp
# print(a,b)

# #OR

# a=2
# b=3
# a,b=b,a
# print(a,b)

# #5
# import random
# num=random.randint(1,10)
# print(num)

# #6 km to mile
# km=13
# miles=0.621*km
# print(miles)

# #7 celsius to fahrenheit
# c=37

# f=(c*9/5)+32
# print(f)

# #8 leap year
# year=1996
# if (year%400==0 and year%100==0) or (year%4==0 and year%100 !=0):
#     print("Leap year")
# else:
#     print("Not a Leap year")

# #9 comp. three num
# a=0
# b=0
# c=1
# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# # elif(a==b and b==c ):
# #     print(a)
# else:
#     print(c)

# #10 Prime Number
# num=97
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# if count==2:
#         print("Prime")
# else:
#         print("Not Prime")

# #11 how many prime in a range
# higher_num=1000
# non_prime=0
# for i in range(2,higher_num+1):
#     for j in range(2,i):
#         if i%j==0:
#            non_prime+=1
#            break
    
            
# total_num=higher_num-2
# prime=(total_num-non_prime)+1
# print(prime)


# #OR
# lower=300
# upper=330
# prime_counter=0
# for i in range(lower,upper+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         prime_counter+=1
# print(prime_counter)

# #12 factorial
# num=7
# facto=1
# for i in range(num,1,-1):
#      facto=facto*i
# print(facto)

# #OR

# def facto(num):
    
#     if num==1:
#         return 1
#     elif num==0:
#        return 0
#     else:
#      return(num*facto(num-1))

# print(facto(5))


# #13 Multiplication table
# n=5
# for i in range(1,11):
#     print(n,"X",i,"=",n*i)
# #OR
# i=1
# while(i<=10):
#      print(n,"X",i,"=",n*i)
#      i+=1
    
# #14 fibonacci series
# # def fibo(lower,size):
 
# #  if count>size:
# #         return 1
# #  else:
# #         return 


# # fibo(0,10)
# size=10
# n1=0
# n2=1
# i=1
# print(n1,n2,end=" ")

# while(i<=size-2):
#     n3=n1+n2
#     n1=n2
#     n2=n3
#     print(n3,end=" ")
    
#     i+=1
# print()

#15 Armstrong
n=153
n1=n
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem**3
    n=n//10
if n1==sum :
    print("Armstrong")
else:
    print("Not Armstrong")


#16 Armstrong in any intervel
lower=1
upper=1000
count=0
arm=0
for n in range(lower,upper+1):
        arm+=1
        n1=n
        sum=0
        while(n>0):
            rem=n%10
            sum=sum+rem**3
            n=n//10
        if n1==sum :
            count+=1
            print(arm)
        
print(f"there are {count} armstrong number bw {lower} and {upper}"  )

#17 Reverse
n=343
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)

#18 Palindrome

n=343
n1=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if n1==rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#19 Palindrome in an interval
lower=100
upper=1000
palin=0
count=0
for n in range(lower,upper+1):
    n1=n
    palin+=1
    rev=0
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if n1==rev:
        print(palin)
        count+=1
print(f"there are {count} palindrome number bw {lower} and {upper}"  )

#20 sum of n natural numbers
lower=1
upper=10
sum=0
for i in range(lower,upper+1):
    sum=sum+i
print(sum)

#21 find divisible numbers in any range by a given number
n=13
lower=1
upper=1000
count=0
for i in range(lower,upper+1):
    if i%n==0:
       count+=1
       print(i)

print(f"There are {count} numbers are divisible by {n} bw {lower} and {upper}")

#22





x=26