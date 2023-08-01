#To create a new file
f=open("newfile12.txt","r")
print("file has been created successfully")

#Read any specific line using readlines() function

# With Exception Handling

try:
    f = open("Prashant.txt","rt")
    data = f.read()
    print(data)
    f.close() 
    print("File has been closed successfully")
except(IOError):
    print('''You can't open a file  
that doesn't exist''')

print("...Rest of the code")

# f = open("newfile.txt","rt")
# data = (f.readlines()[-1]) #[-1]- last line of file
# print("Last line of your file:") 
# print(data)

# f.close() 
# print("File has been closed successfully")


# # To read a file
# f=open("newfile.txt","r")
# print(f.read())

# Wit Exception Handling

# f = open("Prashant.txt","r")
# data = f.read()
# print(data)

# f.close()
# print("File has been closed Successfully")

# print("...Rest of the code")