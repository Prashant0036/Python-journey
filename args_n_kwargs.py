#Without using *args
def nm(a,b,c):
    print(a,b,c)
nm("Prashant","Devesh","Dogesh")
''' Now if I want to add some arguments in ths function then
    I have to do the same in function definaton, It couldn't be the best way'''

#Using *args
def nm(*name):
    print(name) #tuple

nm_list=["Prashant","Devesh","Dogesh","Ashwani","Vansh","XYZ"] #list
nm(*nm_list)

'''by using *name it will pass the list as a tuple in the nm() function'''


# Using **kwargs
def st_data(normal,*args,**kwargs):
      #Now we have passed our dict. in function as **kwargs
      
      for key,value in kwargs.items():
            print(f"Roll no. is {key} and the name is {value}")
      print(normal)
      print(args)


st_dict={1:"Prashant",2:"Vansh",3:"Anant",4:"Nishant"}
normal=2
st_data(normal,nm_list,st_dict)

''''Rule- first pass normal arguments then *args and then *kwargs'''

