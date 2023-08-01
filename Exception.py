try:
   # print(2/0)
    lst=[2,3,2,23,42]
   # print(lst[7])
    print(2/0)




#except ZeroDivisionError as e:
 #   print(33703)
  #  print(e)
#except (IndexError,ZeroDivisionError) as e:
 #  print(e)   
except (Exception) as e :
    print(e)
else:
    print("This is else block")
finally :
    print("Finally Block")

a=17
# if a<18:
#     raise ValueError("You can not apply.")

assert a>18, "Sorry"