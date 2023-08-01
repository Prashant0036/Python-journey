print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5//2) #To Remove Decimal Part
print(5%2)
print(5**2) #To find power of a No.
i=1
i=i+2 
#OR 
i+=2

j=5
j=j-2
#OR
j-=2

j=2
j=j*2
#OR
j*=2

#OPERATOR PRECEDENCE
print(2+5*2) #Result = 14 or 12 
# Result will be 12
print((2+5)*2)
# Now Result will be 14

#Comparison Operator (Return Logical Value)
print(5<=2) #Return False
print(5>=2) #Return True
print (5==2) #Return False
print (5==5)#Return True
print(2!=5)#Return True
print(2!=2) #Return False


# Logical Operator
print(5==2 or 6==6) #Return True
print(5==2 or 6!=6) #Return False bcz both cond. are false
print (5==2 and 6==6) #Retun False
print(5==5 and 6==6) #Return True
print(not (5==5 and 6==6)) #Return False


#Membership Operator {in and not in}
# To check any substring exists or not in any String
#If that substring exists --> Return True
#If that substring not exists --> Return False
nm="Prashant"
print("Pr" in nm) #--> Return True
print("Kra" in nm) #--> Return False
print("Pr" not in nm ) #--> Return False
print("Kra"not in nm) #--> Return True