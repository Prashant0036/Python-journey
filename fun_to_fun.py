def mul(a,b):
    return a*b
def add(a,b):
    return a+b

def High_order_fun(fun,x,y):
    print(fun(x,y))
    ''' fun is first class function'''

High_order_fun(add,3,4)

def sub(a,b):
    return a-b
subtract=sub
print(subtract(6,3))

#Closures:
def outer ():
    x=200
    def inner():
        print('''This is inner function''')

    return inner


inner=outer()
inner()
#returnFun()
#print(returnFun)
#returnFun.inner()