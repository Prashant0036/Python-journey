import sys
# it is used to manipulate runtime environment

print(sys.path) #PYTHONPATH environment variable
print("hii")
# sys.exit()
print("bye") #it will not print

print(sys.platform)
print(sys.modules) 
print(sys.executable)
print(sys.copyright)
for x in sys.argv:
    print(x)

 
