#def stands for define
# #This is no returntype function

# def Eq_Checker():

#     print("Enter Three Numbers One by One:")
#     a,b,c=int(input()),int(input()),int(input())
     


#     if(a==b and b==c):
#      print("All Numbers are equal")
#     elif(a>=b and a>c):
#      print(a, "is largest No.")
#     elif(b>=a and b>c):
#         print (b ,"is largest No.")
#     else:
#         print(c, "is largest No.")


# Eq_Checker() #Calling the function


# #This is Return Type Function.
# def ret_fun():
#     print("Enter Three Numbers One by One:")
#     a,b,c=int(input()),int(input()),int(input())
     

 
#     if(a==b and b==c):
     
#      x=1
#     elif(a>=b and a>c):
     
#      x=2
#     elif(b>=a and b>c):
       
#         x=3
#     else:
        
#         x=4
     
#     return x

# result=ret_fun()
# if result==1:
#  print("All Numbers are equal")
# elif result==2:
#  print( " first one is largest No.")
# elif result==3:
#      print( " Second one one is largest No.")
# elif result==4:
#      print( " Third one is largest No.")


# #Another Ex. of Non-Return Type Funcion

# a=int(input("Enter First Number:"))
# b=int(input("Enter Second Number:"))
    
    
# def add_fun(): 
#  """  It will give addition of two numbers   """   
#  print("Total Sum:",a+b)

# def sub_fun():    
#  print("Subtract =",a-b)

# def mul_fun():    
#  print("Total Multiplication:",a*b)

# def div_fun():    
#  print("Total Division:",a/b)

# def rem_fun():    
#  print("Remainder:",a%b) 





# print(add_fun.__doc__)  # It will print docstring of this function
# add_fun()