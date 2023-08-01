nm=input("Enter a name:")
lnm=len(nm)
list=[]
for i in range (lnm) :
    list.append(nm[i])
ln=len(list)

d={ }
for j in range ( ln ):
  cn=  list.count(list[j])
  d[list[j]]=cn
#   print(list[j],":",cn)
for i,j in d.items():
    print(i ,":", j)
