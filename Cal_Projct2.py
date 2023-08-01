
while(True):
    import math


    def add_fun():
        print("Total Sum:", a+b)


    def sub_fun():
        print("Subtract  =", a-b)


    def mul_fun():
        #print("Total Multiplication is equal to :",a*b)
        mul = a*b
        return mul


    def div_fun():
        print(" Division is equal to ", a/b)


    def rem_fun():
        print("Remainder is equals to ", a % b)


    def pow_fun():
        print(a, " to the power ", b, " = ", pow(a, b))


    def sqrt_fun():
        print("Squre root of ", a, " is: ", math.sqrt(a))
        print("Squre root of ", b, " is: ", math.sqrt(b))


    print("Welcome to Calculator Panel:".center(50, "*"))
    print("--------------------------------------------------")
    a = int(input("Enter First Number:"))
    b = int(input("Enter Second Number:"))
    print(" 1/- For Addition\n 2/- For Subtraction\n 3/- For Multiplication\n 4/- For Division\n 5/- For Remainder\n 6/- For Power\n 7/- For Squre Root")
    print("Enter your Choice:")
    ch = int(input())

    if ch == 1:
        add_fun()
    elif ch == 2:
        sub_fun()
    elif ch == 3:
        result = mul_fun()
        print(" Multiplication is ", result)
    elif (ch == 4):
        div_fun()
    elif(ch == 5):
        rem_fun()
    elif(ch == 6):
        pow_fun()
    elif(ch == 7):
        sqrt_fun()
    else:
        print("Please! Enter a Right Choice")
     
    inp=input("Do you want to continue:\n Enter Y or N:\n")
    if inp=="Y" or inp== "y":
        pass
    elif inp=="N" or inp=="n":
        print("Thank You for choosing us. See you soon :)")
        break 
    else:
        print("Please Enter y for continue and n for exit")