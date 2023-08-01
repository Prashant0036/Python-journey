while(1):

    print("........Welcome to BookBazar.com........")
    print("----------------------------------------")
    print(" 1/- for Enter Stock Details \n 2/- For View Details")
    choice =int( input("Enter Your Choice:"))

    if choice==1:
            stcnm =input("Enter Item's Category:")
            itnm =input("Enter Item's Name:")
            price= float(input("Enter item Price:"))
            
            qnt = int(input("Enter item qnt:"))
        
            dis = int(input("Enter Discount percentage:"))
            pwd=float(qnt*price)
            fp=pwd-(pwd*(dis/100))
            print(fp)   
        
    if choice==2:
            print("\n\n\n")
            print("Item category Name:",stcnm)
            print("Item name:",itnm)
            print("Price of one Item:",price)
            print("Total Quantity:",qnt)
            print("Price without Discount",price*qnt)
            print("Total Dis. per.",dis)
            print("Final Price:",fp)
            print("Thank You! :)")
            break