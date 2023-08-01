stu={1000:"Prashant",1001:"Anant",1002:"Vivek"} #Define a dict.

#To print type of stu
print(type(stu))

#To print Dict.
print(stu)

def def_dict():
    #This is another way to define a dictionary
    D = {"Prashant":{"Lunch":{"Roti":4}},"Devesh":{"Dinner":{"Rice":"One Plate"}},"Ram":"Breakfast"}

    print(D)
    print(D["Prashant"])
    print(D["Prashant"]["Lunch"])
    print(D["Prashant"]["Lunch"]["Roti"])



#To print key of an dictionary
print(stu.keys())
  #OR
print("List of Roll No.")
for i in stu.keys():
    print(i)

#To print value of keys
for i in stu.values():
    print(i)



print("List of Roll No. and Name")
for i,j in stu.items():
    print(i,":",j)

# To add any value
stu[1003]="Devesh"
print(stu)

#To update any value
stu[1003]="Yogesh"
print(stu)

#To delete any value
del stu[1003]
print(stu)


#To create a copy of dictionary
stu1=stu.copy() 
print(stu1)

#To access any value from it's key
print(stu.get(1001))

#To add any element in dict
stu.update({1004:"Ria"})
print(stu)