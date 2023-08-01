Marks =[2,1,3,2.6,"String"]
print(Marks[0])
print(Marks[2])

print(Marks[-1]) # Print list's item from last
print(Marks[-2])
# print(Marks[-6]) #Array Indexout of bounds


# If we want to print some selected items from list 
#print(Listname[startingIndex:LastIndex])
# Last Index item will not include in it.{}
print(Marks[1:4])
print(Marks[1:5])


# To display all items of a list with the help of for loop
for items in Marks:
 print(items)

# To display items of list using while loop
print("Using while loop")
i=0
while i<len(Marks):
    print(Marks[i])
    i=i+1

  
#Add something in list
Marks.append("New Item")
print(Marks)


# To insert any new item in  list on specific position 
# Listname.insert(IndexNo.,data)
Marks.insert(2,0)
print(Marks)

#update any old element
Marks[1]=3
print(Marks)

# Delete element from last
Marks.pop()
print(Marks)

# Delete element from specific position
Marks.pop(2)
print(Marks)

#Remove first item with specified by its value
#Marks.remove(2.3)

# Reverse order of a list
Marks.reverse()
print(Marks)

#To copy a list
Numbers=Marks.copy()
print(Numbers)

#To count any item in list(How many times it occur)
print(Numbers.count(1))


#To check any selected item exists in our list or not
print(2 in Marks) #Will return True
print(4 in Marks) #Will return False

#To know length of list
print(len(Marks))


# To clear all the elements of a List
Marks.clear()
print(Marks)

# To delete list permanently
del Marks

#To join two list 
list1=[1,2,3,4]
list2=[5,6,7,8]
list3=list1+list2
print(list3)
list1.extend(list2)
print(list1)

#Take List Item from user input
 
size =int (input("Enter How many items, you want to enter in list:"))
Numbers = []
i=0
while(i<size):
    print("Enter", i+1, "Number:")
    item=int(input())
    Numbers.append(item)
    i=i+1


#Print all list items
print("List Items are below:")
k=0
while(k<size):
    print(Numbers[k])
    k=k+1
#Second way to print List Items
print("This is another way to print list items")
print(Numbers)
    

#Calculate sum of all list items
j=0
sum=0
while(j<size):
    sum=sum+Numbers[j]
    j=j+1

print("Total sum of list items = ", sum)

#To sort any List:
Mark=[6,8,2,5,1,7]
Mark.sort()
print(Mark)

list1=[1,2,3,4]

list2=[]
for i in list1:
    list2.append(2*i)
print(list2)
dbl=list(map(lambda x:2*x,list1))
print(dbl)

#List to dictionary
key=[1,2,3,4]
value=["A","B","C","D"]
li_to_dic=dict(zip(key,value))
print(li_to_dic)


#max fun
maxi=max(dbl)
print(maxi)

mini=min(dbl)
print(mini)