def create() :
    f=open("abc.txt","x")
    print("File has been created successfully")

def apnd():
    cn=int(input("How many lines you want to add?"))
    
    for i in range (cn):
        f=open("abc.txt","a+")
        print("Enter the ", (i+1),"line data you want to add in file:")
        data=input()
        data=data+"\n"
        f.write(data)
    print("Data has been added successfully")

def wrt():
    f=open("abc.txt","w")
    data=input("Enter the data you want to write in file:")
    data=data+"\n"
    f.write(data)
    print("Data has been written successfully")

def prnt():
    f=open("abc.txt","r")
    print(f.read())

def f_ln():
    print("First line of this file :")
    f=open("abc.txt","r")
    print(f.readline())

def f_5ln():
    print("First 5 lines of this file :")
    f=open("abc.txt","r")
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())

def nol():
    f=open("abc.txt","r")
    k=0
    for i in f:
       k+=1 
    print("Number of lines in your file = ",k )

def clr():
    f=open("abc.txt","w")
    f.write("")
    print("Data has been cleared successfully")

def l_ln():
    print("Last line of this file :")
    f=open("abc.txt","r")
    print(f.readlines()[-1])

def l_2ln():
    print("Last two lines of this file :")
    f=open("abc.txt","r")
    print(f.readlines()[-1])
    print(f.readlines()[-1])
k=0
while(1):
    if k<1:
        k+=1
        print("[ Welcome to File Handling Program ]".center(50,"*"))
        print("[ Menu ]".center(50,"*"))
        print()
        print("Please choose a option from below:")
        print()
        print("1/- To Create a new file")
        print("2/- To Write data in file")
        print("3/- To add new data in file")
        print("4/- To Print all data of file")
        print("5/- To Print first line of file")
        print("6/- To Print last line of file")
        print("7/- To Print first 5 lines of file")
        print("8/- To Print last 2 lines of file")
        print("9/- To Print total number of line of file")
        print("10/- To Clear all data of file")

        print()
        print("Please! Enter your choice [1-10] according to given menu:")
        ch = (input())
        if ch == '1':
            create()
        elif ch == '2':
            wrt()
        elif ch == '3':
            apnd()
        elif ch == '4':
            prnt()
        elif ch == '5':
            f_ln()
        elif ch == '6':
            l_ln()
        elif ch == '7':
            f_5ln()
        elif ch == '8':
            l_2ln()
        elif ch == '9':
            nol()
        elif ch == '10': 
            print("Are you sure ? \n Press y for yes \n Press n for reselect")
            ch1 = input()
            if ch1 == 'y' or ch1 == 'Y':
             clr()
            else:
                continue
        else:
            print("Please Enter valid input [1-10]")
            continue
        print()
        choice = input(
            "Do you want to continue?\n Press Y for yes:\n Press N for Exit:")
        if choice == "Y" or choice == "y":
            continue
        elif choice == "N" or choice == "n":
            print()
            print("|| Thank you :) || See you soon........")
            print()
            break
        else:
            print("Please! Enter a valid input")
            continue
       
    else:
        print("[ Welcome to File Handling Program ]".center(50,"*"))
        print("[ Menu ]".center(50,"*"))
        print()
        print("Please choose a option from below:")
        print()
        print("2/- To Write data in file")
        print("3/- To add new data in file")
        print("4/- To Print all data of file")
        print("5/- To Print first line of file")
        print("6/- To Print last line of file")
        print("7/- To Print first 5 lines of file")
        print("8/- To Print last 2 lines of file")
        print("9/- To Print total number of line of file")
        print("10/- To Clear all data of file")

        print()
        print("Please! Enter your choice [2-10] according to given menu:")
        ch = (input())
        if ch == '1':
            print("Please enter valid input")
        elif ch == '2':
            wrt()
        elif ch == '3':
            apnd()
        elif ch == '4':
            prnt()
        elif ch == '5':
            f_ln()
        elif ch == '6':
            l_ln()
        elif ch == '7':
            f_5ln()
        elif ch == '8':
            l_2ln()
        elif ch == '9':
            nol()
        elif ch == '10': 
            print("Are you sure ? \n Press y for yes \n Press n for reselect")
            ch1 = input()
            if ch1 == 'y' or ch1 == 'Y':
             clr()
            else:
                continue
        else:
            print("Please Enter valid input [2-10]")
            continue
        print()
        choice = input(
            "Do you want to continue?\n Press Y for yes:\n Press N for Exit:")
        if choice == "Y" or choice == "y":
            continue
        elif choice == "N" or choice == "n":
            print()
            print("|| Thank you :) || See you soon........")
            print()
            break
        else:
            print("Please! Enter a valid input")
            continue