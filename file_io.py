# File io basic
"""
"r"-- Open file for reading -default
"w"-- Open file for writing
"x"-- (Exclusive) Create file if not exists
"a"-- (append) Add more content to a file but in last

------ Modes -------
"t"-- text mode -default 
"b"-- Binary mode
"+"-- Read and Write

"""

"""
To know your working directory
import os
print(os.getcwd())

"""

# To read a file
f=open("prashant.txt","rt") #where "r" represents read mode and "t" represents text mode
content=f.read()
print(content)  
f.close()


f=open("prashant.txt","rb") #where "r" represents read mode and "b" represents binary mode
content=f.read()
print(content)  
f.close()

f=open("prashant.txt","rt") #where "r" represents read mode and "t" represents text mode
content=f.read(5) #It means we want to read first 5 character of this file
print("First 5 character",content)  
content=f.read(5) #It means we want to read next 5 character of this file
print("Next 5 character",content)
content=f.read(2345) #It all available character of this file
print("max possible character",content)
f.close()


f=open("sample.txt")
content=f.read()
for i in content:  # To print character by character
    print(i,end="")

f=open("sample.txt")
for i in f:  # To print line by line
    print(i,end="")
     
     # OR
f=open("sample.txt")
print()
print(f.readline()) # To print one line 
print(f.readline()) # To print another line

f=open("sample.txt")
print(f.readlines()) # will print file lines as an element of List

# tell() and seek() function
#f=open("seek_tell.txt","x")
f=open("seek_tell.txt","r+")

f.write("Hi! This is Prashant\n I'm a Billionaire")
f=open("seek_tell.txt","r")

print(f.readline())
print(f.tell()) #will tell where our pointer is ? (On which character) (op:22)
print(f.readline())
print(f.tell()) #will tell where our pointer is ? (On which character) (op:40)
f.seek(0) #will strat pointer from 0th character
print(f.readline()) #Will start read line from 0th char again
                   # because the pointer has reached on 0th character

#tell()
