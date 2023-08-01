def pdrm():
    str=input("Enter a string:")
    str1=str.upper()
    if str1==str1[::-1]:
        print("It is Palindrome" )
    else:
        print("It is not Palindrome" )
#pdrm()
def sum():
    print("Enter two numbers one by one:")
    a=int(input())
    b=int(input())
    print("Sum of two numbers is:",a+b)
# sum()

def tpl():
    print("How many elements you want to enter?")
    size=int(input())
    a=[]
    for i in range (size):
        print("Enter",i+1,"element:")
        x=int(input())
        a.append(x)
    t=tuple(a)
    print(t)
# tpl()

def dict():
    a=[]
    b=[]
    sb=b.sort()
    dic={}
    for i in range (5):
        print("Enter",i+1,"Roll no.:")
        x=int(input()) 
        a.append(x)
        print("Enter",i+1,"Student name:")
        y=input() 
        b.append(y)
    for i in range (5):
      
        dic[a[i]]=b[i]
    l=list(dic.values())
    l1=l.sort()
    print(dic)
    print(l1)

dict()

def swap6():
    nm=input("Enter your name:")
    l=list(nm)
    length=len(nm)
    l[0], l[length-1]= l[length-1],l[0]
    str=""
    print(str.join(l))
    
swap6()
def txt7():
   f=open("pqr.txt","x")

def asc():
    c=input("Enter any character:")
    print("ASCII value is:",ord(c))
asc()
def pat():
    nm="Apple"
    length=len(nm)
    for i in range (1,length+1):
        for j in range(i):
            print(nm[j],end="")
        print()
pat()

def subs():
  str="Prashant"
  print(str[:3])
  print(str[3:])

subs()