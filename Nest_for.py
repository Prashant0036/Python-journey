#Nested for loop:
for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(j,end="")
    print("")     


a =int(input("Enter no. of rows :"))
for i in range(a):
    for j in range (i+1):
        print(j+1, end=" ")
    print("") 

"""a =int(input("Enter no. of rows :"))
for i in range(a):
    for j in range (i+1):
        print(i+1, end=" ")
    print("")    

a =int(input("Enter no. of rows :"))
for i in range(a):
    for j in range (i,-1,-1):
        print(j+1, end=" ")
    print("")
"""


for i in range (1,6):
    for j in range(1,6):
       if j<=i: 
        print(j,end=' ')
       else:
            print(" ",end="")
    print() 

"""" 1
     12
     123
     1234
     12345"""



k=1
for i in range (1,6):
    for j in range(1,6):
        if j<=i:
         
         print(k,end=" ")
         k=k+1
        else:
         print(" ",end="")
    print()
    """"1
        2  3
        4  5  6
        7  9  9  10
        11 12 13 14 15"""

for i in range (1,6):
    for j in range (1,6):
        if j<=6-i:
            print(j,end=" ")
        else:
            print("",end="")
    print()       

""" 1 2 3 4 5
    1 2 3 4
    1 2 3
    1 2
    1        """    

for i in range (1,6):
    for j in range(1,6):
        if j>=6-i:
            print("*",end="")
        else:
            print(" ",end="")    
    print() 

"""      *
        **
       ***
      ****
     ***** """       

for i in range (1,6):
    for j in range(1,6):
        if j>=6-i :
            print(j,end="")
        else:
            print(" ",end="")    
    print()

for i in range (1,6):
    k=1
    for j in range(1,6):
        if j>=6-i:
            print(k,end="")
            k+=1
        else:
            print(" ",end="")    
    print() 
     

nm="Prashant"
x=""
for i in nm:
    x+=i
    print(x)


nm="Prashant"
length=len(nm)
for i in range (1,length+1):
    for j in range(i):
        print(nm[j],end="")
    print() 

      