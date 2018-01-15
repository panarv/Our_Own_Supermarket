# Our Own Supermarket

import pickle

def Error_BI(m):    #A Function to obtain a value; and to handle The Blank Input Error or Input of type:string, if any
    while True:     #This Function does not involve parameters that require float values
        a=raw_input(m)
        if a.isdigit():
            return int(a)
        else:
            print "Please enter a Numeric Value of Type : Integer"

class item:
    def __init__(self):
        self.quantity=self.cp=self.sp=self.prof_perc=0
        self.name=""
    def input(self):
        try:
            self.name=raw_input("Enter Name of Item: ")
            self.quantity=Error_BI("Enter Quantity: ")
            self.cp=input("Enter Cost Price (AED): ")
            self.prof_perc=input("Enter Profit Percent (%): ")
            self.sp=float(self.cp)*(100.0+self.prof_perc)/100.0        #Calculating Selling Price
        except:
            print "'No Input/String Input Error' has occured. Please Re-Enter the Parameters"
            self.input()
        
class staff:                                                       #Admin or Employee
    def __init__(self):
        self.mob_num=0
        self.pwd="*****"
        self.name=""
    def input(self,staff_type):
        self.name=raw_input("\nEnter "+staff_type+" Name: ")
        self.pwd=raw_input("Enter Password: ")
        self.mob_num=raw_input("Enter Mobile Number: ")

def setup():
    items={}                                                #All Items are Stored in this List
    admin={1000:staff()}                                    #All Admin Details and Passwords are stored in this List
    employee={2000:staff()}                                 #All Sales Employee's Details are stored in this List
    sales=0                                                 #Total Sales Done
    profit=0                                                #Total Profit Earned
    io={"admin":0,"employee":0,"items":0}                   #Count for Deleted Staff and Items
    data={"status":0,"items":items,"adm":admin,"emp":employee,"sales":sales,"prof":profit,"io":io}
                                                            #A Dictionary containing all the data of the Supermarket

    f=open("Supermarket Data.dat","wb")                     #File for Storing all Data
    pickle.dump(data,f)
    f.close()   

def login():                                        #Function to Login to an Account
    print "\n====================================================================================================\n"
    print "Please enter your Admin/Employee ID to login to the System\nNote: Case Sensitive.\n"  
    f=open("Supermarket Data.dat","rb")
    data=pickle.load(f)
    admin=data["adm"]
    employee=data["emp"]
    f.close()
    while True:
        idno=Error_BI("Enter your User ID Number : ")
        password=raw_input("Enter your Password - ")    #Password
        admin_id=admin.keys()
        employee_id=employee.keys()
        if idno in admin_id:
            if admin[idno].pwd==password:
                print "\n======================================== LOGGED IN  TO ADMIN =======================================\n"
                print " "*43+"Welcome "+admin[idno].name+"!"
                menudisplay_admin()                
            else:
                print "\nIncorrect Password\n"
                continue
        elif idno in employee_id:
            if employee[idno].pwd==password:
                print "\n=================================== LOGGED IN TO  SALES  EMPLOYEE ==================================\n"
                print " "*43+"Welcome "+employee[idno].name+"!"
                menudisplay_emp()
            else:
                print "\nIncorrect Password\n"
                continue
        else:
            print "\nUser doesn't exist\n"

def addproduct():                                   #Function to Add n Products
    print "===================================================================================================="
    f=open("Supermarket Data.dat","rb")
    data=pickle.load(f)
    items=data["items"]
    io=data["io"]
    f.close()
    print "\t\t\t\t\tADD PRODUCT\n"
    n=Error_BI('Enter the Number of Products to be added: ')    
    for i in range(n):
        print"\nEnter Details for Product",(i+1),": "
        product=item()
        product.input()
        prod_id = 1001+len(items)+io["items"]
        items[prod_id]=product
        print "Product",product.name,"is Added.\nThe Product ID is: ",prod_id,"\nThe Selling Price is: AED",product.sp,"\n"
    f=open("Supermarket Data.dat","wb")
    pickle.dump(data,f)
    f.close()

def deleteproduct():                                #Function to delete Products
    print "===================================================================================================="
    f=open("Supermarket Data.dat","rb")
    data=pickle.load(f)
    items=data["items"]
    io=data["io"]
    f.close()
    print "\t\t\t\t\tDELETE PRODUCT\n"
    amount=len(items)
    n=amount+1
    while n>amount:
        n=Error_BI("Enter Number of Products to be Deleted: ")
        if n>amount:
            print "Error : Value Entered is more than Available Products. Please try again."    #Error Handling
    k=1
    while k<=n:
        prod_id=Error_BI("\nEnter Product ID of the Product to be deleted: ")
        if prod_id not in items.keys():
            print "Invalid ID Number. Please Enter Again."
        else:
            print "The Product,",items[prod_id].name,"has been Deleted.\n"
            del items[prod_id]
            io["items"]+=1
            k+=1
    f=open("Supermarket Data.dat","wb")                    
    pickle.dump(data,f)
    f.close()
        
def mod_productname():                              #Modify Product Name 
    print "===================================================================================================="
    f=open("Supermarket Data.dat","rb")
    data=pickle.load(f)
    items=data["items"]
    f.close()
    print "\t\t\t\t\tMODIFY PRODUCT NAME\n"
    while 1:
        mod_idno=Error_BI("Enter the ID Number of the Product: ")
        print
        if mod_idno not in items.keys():
            print "Invalid ID Number. Please Enter Again."
        else:
            items[mod_idno].name=raw_input("\nEnter New Name of Product: ")
            print "Name of the Product is changed to",items[mod_idno].name,"\n"
            break
    f=open("Supermarket Data.dat","wb")                    
    pickle.dump(data,f)
    f.close()
                
def mod_productquantity():                          #Modify Product Quantity
    print "===================================================================================================="
    f=open("Supermarket Data.dat","rb")
    data=pickle.load(f)
    items=data["items"]
    f.close()
    print "\t\t\t\t\tMODIFY PRODUCT QUANTITY\n"
    while 1:
        mod_idno=Error_BI("Enter the ID Number of the Product: ")
        print
        if mod_idno not in items.keys():
            print "Invalid ID Number. Please Enter Again."
        else:
            items[mod_idno].quantity=Error_BI("\nEnter New Quantity of Product: ")
            print "Quantity of the Product is changed to",items[mod_idno].quantity,"\n"
            break
    f=open("Supermarket Data.dat","wb")                    
    pickle.dump(data,f)
    f.close()
    
def mod_costprice():                                #Modify Product Cost Price
    print "===================================================================================================="
    f=open("Supermarket Data.dat","rb")
    data=pickle.load(f)
    items=data["items"]
    f.close()
    print "\t\t\t\t\tMODIFY COST PRICE\n"
    while 1:
        mod_idno=Error_BI("Enter the ID Number of the Product: ")
        print
        if mod_idno not in items.keys():
            print "Invalid ID Number. Please Enter Again."
        else:
            while True:
                try:
                    items[mod_idno].cp=input("\nEnter New Cost Price of Product: ")
                    print "Cost Price of the Product is changed to AED",items[mod_idno].cp,"\n"
                except:
                    print "'No Input/String Input Error' has occured. Please Enter the Cost Price again."
                else:
                    break
            break
    items[mod_idno].sp=float(items[mod_idno].cp)*(100.0+items[mod_idno].prof_perc)/100.0
    print "The New Selling Price is AED",items[mod_idno].sp
    f=open("Supermarket Data.dat","wb")                    
    pickle.dump(data,f)
    f.close()
    
def mod_profitpercent():                            #Modify Product Profit Percent
    print "===================================================================================================="
    f=open("Supermarket Data.dat","rb")
    data=pickle.load(f)
    items=data["items"]
    f.close()
    print "\t\t\t\t\tMODIFY PROFIT PERCENT\n"
    while 1:
        mod_idno=Error_BI("Enter the ID Number of the Product: ")
        print
        if mod_idno not in items.keys():
            print "Invalid ID Number. Please Enter Again."
        else:
            while True:
                try:
                    items[mod_idno].prof_perc=input("\nEnter New Profit Percent of Product: ")
                    print "Profit Percent of the Product is changed to",items[mod_idno].prof_perc,"%\n"
                except:
                    print "'No Input/String Input Error' has occured. Please Enter the New Profit Percent again."
                else:
                    break                    
            break
    items[mod_idno].sp=float(items[mod_idno].cp)*(100.0+items[mod_idno].prof_perc)/100.0
    print "The New Selling Price is AED",items[mod_idno].sp
    f=open("Supermarket Data.dat","wb")                    
    pickle.dump(data,f)
    f.close()
    
def displayproductlist():                           #Displaying Product List for Admins
    print "===================================================================================================="
    f=open("Supermarket Data.dat","rb")
    data=pickle.load(f)
    items=data["items"]
    f.close()
    print ("\n"+" "*45+"PRODUCT LIST")
    idnos=items.keys()
    info=items.values()
    print "\n====================================================================================================\n"
    if len(items)>0:
        print ("ID Number   "+"Name"+" "*19+"Quantity   "+"Cost Price(AED)    "+"Profit(%)    "+"Selling Price(AED)\n")
    for i in range(len(items)):
        print str(idnos[i])+" "*8+str(info[i].name)+" "*(23-len(str(info[i].name)))+str(info[i].quantity)+" "*(11-len(str(info[i].quantity)))+str(info[i].cp)+" "*(19-len(str(info[i].cp)))+str(info[i].prof_perc)+" "*(13-len(str(info[i].prof_perc)))+str(info[i].sp)
        if i==len(items)-1:
            break
    else:
        print "No Items available to Display."
    print "\n====================================================================================================\n"
    
def buyproduct():                                   #Buying a Product
    print "===================================================================================================="
    f=open("Supermarket Data.dat","rb")
    data=pickle.load(f)
    items=data["items"]
    sales=data["sales"]
    profit=data["prof"]
    f.close()
    amount=len(items)
    n=amount+1
    while n>amount:
        n=Error_BI("Enter Number of Products you would like to buy: ")         #Error Handling
        if n>amount:
            print "Error : Value Entered is more than Available Products. Please try again."
    i=0
    bill={}        #Stores Quantity of each item purchased
    billtotal=0
    while i<n:
        idnos=items.keys()
        idno=0
        while idno not in idnos:
            idno=Error_BI("Enter ID Number of the Product you would like to Buy: ")
            if idno not in idnos:
                print "Invalid ID Number."
        else:
            quan=Error_BI("Quantity: ")
            if quan<=items[idno].quantity:
                bill[idno]=quan
                items[idno].quantity-=quan
                sales+=((items[idno].sp)*quan)
                profit+=(items[idno].sp-items[idno].cp)*quan   
                billtotal+=(items[idno].sp*quan)
                i+=1
            else: print "The Requested Item is not available in the Quantity you wanted. Only",items[idno].quantity,"Pieces are Available."

    print "\n====================================================================================================\n"
    print (" "*45+"BILL\n")
    billkey=bill.keys()
    print "Product Name"+" "*10+"Quantity        "+"Unit Price(AED)"+" "*11+"Total Price(AED)"
    for i in range(n):
        print str(items[billkey[i]].name)+" "*(22-len(str(items[billkey[i]].name)))+str(bill[billkey[i]])+" "*(16-len(str(bill[billkey[i]])))+str(items[billkey[i]].sp)+" "*(26-len(str(items[billkey[i]].sp)))+str(items[billkey[i]].sp*bill[billkey[i]])
    print "\n===================================================================================================="
    print " "*64+"TOTAL - AED "+str(billtotal)
    print "====================================================================================================\n"

    data["sales"]=sales
    data["prof"]=profit
    f=open("Supermarket Data.dat","wb")                    
    pickle.dump(data,f)
    f.close()

def profit():                          #Prints the Total Profit and Sales Obtained
    print "===================================================================================================="
    f=open("Supermarket Data.dat","rb")
    data=pickle.load(f)
    sales=data["sales"]
    profit=data["prof"]
    f.close()
    print "\n\t\t\t\t\tTOTAL PROFIT"
    print "\nThe Total Profit is: AED",profit
    print "The Total Sales is: AED",sales
    f=open("Supermarket Data.dat","wb")                    
    pickle.dump(data,f)
    f.close()

def add_admin():                            #Adds n Admin Accounts
    print "===================================================================================================="
    f=open("Supermarket Data.dat","rb")
    data=pickle.load(f)
    admin=data["adm"]
    io=data["io"]
    f.close()
    n=Error_BI("Enter Number of Admins to be Added: ")
    for i in range(n):
        adm=staff()
        adm.input("Admin")
        idno=1000+len(admin)+io["admin"]
        admin[idno]=adm
        print "New Admin ID - ",idno
        print
    f=open("Supermarket Data.dat","wb")                    
    pickle.dump(data,f)
    f.close()

def add_employee():                         #Adds n Employee Accounts
    print "===================================================================================================="
    f=open("Supermarket Data.dat","rb")
    data=pickle.load(f)
    employee=data["emp"]
    io=data["io"]
    f.close()
    n=Error_BI("Enter Number of Employee's to be Added: ")
    for i in range(n):
        idno=2000+len(employee)+io["employee"]
        emp=staff()
        emp.input("Employee")
        employee[idno]=emp
        print "New Employee ID - ",idno
        print
    f=open("Supermarket Data.dat","wb")                    
    pickle.dump(data,f)
    f.close()
def del_admin():                            #Deletes n Admin Accounts
    print "\n====================================================================================================\n"
    f=open("Supermarket Data.dat","rb")
    data=pickle.load(f)
    admin=data["adm"]
    io=data["io"]
    f.close()
    print "\t\t\t\t\tDELETE ADMIN"
    amount=len(admin)-1
    n=amount+1
    while n>amount:
        n=Error_BI("Enter Number of Admin Accounts to be Deleted: ")         #Error Handling
        if n>amount:
            print "Error : Value Entered is more than Available Admin Accounts. Please try again."
    k=1
    while k<=n:
        admin_id=Error_BI("\nEnter Admin ID: ")
        admin.keys().remove(1000)
        if admin_id not in admin.keys():
            print "Invalid ID Number. Please Enter Again."
        else:
            print "The Admin,",admin[admin_id].name,"has been Deleted."
            del admin[admin_id]
            io["admin"]+=1
            k+=1
    f=open("Supermarket Data.dat","wb")                    
    pickle.dump(data,f)
    f.close()

def del_emp():                              #Deletes n Employee Accounts
    print "\n====================================================================================================\n"
    f=open("Supermarket Data.dat","rb")
    data=pickle.load(f)
    employee=data["emp"]
    io=data["io"]
    f.close()
    print "\t\t\t\t\tDELETE EMPLOYEE"
    amount=len(employee)-1
    n=amount+1
    while n>amount:
        n=Error_BI("Enter Number of Employee Accounts to be Deleted: ")         #Error Handling
        if n>amount:
            print "Error : Value Entered is more than Available Employee Accounts. Please try again."
    k=1
    while k<=n:
        emp_id=Error_BI("\nEnter Employee ID: ")
        employee.keys().remove(2000)
        if emp_id not in employee.keys():
            print "Invalid ID Number. Please Enter Again."
        else:
            print "The Employee,",employee[emp_id].name,"has been Deleted."
            del employee[emp_id]
            io["employee"]+=1
            k+=1
    f=open("Supermarket Data.dat","wb")                    
    pickle.dump(data,f)
    f.close()

def mod_mob_no_admin():
    print "\n====================================================================================================\n"
    f=open("Supermarket Data.dat","rb")
    data=pickle.load(f)
    admin=data["adm"]
    f.close()
    print "\t\t\t\t\tMODIFY MOBILE NUMBER - ADMIN"
    while True:
        admin_id=Error_BI("\nEnter Admin ID: ")
        admin.keys().remove(1000)
        if admin_id not in admin.keys():
            print "Invalid ID Number. Please Enter Again."
        else:
            mob=raw_input("Enter the New Mobile Number : ")
            admin[admin_id].mob_num=mob
            print "Mobile Number Changed to : ",mob
            break
    f=open("Supermarket Data.dat","wb")                    
    pickle.dump(data,f)
    f.close()

def mod_mob_no_emp():
    print "\n====================================================================================================\n"
    f=open("Supermarket Data.dat","rb")
    data=pickle.load(f)
    employee=data["emp"]
    f.close()
    print "\t\t\t\t\tMODIFY MOBILE NUMBER - EMPLOYEE"
    while True:
        emp_id=Error_BI("\nEnter Employee ID: ")
        employee.keys().remove(2000)
        if emp_id not in employee.keys():
            print "Invalid ID Number. Please Enter Again."
        else:
            mob=raw_input("Enter the New Mobile Number : ")
            employee[emp_id].mob_num=mob
            print "Mobile Number Changed to : ",mob
            break
    
    f=open("Supermarket Data.dat","wb")                    
    pickle.dump(data,f)
    f.close()

def change_pwd():                             #Change Password
    print "\n====================================================================================================\n"
    f=open("Supermarket Data.dat","rb")
    data=pickle.load(f)
    admin=data["adm"]
    employee=data["emp"]
    f.close()
    print "\t\t\t\t\tCHANGE PASSWORD\n"
    while True:                                       
        idno=Error_BI("Enter your Admin/Employee ID Number - ")     #User ID : Works for both, Employee's as well as Admins
        password=raw_input("Enter your Password - ")             #Password
        admin_id=admin.keys()
        admin_id.remove(1000)
        employee_id=employee.keys()
        employee_id.remove(2000)
        if idno in admin_id:
            if admin[idno].pwd==password:
                new_pwd=raw_input("Enter your new password : ")
                admin[idno].pwd=new_pwd
                print "Password Changed"
                break
            else:
                print "\nIncorrect Password, Try Again.\n"
                continue
        elif idno in employee_id:
            if employee[idno].pwd==password:
                new_pwd=raw_input("Enter your new password : ")
                employee[idno].pwd=new_pwd
                print "Password Changed"
                break
            else:
                print "\nIncorrect Password, Try Again.\n"
                continue
        else:
            print "Invalid User ID. The given User ID does not exist. Try Again.\n"
    f=open("Supermarket Data.dat","wb")                    
    pickle.dump(data,f)
    f.close()

def displ_admin():                          #Displays All Admin Details
    print "\n====================================================================================================\n"
    f=open("Supermarket Data.dat","rb")
    data=pickle.load(f)
    admin=data["adm"]
    f.close()
    print " "*45+"DISPLAY ADMINS"
    idnos_admin=admin.keys()
    idnos_admin.remove(1000)
    info_admin=admin.values()
    info_admin.remove(admin[1000])
    print "\n====================================================================================================\n"
    if len(idnos_admin)>0:
        print "Admin ID      "+"Name"+" "*20+"Mobile Number"
    for i in range(len(idnos_admin)):
        print str(idnos_admin[i])+" "*10+str(info_admin[i].name)+" "*(24-len(info_admin[i].name))+str(info_admin[i].mob_num)
        if i==(len(idnos_admin)-1):
            break
    else:
        print "No Admin Accounts are Available to Display."
    print "\n====================================================================================================\n"

def displ_emp():                            #Displays All Employee Details
    print "\n====================================================================================================\n"
    f=open("Supermarket Data.dat","rb")
    data=pickle.load(f)
    employee=data["emp"]
    f.close()
    print " "*45+"DISPLAY EMPLOYEE"
    idnos_employee=employee.keys()
    idnos_employee.remove(2000)
    info_employee=employee.values()
    info_employee.remove(employee[2000])
    print "\n====================================================================================================\n"
    if len(idnos_employee)>0:
        print "Employee ID      "+"Name"+" "*20+"Mobile Number"
    for i in range(len(idnos_employee)):
        print str(idnos_employee[i])+" "*13+str(info_employee[i].name)+" "*(24-len(info_employee[i].name))+str(info_employee[i].mob_num)
        if i==(len(idnos_employee)-1):
            break
    else:
        print "No Employee Accounts are Available to Display."
    print "\n====================================================================================================\n"
    
def displ_menu_emp():                       #Product List for Employees 
    print "===================================================================================================="
    f=open("Supermarket Data.dat","rb")
    data=pickle.load(f)
    items=data["items"]     
    f.close()
    print" "*45+"PRODUCT LIST"
    idnos=items.keys()
    info=items.values()
    print "\n====================================================================================================\n"
    if len(items)>0:
        print "ID Number       "+"Name"+" "*20+"Quantity"+" "*5+"Selling Price(AED)\n"
    for i in range(len(items)):
        print str(idnos[i])+" "*12+str(info[i].name)+" "*(24-len(str(info[i].name)))+str(info[i].quantity)+" "*(13-len(str(info[i].quantity)))+str(info[i].sp)
        if i==len(items)-1:
            break
    else:
        print "No Items available to Display."
    print "\n====================================================================================================\n"
    
def signout():                              #Sign Out From Account
    print "===================================================================================================="
    print "\t\t\t\t\t-SIGNED OUT-"
    cont=raw_input("\t\t Enter 'Yes' if you want to login to another Domain Account \n\t\t\t\tOr Enter 'No' to Exit.\nEnter Choice (Note: Not Case Sensitive): ")
    cont=cont.lstrip()
    cont=cont.rstrip()
    if cont.lower()=="yes":
        login()
    else:
        exit()    

def menudisplay_emp():
    print "===================================================================================================="
    print "\t\t\t 1) Buy Product"
    print "\t\t\t 2) Display all Products"                                  #MAIN MENU FOR EMPLOYEES
    print "\t\t\t 3) Signout"
    print "\t\t\t 4) Exit Program"
    print "===================================================================================================="
    ch=0
    while ch!=1 and ch!=2 and ch!=3 and ch!=4:
        ch=int(Error_BI("\t\t\t Enter your Choice(1-4): "))                    #INCORRECT INPUT DATA HANDLING
        if ch>4 or ch<1:
            print "Incorrect Choice, Enter the Correct Choice."
    else:
        if ch==1:
            buyproduct()
        elif ch==2:
            displ_menu_emp()
        elif ch==3:
            signout()
        elif ch==4:
            exit()
    cont=raw_input("\t\t\t\t Enter 'Yes' if you want to Continue to the Main Menu \n\t\t\t\tOr Enter 'No' to Exit.\nEnter Choice (Note: Not Case Sensitive): ")
    cont=cont.lstrip()
    cont=cont.rstrip()
    if cont.lower()!="no":
        menudisplay_emp()
    else:
        exit()
    
def menudisplay_admin():
    print "===================================================================================================="
    print "\t\t\t 1)  Add/Delete Existing Product"
    print "\t\t\t 2)  Modify Product Details"                        #MAIN MENU FOR ADMINS
    print "\t\t\t 3)  Display all Products"
    print "\t\t\t 4)  Print Current Sales Data"
    print "\t\t\t 5)  Add an Admin / Employee"
    print "\t\t\t 6)  Delete an Admin / Employee"
    print "\t\t\t 7)  Modify Mobile Number for an Admin / Employee"
    print "\t\t\t 8)  Change Password"
    print "\t\t\t 9)  Display Admin / Employee list"
    print "\t\t\t 10) Sign Out"
    print "\t\t\t 11) Exit"
    print "===================================================================================================="
    ch=0
    while ch>11 or ch<1:
        ch=int(Error_BI("\t\t\t Enter your Choice(1-11): "))                    #INCORRECT INPUT DATA HANDLING
        if ch>11 or ch<1:
            print"Incorrect Choice, Enter the Correct Choice."
    else:
        if ch==1:
            while 1:
                print "===================================================================================================="
                print "\t\t\t\t 1) Add Product"
                print "\t\t\t\t 2) Delete Product"
                print "\t\t\t\t 3) Return to Menu"
                ch1=0
                while ch1>3 or ch1<1:
                    ch1=int(Error_BI("Enter your Sub Choice(1-3): "))
                    if ch1>3 or ch1<1:
                        print "Incorrect Choice, Enter the Correct Choice."
                if ch1==1:
                    addproduct()
                elif ch1==2:
                    deleteproduct()
                elif ch1==3:
                    menudisplay_admin()
                cont=raw_input("\t\t\t\t Enter 'Yes' if you want to continue \n\t\t\t\tor Enter 'No' to return to Main Menu \n\t\t\t\tor Enter 'Exit' to exit the Program.\nEnter Choice (Note: Not Case Sensitive): ")
                cont=cont.lstrip()
                cont=cont.rstrip()
                if cont.lower()=="yes":
                    continue
                elif cont.lower()=="exit":
                    exit()
                else: menudisplay_admin()
                
        elif ch==2:
            while 1:
                print "===================================================================================================="
                print "\t\t\t\t 1) Modify Product Name"
                print "\t\t\t\t 2) Modify Product Quantity"
                print "\t\t\t\t 3) Modify Cost Price"
                print "\t\t\t\t 4) Modify Profit Percent"
                print "\t\t\t\t 5) Return to Menu"
                ch2=0
                while ch2>5 or ch2<1:
                    ch2=int(Error_BI("Enter your Sub Choice(1-5): "))
                    if ch2>5 or ch2<1:
                        print "\t\t\t\tIncorrect Choice, Enter the Correct Choice (1-5)."
                if ch2==1:
                    mod_productname()
                elif ch2==2:
                    mod_productquantity()
                elif ch2==3:
                    mod_costprice()
                elif ch2==4:
                    mod_profitpercent()
                elif ch2==5:
                    menudisplay_admin()                                          
                cont=raw_input("\t\t\t\t Enter 'Yes' if you want to continue \n\t\t\t\tor Enter 'No' to return to Main Menu \n\t\t\t\tor Enter 'Exit' to exit the Program.\nEnter Choice (Note: Not Case Sensitive): ")
                cont=cont.lstrip()
                cont=cont.rstrip()
                if cont.lower()=="yes":
                    continue
                elif cont.lower()=="exit":
                    exit()
                else: menudisplay_admin()
        elif ch==3:
            displayproductlist()
        elif ch==4:
            profit()
        elif ch==5:
            while 1:                
                choice=""
                while choice.lower()!="admin" and choice.lower()!="employee":
                    choice=raw_input("Add an 'Admin' or 'Employee'? \nNote:Not Case Sensitive.\nEnter your Choice:")
                    choice=choice.rstrip()
                    choice=choice.lstrip()
                    if choice.lower()!="admin" and choice.lower()!="employee":
                        print "You have entered the Wrong Choice. Please Enter Either 'Admin' or 'Employee' only."
                if choice.lower()=="admin":
                    add_admin()
                elif choice.lower()=="employee":
                    add_employee()
                cont=raw_input("\t\t\t\t Enter 'Yes' if you want to continue \n\t\t\t\tor Enter 'No' to return to Main Menu \n\t\t\t\tor Enter 'Exit' to exit the Program.\nEnter Choice (Note: Not Case Sensitive): ")
                cont=cont.lstrip()
                cont=cont.rstrip()
                if cont.lower()=="yes":
                    continue
                elif cont.lower()=="exit":
                    exit()
                else: menudisplay_admin()
        elif ch==6:
            while 1:                
                choice=""
                while choice.lower()!="admin" and choice.lower()!="employee":
                    choice=raw_input("Delete an 'Admin' or 'Employee'? \nNote:Not Case Sensitive.\nEnter your Choice:")
                    choice=choice.rstrip()
                    choice=choice.lstrip()
                    if choice.lower()!="admin" and choice.lower()!="employee":
                        print "You have entered the Wrong Choice. Please Enter Either 'Admin' or 'Employee' only."
                if choice.lower()=="admin":
                    del_admin()
                elif choice.lower()=="employee":
                    del_emp()
                cont=raw_input("\t\t\t\t Enter 'Yes' if you want to continue \n\t\t\t\tor Enter 'No' to return to Main Menu \n\t\t\t\tor Enter 'Exit' to exit the Program.\nEnter Choice (Note: Not Case Sensitive): ")
                cont=cont.lstrip()
                cont=cont.rstrip()
                if cont.lower()=="yes":
                    continue
                elif cont.lower()=="exit":
                    exit()
                else: menudisplay_admin()
        elif ch==7:
            while 1:                
                choice=""
                while choice.lower()!="admin" and choice.lower()!="employee":
                    choice=raw_input("Modify Mobile Number for an 'Admin' or 'Employee'? \nNote:Not Case Sensitive.\nEnter your Choice:")
                    choice=choice.rstrip()
                    choice=choice.lstrip()
                    if choice.lower()!="admin" and choice.lower()!="employee":
                        print "You have entered the Wrong Choice. Please Enter Either 'Admin' or 'Employee' only."
                if choice.lower()=="admin":
                    mod_mob_no_admin()
                elif choice.lower()=="employee":
                    mod_mob_no_emp()
                cont=raw_input("\t\t\t\t Enter 'Yes' if you want to continue \n\t\t\t\tor Enter 'No' to return to Main Menu \n\t\t\t\tor Enter 'Exit' to exit the Program.\nEnter Choice (Note: Not Case Sensitive): ")
                cont=cont.lstrip()
                cont=cont.rstrip()
                if cont.lower()=="yes":
                    continue
                elif cont.lower()=="exit":
                    exit()
                else: menudisplay_admin()
        elif ch==8:
            change_pwd()
        elif ch==9:
            while 1:                
                choice=""
                while choice.lower()!="admin" and choice.lower()!="employee":
                    choice=raw_input("Display 'Admin' or 'Employee' List? \nNote:Not Case Sensitive.\nEnter your Choice:")
                    choice=choice.rstrip()
                    choice=choice.lstrip()
                    if choice.lower()!="admin" and choice.lower()!="employee":
                        print "You have entered the Wrong Choice. Please Enter Either 'Admin' or 'Employee' only."
                if choice.lower()=="admin":
                    displ_admin()
                elif choice.lower()=="employee":
                    displ_emp()
                cont=raw_input("\t\t\t\t Enter 'Yes' if you want to continue \n\t\t\t\tor Enter 'No' to return to Main Menu \n\t\t\t\tor Enter 'Exit' to exit the Program.\nEnter Choice (Note: Not Case Sensitive): ")
                cont=cont.lstrip()
                cont=cont.rstrip()
                if cont.lower()=="yes":
                    continue
                elif cont.lower()=="exit":
                    exit()
                else: menudisplay_admin()
        elif ch==10:
            signout()
        elif ch==11:
            exit()
        cont=raw_input("\t\t\t\t Enter 'Yes' if you want to Continue to \n\t\t\t\t the Main Menu Or Enter 'No' to Exit.\n\nEnter Choice (Note: Not Case Sensitive): ")
        cont=cont.lstrip()
        cont=cont.rstrip()
        if cont.lower()!="no":
            menudisplay_admin()
        else:
            exit()
            
def main():
    print "===================================================================================================="
    print"\t\t\t\t\tOur Own Supermarket"                            #Main Introduction To Program
    print "Welcome to Our Own Supermarket. \nKindly Select Initial Program Mode: "
    print "\t1) Initial Setup       : Select this mode if this is your first time with the program."
    print "\t2) Normal Running Mode : Select this mode if this isn't your first time with the program."
    ch=0
    while ch!=1 and ch!=2:
        ch=Error_BI("\tEnter Choice (1-2) [Default Option = 1] : ")
        if ch==2:
            try:
                f=open("Supermarket Data.dat","rb")
            except:
                print "Error. You have entered an inappropriate setup mode. The file \"Supermarket Data.dat\" does not exist. Please Try Again."
                main()
            else: 
                print "Normal Running Mode Initiated."
        else:
            setup()
            print "Setup Complete."
            break
    login()
main()


                                                                                                                      
