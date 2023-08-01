class abc:
    sal=10
    def __init__(self,sal,roll):
        self.sal=sal
        self.roll=roll

    def fun(self):
        print(self.sal)

     
ob = abc(5000,121)
print(ob.__dict__)
ob1=abc(7000,213)
ob.fun()
print(ob.sal)


def fun1(fun):
    print(1)
    fun()
    print(0)

@fun1                              
def fun2():
    print(333)

def fun3():
    print(888)

class Employee:
    empLeaves=8 # class variable
                        
prashant=Employee()
anant=Employee()

prashant.sal=200000 #instance variable, Har kisi variable k liye alag hoga
anant.sal=100000 # same as above
print(prashant.sal)
print(anant.sal)
print(prashant.empLeaves) #or
print(anant.empLeaves) #or
print(Employee.empLeaves) #class variable sab k liye same hoga but class.var se hi change hoga


