emp=("a","b","c")
print("Data type of emp:",type(emp))
print(emp)
l1=list(emp)
new_itm=input("Enter new element:")

l1.append(new_itm)
emp=tuple(l1)

    
#To print tuple     
print(emp)

#To print tuple with for each loop
count=0
for i in emp:
    count+=1
    print(i)

#To traverse tuple with for loop
for j in range(0,len(emp)):
    print(j+1,":",emp[j])

t1=tuple((6,2,3))
print(t1)
t2=tuple((4,5))
print(t1)
t3=sum((t1,t2),())
print(t3)
r=all(t1)
print(r)