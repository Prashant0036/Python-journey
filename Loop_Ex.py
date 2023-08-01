i=5
while i>0:
    
    print("*" *i)
    i-=1
    
for i in range(5):
 print(i+1)

Students=["Ram","Shyam","Radha",]

#print any string multiple times using for loop:
for i in range(1,21,1):
    print(i,":","Prashant ",end="")

#Print series of 1 to 20:
for i in range(1,21,1):
    print(i)

#Reverse series 20 to 1:
for i in range (20,0,-1):
    print(i)


#Print second largest no. of series
X=[]
for i in range (20,0,-1):
    print(i)
    X.append(i)
print(X)    
print("Second Largest Number of This des. series=",X[1])



#Odd no. series 1 to 20:
for i in range (1,21,2):
    print(i)

for i in range (1,21,1):
       if i%2!=0: #for odd no.  
          print(i) 

for i in range (1,21,1):
   if i%2==0: #for even no.  
    print(i) 
   
#Even no. series 1 to 20:
for i in range (2,21,2):
    print(i)    


#Print any string char. by char.
nm="Prashant"
for i in range(0,len(nm),1):
   print(nm[i])


#Reverse a string using loop

nm="Prashant"
for i in range (len(nm)-1,-1,-1):
    print(nm[i],end="")



