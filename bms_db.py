'''
WAP of BMS
create a reg. form
view acc. holder details
update details
delete details

'''
import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="",database="bms")
mycur=conn.cursor()
def acc_reg():
    
    acno=int(input("Enter Account Number:"))
    acnm=input("Enter Account Holder Name:")
    actyp=input("Enter Account type:")
    inbal=int(input("Enter opening Balance:"))

    conn=mysql.connector.connect(host="127.0.0.1",user="root",password="",database="bms")
    # print("Success")
    mycur=conn.cursor()
    a="insert into ah_reg (acno,acnm,actyp,inbal) values (%d,'%s','%s',%d)" %(acno,acnm,actyp,inbal)
    
    mycur.execute(a)  
    # mycur.execute(b)
    conn.commit()
    print("Record inserted")

def acc_dtls():
 ch=input("Press y to show all data:")
 if ch=='y' or ch=='Y':
        print("Here it is..")
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="",database="bms")
        mycur=conn.cursor()
        b='select * from ah_reg '
        mycur.execute(b)
        result=mycur.fetchall()
        count=0
        for x in result:
            count+=1
            print(count, "Account holder details---")
            print("Account Number:")
            print(x[0])
            print("Account Holder Name:")
            print(x[1])
            print("Account Type:")
            print(x[2])
            print("Account Balance:")
            print(x[3])
            
            print()

def acc_srch():
   acn=int(input("Enter Your Account Number:"))
   
   conn=mysql.connector.connect(host="127.0.0.1",user="root",password="",database="bms")
   mycur=conn.cursor()
   q='select * from ah_reg where acno=%d' %(acn)
   mycur.execute(q)
   for x in mycur.fetchall():
            print("Account holder details of Account Number ",acn)
            print("Account Number:")
            print(x[0])
            print("Account Holder Name:")
            print(x[1])
            print("Account Type:")
            print(x[2])
            print("Account Balance:")
            print(x[3])
            
            print()
# 


def acc_updt():
  
  def updt_nm():
   acn=int(input("Enter Your Account Number:"))
   nw_nm=input("Enter your name to be updated:")
   q= "update ah_reg set acnm= '%s' where acno= %d" %(nw_nm,acn)
   mycur.execute(q)
   conn.commit()
   print("Your details has been updated successfully you can check it out...")
   q1="select * from ah_reg where acno =%d" %(acn)
   mycur.execute(q1)
   result=mycur.fetchall()
   for x in result:
        print(x)
   
  def updt_at():
    acn=int(input("Enter Your Account Number:"))
    print("Press S for convert current to saving")
    print("Press C for convert saving to current")
    ch=input()
    if ch=="C" or ch=="c":
        q='update ah_reg set actyp="Current" where acno=%d' %(acn)
        mycur.execute(q)
        conn.commit()
        print("Your details has been updated successfully you can check it out...")
        q1="select * from ah_reg where acno =%d" %(acn)
        mycur.execute(q1)
        result=mycur.fetchall()
        for x in result:
                print(x)
    elif ch=="S" or ch=="s":
        q='update ah_reg set actyp="Saving" where acno=%d' %(acn)
        mycur.execute(q)
        conn.commit()
        print("Your details has been updated successfully you can check it out...")
        q1="select * from ah_reg where acno =%d" %(acn)
        mycur.execute(q1)
        result=mycur.fetchall()
        for x in result:
                print(x)
    else:
        print("Please Emter valid input")

    


  while(1):
        print(" 1/- To update your name")
        print(" 2/- To update your account type")
        ch=int(input("Enter your choice from menu [1-2] :"))
        if ch==1:
            updt_nm()
            
        elif ch==2:
            updt_at()
            
        else:
            print("Please Enter valid input")
        print("Do you want to continue? \n press y for y \n press n for exit")
        choice=input()
        if choice =="y":
            continue
        elif choice=="n":
            break




 


def acc_del():
    def del_():
        acn=int(input("Enter your account number"))
        q="delete from ah_reg where acno=%d" %(acn)
        mycur.execute(q)
        conn.commit()
        print("Your account has been deleted successfully")

    print("You are going to delete your account\n press y for confirm \n press n for exit")
    ch=input()
    if ch=="y" or ch=="Y":
        del_()
    elif ch=="n" or ch=="N":
        pass
    
while(1):
    print("Welcome to our Bank".center(50,"*"))
    print()
    print("1/- To open your account")
    print("2/- To view all account in our Bank")
    print("3/- To view your account details in our Bank")
    print("4/- To update your details in our Bank")
    print("5/- To close your account")
    print("Please enter your choice from above menu [1-5]:")
    ch=int(input())
    if ch==1:
       acc_reg()
    elif ch==2:
       acc_dtls()
    elif ch==3:
       acc_srch()
    elif ch==4:
        acc_updt()
    elif ch==5:
        acc_del()
    else:
        print("Please Enter Valid Input")
        continue
    print()
    print('Do you want to continue? \n press y for yes \n press n for exit')
    choice=input()
    if choice=="y" or choice=="Y":
        continue
    elif choice=="n" or choice=="N":
        break
    else:
        print("Please Enter Valid Input")
        
    

       
       
    
