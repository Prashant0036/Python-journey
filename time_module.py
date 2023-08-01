import time
print(time.time())

# factorial
initial=time.time()
num=7
facto=1
for i in range(num,1,-1):
     facto=facto*i
print(facto)
print(f"Time taken using for loop is {initial-time.time()}")
#OR

time.sleep(5) #It will wait for 5 second 

def facto(num):
    
    if num==1:
        return 1
    elif num==0:
       return 0
    else:
     return(num*facto(num-1))
initial_1=time.time()
print(facto(7))
print(f"Time taken using recursion is {initial_1-time.time()}")


print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
time_tuple=(time.localtime())
print(time.strftime('%d/%m/%Y %H:%M:%S',time_tuple))

