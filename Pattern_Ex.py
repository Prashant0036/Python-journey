import math
#Question-1
""""    1
        12
        123
        1234
        12345 """

for i in range (1,6):
    for j in range(1,6):
       if j<=i: 
        print(j,end="")
       else:
            print(" ",end="") 
    print()

print("1st one is completed".center(50,"*"))

#Question-2
""""    1
        2  3
        4  5  6
        7  9  9  10
        11 12 13 14 15 """

k=1
for i in range (1,6):
    for j in range(1,6):
        if j<=i:
            print(" ",k,end="")
            k+=1    
        else:
            print(" ",end="")
            
    print()    

print("2nd one is completed".center(50,"*"))

#Question-3
""" 1 2 3 4 5
    1 2 3 4
    1 2 3
    1 2
    1        """

for i in range(1,6):
    for j in range(1,6):
        if j<=6-i:
            print(j,end=" ")
        else:
            print("",end="")
    print()             
print("3rd one is completed".center(50,"*"))

#Question-4
'''     1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5

 '''

for i in range(1,6):
    k=1
    for j in range(1,6):
        if j>=6-i:
         print(k,end="")
         k+=1
        else:
            print(" ",end="")
    print()

print("4th one is completed".center(50,"*"))


#Question-5
'''     1
      2 1
    3 2 1
  4 3 2 1
5 4 3 2 1
'''
for i in range(1,6):
    k=5
    for j in range(1,6):
        
        if j>=6-i:
            print(k,end="")
            
        else:
            print(" ",end="")
        k-=1
    print()

print("5th one is completed".center(50,"*"))

#Question-6
'''
P
P r
P r a
P r a s
P r a s h
P r a s h a
P r a s h a n
P r a s h a n t

'''
nm="Prashant"
length=len(nm)
for i in range (1,length+1):
    for j in range(i):
        print(nm[j],end="")
    print()

print("6th one is completed".center(50,"*"))

# Question-7
''' 
 P r a s h a n t
 P r a s h a n
 P r a s h a
 P r a s h
 P r a s
 P r a
 P r
 P
 

'''
nm="Prashant"
for i in range(1,length+1):
    for j in range(length):
        if j<=8-i:
            print(nm[j],end="")
        else:
            print(" ",end="")
    print()



