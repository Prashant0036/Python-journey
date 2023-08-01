Emp1=["jay","Ajay","jay","Ankit","jaya","jay"]
cnt=int((Emp1.count("jay")))
if cnt>1:
    for i in (0,len(Emp1)-1):
        Emp1.remove("jay")
        #Emp1.remove("jaya")


print(Emp1)