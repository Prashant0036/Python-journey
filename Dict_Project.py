sdnt={1000:"Nisnant",1001:"Ram",1002:"Shyam",1003:"Mayank",1004:"Prashant",1005:"Ria",1006:"Anant",1007:"Yogesh",1008:"Kartik",1009:"Anushka"}

def roll():
    print("All roll no. are below:")
    k=0
    for i in sdnt.keys():
     k+=1
     print(k,"/-",i)

def nm():
    print("All student names are below:")
    k=0
    for i in sdnt.values():
     k+=1
     print(k,"/-",i)

def al_nm():
    print("All student names [alphabetically] are below:")
    list1=list(sdnt.values())
    list1.sort()
    k=0
    for i in list1:
        k+=1
        print(k,"/-",i)


def all():
    print()
    print("All student names along with their roll no., are below:")
    print()
    print("S. No."," Roll No."," Student Name")
    print()
    k=0
    for i, j in sdnt.items():
     k+=1
     print(k,"/-   ",i ,"    ",j)


def add():
    print("Enter new Student's Roll No:")
    rn=int(input())
    print("Enter new Student's Name:")
    nm=input()
    sdnt[rn]:nm
    sdnt[rn]=nm
    print("Record has been added successfully.\n Press 'Enter' to view: ")
    x=input()
    print()
    print("S. No."," Roll No."," Student Name")
    print()
    all()


def updt():
    all()
    print("Enter Student's Roll No you want to update:")
    prn=int(input())
    print("Enter new Student's Name:")
    nm=input()
    sdnt[prn]=nm
    print("Record has been updated successfully.\n Press 'Enter' to view: ")
    x=input()
    
    print()
    all()

def dlt():
 print()
 print("S. No."," Roll No."," Student Name")
 print()
 all()
 print("Enter Student's Roll No. you want to delete:")
 rn=int(input())
 def dlt1():
    print("Are you sure ? \n Press y for yes \n Press n for reselect")
    ch1 = input()
    if ch1 == 'y' or ch1 == 'Y':
        del sdnt[rn]

        print("Record has been deleted successfully.\n Press 'Enter' to view: ")
        x=input() 
        print()
        print("S. No."," Roll No."," Student Name")
        print()
        all()
    elif ch1=='n' or ch1=='N':
        dlt()
    else:
        print("Please enter a valid input")
        dlt1()
 dlt1()        

def vowel():
    
    list1=list(sdnt.values())
    k=0
    list1_upper = [j.upper() for j in list1]
   
    print(" Students names starting with vowel:")
    for i in range(0, len(list1)):
    
        if list1_upper[i].startswith('A') or list1_upper[i].startswith('E') or list1_upper[i].startswith('I') or list1_upper[i].startswith('O') or list1_upper[i].startswith('U'):
            list1_cap = [emp.capitalize() for emp in list1_upper]
            k+=1
            print(k,"/- ",list1_cap[i])
        


def cons():
    list1=list(sdnt.values())
    
    list1_upper = [j.upper() for j in list1]
    k=0
    print(" Students names starting with consonant:")
    for i in range(0, len(list1)):
    
        if list1_upper[i].startswith('A') or list1_upper[i].startswith('E') or list1_upper[i].startswith('I') or list1_upper[i].startswith('O') or list1_upper[i].startswith('U'):
            list1_cap = [emp.capitalize() for emp in list1_upper]
   
        else:
            k+=1
            print(k,"/- ",list1[i])



while(True):
    print()
    print("[ Welcome to Student Management System ]".center(50,"*"))
    print()
    print("Please choose a option from below:")
    print()
    print("1/- To Print the Roll no. of all Students")
    print("2/- To Print the names of all Students")
    print("3/- To Print the names of all Students [Alphabetically]")
    print("4/- To Print all record of Students")
    print("5/- To Add new record of any Student")
    print("6/- To Update record of any Student by Roll no.")
    print("7/- To Delete record of any Student")
    print("8/- To Check Students name starts with vowel")
    print("9/- To Check Students name starts with consonant")
    print()
    print("Please! Enter your choice [1-9] according to given menu:")
    ch = (input())
    if ch == '1':
        roll()
    elif ch == '2':
        nm()
    elif ch == '3':
        al_nm()
    elif ch == '4':
        all()
    elif ch == '5':
        add()
    elif ch == '6':
        updt()
    elif ch == '7':
        dlt()
    elif ch == '8':
        vowel()
    elif ch == '9':
        cons()
    else:
        print("Please Enter valid input [1-9]")
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



