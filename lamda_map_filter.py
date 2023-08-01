#Lambda Function
add = lambda x,y: x+y
upper = lambda x: x.upper()

print(add(2,7))
print(upper("prashant"))


#map function
list_=["1","2","3","4"]

''' now I have to convert all list items into integer
1 - without using map function '''
# for i in range(len(list_)):
#     list_[i]=int(list_[i])

''' using map() function'''
list_=list(map(int,list_))
c=list_[0]+1


num=[1,2,3,4,5,6]
# I want another list of squre of these list items

squre=list(map(lambda x:x*x,num))
print(squre)

#using Filter 
lstForFilter=[1,2,3,4,5,6,7,8,9]
odd=list(filter(lambda x:x%2!=0,lstForFilter))
print(odd)
