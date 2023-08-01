Emp = ["Yogesh", "Devesh", "Dev", "Ashwani", "Anant",
       "Vijay", "Roopesh", "Devesh", "Yogesh", "aadu"]


def show():
    print("All Employees of company:")
    print(Emp)


def dup_emp():
    print("These are duplicate Employees in company:")
    for i in range(0, len(Emp)):
        cnt = Emp.count(Emp[i])
        if cnt > 1:
            print(Emp[i])


def last_emp():
    print("Last Employees of company:")

    print(Emp[-1])


def add_emp():
    newEmp = input("Enter new Employee name:")
    Emp.append(newEmp)
    print("Updated Employees are:", Emp)


def ins_emp():
    newEmp = input("Enter new Employee name:")
    pos = int(input("Enter the position at which you want to add new Employee:"))
    Emp.insert(pos, newEmp)
    print("All updated Employees of company:")
    print(Emp)


def top5_emp():
    print("These are Top 5 Employees of company")
    print(Emp[0:5])


def del_lemp():

    Emp.pop()
    print("Updated Employees are:",)
    print(Emp)


def del_3emp():
    pos = int(input("Enter the position of which you want to remove an Employee:"))
    Emp.pop(pos+1)
    print("Updated Employees are:",)
    print(Emp)


def Up_case():
    print("Employees name in Upper Case:")
    emp_upper = [emp.upper() for emp in Emp]
    print(emp_upper)


def low_case():
    print("Employees name in Lower Case:")

    emp_lower = [emp.lower() for emp in Emp]
    print(emp_lower)


def proper_case():
    print("Employees name in proper Case:")

    emp_proper = [emp.capitalize() for emp in Emp]
    print(emp_proper)


def no_of_emp():
    print("There are ", len(Emp), " Employees in your Company")


def emp_strt_vow():
    print("Employees, Whoose name starts with a  vowel:")

    emp_upper = [emp.upper() for emp in Emp]
    
    for i in range(0, len(Emp)):

        if emp_upper[i].startswith('A') or emp_upper[i].startswith('E') or emp_upper[i].startswith('I') or emp_upper[i].startswith('O') or emp_upper[i].startswith('U'):
            emp_cap = [emp.capitalize() for emp in emp_upper]
            print(emp_cap[i])
           
    # if k>1:    
    #  print("There is no employee which name starts with a vowel")


def jn_nw_li():
    Emp2 = []
    size = int(input("Enter how many employees you want to add:"))
    print("Enter new Employees name one by one:")
    for i in range(0, size):
        print("Enter", i+1, "Employee name:")
        emp = input()
        Emp2.append(emp)
    Emp.extend(Emp2)
    print("List of updated Employees is below:")
    print(Emp)


def clear_():
    Emp.clear()
    print(Emp)
    print("Employees data from List has been cleared Successfully")


def delete_():
    Emptemp = Emp.copy()
    cnfrm = input(
        "Are you sure to delete Employees data permanently?\n Press Y for delete:\n Press N for Cancel:")
    if cnfrm == "Y" or cnfrm == "y":
        del Emptemp
        print("Employee List has been deleted Successfully")
    elif cnfrm == "N" or cnfrm == "n":
        print("Thank you!")
    else:
        print()
        print("Please! Enter Valid Input")
        if cnfrm !="Y" or cnfrm !="y" or cnfrm != "N" or cnfrm != "n":
           delete_() 



while(1):
    print()
    print()
    print("[ Welcome to Employee Management System ]".center(95, "*"))
    print()
    print("[ Menu ]".center(95, "-"))
    print(" 1/- To show all records of Employees")
    print(" 2/- To show duplicate Employees")
    print(" 3/- To show last Employee")
    print(" 4/- To add new Employee at end")
    print(" 5/- To add new Employee at specific position")
    print(" 6/- To show top 5 Employees name")
    print(" 7/- To delete last Employee")
    print(" 8/- To delete any Employee from specific position")
    print(" 9/- To show all Employees name in upper case")
    print("10/- To show all Employees name in lower case")
    print("11/- To show all Employees name in proper case")
    print("12/- To show number of Employee in company")
    print("13/- To show all Employees, whoose name starts with a vowel")
    print("14/- To add new Employee list")
    print("15/- To clear Employeed data from list")
    print("16/- To delete Employee list permanently")
    print()
    print("Please! Enter your choice [1-16] according to given menu:")
    ch = (input())
    if ch == '1':
        show()
    elif ch == '2':
        dup_emp()
    elif ch == '3':
        last_emp()
    elif ch == '4':
        add_emp()
    elif ch == '5':
        ins_emp()
    elif ch == '6':
        top5_emp()
    elif ch == '7':
        del_lemp()
    elif ch == '8':
        del_3emp()
    elif ch == '9':
        Up_case()
    elif ch == '10':
        low_case()
    elif ch == '11':
        proper_case()
    elif ch == '12':
        no_of_emp()
    elif ch == '13':
        emp_strt_vow()
    elif ch == '14':
        jn_nw_li()
    elif ch == '15':
        clear_()
    elif ch == '16':
        delete_()
    else:
        print("Please! Enter your choice [1-16] according to given menu:")
        print("Enter any right choice from below:")
        print()
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
