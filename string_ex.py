
nm="Prashant"
print(nm.lower())
print(nm.upper())
print(nm.__eq__("prashant"))
print(nm.find('r'))
print(nm.find("sha"))
print(nm.replace("Pra","Shri"))
print("T" in nm)
print("t" in nm)
print(len(nm))
#reverse a string
print(nm[::-1])

#skip last char of any string
print(nm[:-1])

#range Keyword
number=range(8) #0,1,2,3,4,5,6,7 {8 will not include in it}
print(number)

#Sort any String using for loop:
p=[]
nm="Prashant"
for i in range (0,len(nm),1):
      p.append(nm[i])
p.sort()
print("sorted name=",p)

#Print any string char. by char.
nm="Prashant"
for i in range(0,len(nm),1):
   print(nm[i])

# If any substring or character is repeating more than one time in any string 
# Then, To find it's duplicacy in that string, we use "count" function.

line=" Hey Ram! Are You there Ram? Ram Where are you going "
para=""" Hey Ram! Are You there Ram? Ram Where are you going
      Hey Ram! Are You there Ram? Ram Where are you going
      Hey Ram! Are You there Ram? Ram Where are you going"""
#To find that how many times Ram is occur in this line or para"

print(line.count("Ram")) #returns 3 time
print(para.count("Ram")) #returns 9 time

from collections import Counter
print(Counter("below")==Counter("elbow"))