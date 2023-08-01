book={}
print(type(book)) #will show dictinory

book={1}
print(type(book)) #will show set

thisset=set(("x","y","z")) # Another way to create a set

book_nm={"a","b","c","d"}
print(book_nm)


#To print tuple using for each loop
k=0
for i in book_nm:
    k+=1   
    print(k,":",i)

thisset=set(("x","y","z")) # Another way to create a set

#To append any new value in set, we convert it in to list first to perform append operation
list1=list(thisset)
list1.append("P")
thisset=set(list1)
print(thisset)

#To remove any element by it's value
thisset.remove("x")

#To delete any random element from last
thisset.pop()

#To clear the set element
thisset.clear()

set2=set("Hello")
set2.add('r')
set2.remove('l')
print(set2)

set_1={1,2,3,4}

set_2={1,2,3,5,6}
print(7 in set_2)
print(set_1.issuperset(set_2))
set_3=set_1.intersection(set_2)
set_4=set_1.union(set_2)
print(set_3,set_4)