qst = set(("What is Data Structure?", "Explain Database Management System.",
          "What is Primary Key?", "What is TCP/IP model?", "What is set in Python?", "What is pointer?"))


def show():
    k = 0
    for i in qst:
        k += 1
        print("Q.", k, ":", i)


def odd():
    k = 0
    for i in qst:
        k += 1
        if k % 2 != 0:
            print("Q.", k, ":", i)


def even():
    k = 0
    for i in qst:
        k += 1
        if k % 2 == 0:
            print("Q.", k, ":", i)


list1 = list(qst)


def dlt():

    show()
    ch = int(input("Enter Question No. to delete:"))
    print()

    print("You have selected Question ", '"',
          list1[ch-1], '"', "to delete!")

    def dlt1():
        print("Are you confirm? \n Press y for yes \n Press n for reselect")
        ch1 = input()
        if ch1 == 'y' or ch1 == 'Y':
            list1.pop(ch-1)
            qst = set(list1)
            print("Updated Questions are below:")
            print()
            k = 0
            for i in qst:
                k += 1
                print("Q.", k, ":", i)

        elif ch1 == 'n' or ch1 == 'N':
            dlt()
        else:
            print()
            print("Please Enter valid input")
            show()
            dlt1()
    dlt1()


def updt():
    qst = set(list1)
    k = 0
    for i in qst:
                k += 1
                print("Q.", k, ":", i)

    def updt1():
        ch = int(input("Enter Question no. you want to update:"))
        print("You have selected Question ", '"',
              list1[ch-1], '"', "to update!")
        print("Are you confirm? \n Press y for yes \n Press n for reselect")
        ch1 = input()
        if ch1 == 'y' or ch1 == 'Y':

            value = input("Enter new Question:")
            list1[ch-1] = value
            qst = set(list1)
            print()
            print("Updated Questions are below:")
            print()
            k = 0
            for i in qst:
                k += 1
                print("Q.", k, ":", i)
        elif ch1 == 'n' or ch1 == 'N':
            updt()
        else:
            print("Please Enter valid input")
            k = 0
            for i in qst:
                k += 1
                print("Q.", k, ":", i)
            updt1()
    updt1()


def size():
     
    
     length=len(list1)
     print("Total no. of Question in this Set:",length)

while(1):
    print(" Question Set ".center(50,"*"))
    print()
    print("1/- To Print all Questions ")
    print("2/- To Print even no. Questions ")
    print("3/- To Print odd no. Questions ")
    print("4/- To Delete any Question ")
    print("5/- To Update any Question ")
    print("6/- To Print no. of Questions ")
    print()
    ch=input("Enter Your Choice from above menu:")
    if ch == '1':
            show()
    elif ch == '2':
        even()
    elif ch == '3':
        odd()
    elif ch == '4':
        dlt()
    elif ch == '5':
        updt()
    elif ch == '6':
        size()
    else:
        print("Please Enter valid input [1-6]")
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


