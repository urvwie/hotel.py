import mysql.connector as conn
mycon=conn.connect(host="localhost", user= "root", passwd="UMANGPAHUJA", database="hotel")

def loginas():
    print("^^^^^^^^^^^^^  WELCOME TO TAJ  PALACE  ^^^^^^^^^^^^^")
    
    print(" HOW MAY I HELP YOU...")

    print("         how will you like to log in ???    ") 
    
    print("           1. HOTEL MANAGER  ")
    
    print("           2. RECEPTIONIST   ")
          
    print("           3. GUEST          ")
                         
#<<<<<<<<<<<<<<<<<<<<<<<<< FOR MANAGER >>>>>>>>>>>>>>>>>>>>
                           
def staffrec():
    print("<<<<<<<<<<<<<<<<<<< STAFF RECORD>>>>>>>>>>>>>>>>>")

    print("         1.INSERT NEW EMPLOYEE DATA  ")
    
    print("         2.SEARCH EMPLOYEE DATA    ")
    
    print("         3.EDIT EMPLOYEE DATA    ")
    
    print("         4.REMOVE EMPLOYEE DATA   ")

    print("         5.EXIT       ")

#Function to insert employee data
def addemployee():
    cur=mycon.cursor()
    print("***************** Enter employee Data *****************")
    employeeID=int(input(" Enter employee id "))
    employeeNAME=input(" Enter employee Name  ")
    emp_phone=input(" Enter employee mobile no ")
    emp_adhar=input(" Enter adhaar no  ")
    DOB=input("  Enter DOB of employee ")
    qy="Insert into staff values(%s,%s,%s,%s,%s)"
    cur.execute(qy,[employeeID,employeeNAME,emp_phone,emp_adhar,DOB])
    print("***** DATA ADDED   *****")
    input("Press Enter to continue")
    mycon.commit()

#search employee
def find_emp():
    print("------------------ Search Employee Details by -------------")
    print("1. employee id")
    print("2. employee phone no")
    print("3. employee adhar no ")
    
def showbyID():
    cur=mycon.cursor()
    employeeID=input("Enter employee ID to search ")
    q="select * from staff where employeeID= %s"
    cur.execute(q,[employeeID])
    if cur.rowcount==1:
        print("****** NO RECORD FOUND *****")
    else:
        data=cur.fetchall()
        print(data)
    input("Press Enter To Continue......")


def showbyphone():
    cur=mycon.cursor()
    emp_phone=input(' Enter employee phone no to search ')
    q="select * from staff where emp_phone= %s"
    cur.execute(q,[emp_phone])
    if cur.rowcount==1:
        print("****** NO RECORD FOUND *****")
    else:
        data=cur.fetchall()
        print(data)
    input("Press Enter To Continue......")

def showbyadhar():
    cur=mycon.cursor()
    a=input(" Enter employee adhar No ")
    q="select * from staff where emp_adhar like '%s'"
    cur.execute(q,[a])
    if cur.rowcount==1:
        print("****** NO RECORD FOUND *****")
    else:
        data=cur.fetchall()
        print(data)
    input("Press Enter To Continue......")


#EDIT EMPLOYEE DATA():
def editemp():
    print("------------------ Edit Employee Details -------------")
    print("1. employee name")
    print("2. employee phone no")
    print("3. employee adhar no ")
    print("4. employee dob")
    cur=mycon.cursor()
    ch=int(input("Enter Your Choice 1-4 "))
    employeeID=input("EMPLOYEE Id to Edit")
    if ch==1:
        x=input("Enter employee name ")
        q="update staff set employeeNAME=%s where employeeID=%s"
    if ch==2:
        x=input("Enter employee phone no ")
        q="update staff set emp_phone=%s where employeeID=%s"
    if ch==3:
        x=input("Enter employee adhar no ")
        q="update staff set emp_adhar=%s where employeeID=%s"
    if ch==4:
        x=input("Enter emp dob yyyy-mm-dd ")
        q="update staff set DOB=%s where employeeID=%s"
    cur.execute(q,[x,employeeID])
    mycon.commit()
    print("Data Updadated")

#function to delete staff logs
def del_logs():
    cur=mycon.cursor()
    employeeID=int(input("Enter employee ID to delete "))
    q="Select * from staff where employeeID = %s "
    cur.execute(q,[employeeID])
    data=cur.fetchall()
    if cur.rowcount==0:
        print("Employee Data Not Found")
    else:
        q="delete from staff where employeeID = %s"
        cur.execute(q,[employeeID])
        mycon.commit()
        print("DATA Deleted")




#<<<<<<<<<<<<<<<<<<<<<<<< FOR RECEPTIONIST>>>>>>>>>>>>>>>>>>>>>>
                              
def guestDATA():
    print("HOW MAY I HELP YOU...")
    print("<<<<<<<<<<<<<<<<<<<<<< GUEST RECORDS >>>>>>>>>>>>>>>>")
    print("               1.INSERT GUEST DETAILS       ")
    print("               2.SEARCH FOR ROOM            ") 
    print("               3.ALLOCATING ROOM            ")     
    print("               4.SEARCH GUEST                ")
    print("               5.DELETE CUSTOMER LOGS       ")
    print("               6.EXIT                       ")

#Function to insert guest details
def insertguest():
    cur=mycon.cursor()
    print("***************** Enter guest Details *****************")
    roomno= int(input("       Enter guest room no "))
    name=input("       Enter guest Name  ")
    DOB=input("       Enter DOB of guest Name  ")
    mobile=input("       Enter guest mobile no ")
    adhaar= input("       Enter adhaar no  ")
    nationality=input("       Enter nationality of guest  ")
    status="available"
    qy="Insert into guest values(%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(qy,[roomno,name,DOB,mobile,adhaar,nationality,status])
    print("***** DATA ADDED   *****")
    input("Press Enter to continue")
    mycon.commit()

#search for room
def searchrno():
    cur=mycon.cursor()
    a=input("Enter room no to be searched ")
    q="select * from guest where roomno=%s "
    cur.execute(q,[a])
    if cur.rowcount==1:
        print("****** NO RECORD FOUND *****")
    else:
        data=cur.fetchall()
        print(data)
    input("Press Enter to continue")
    
#function to room booking
def booking():
    cur=mycon.cursor()
    roomno=int(input("Enter room no to book  "))
    q="select * from guest where roomno=%s "
    cur.execute(q,[roomno])
    cur.fetchall()
    if cur.rowcount==1:
        print("room is not available ")
    else:
        roomno=int(input("Enter room no to book  "))
        name=input("enter guest name whom to book room")
        dt=input("Enter Date of booking yyyy-mm-dd ")
        mobile=int(input("Enter guest mobile no "))
        adhaar= int(input("Enter adhaar no  "))
        nationality=input("Enter nationality of guest ")
        status=input("press enter to book")
        q="insert into guest values(%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(q,[roomno,name,dt,mobile,adhaar,nationality,"available"])
        mycon.commit()
        q="Update guest set status='booked' having roomno=%s"
        cur.execute(q,[roomno])
        mycon.commit()
        print("ROOM BOOKED..... ")
        input("Press Enter to Continue ")

#SEARCH GUEST
def search_guest():
        cur=mycon.cursor()
        name=input(" Enter guest Name ")
        q="select * from guest where name=%s "
        cur.execute(q,[name])
        if cur.rowcount==1:
            print("****** NO RECORD FOUND *****")
        else:
            data=cur.fetchall()
            print(data)
           
#function to delete staff logs
def del_guest():
    cur=mycon.cursor()
    roomno=int(input("Enter room no to delete "))
    name=input("Enter guest name to delete")
    q="Select * from guest where roomno= %s or name=%s"
    cur.execute(q,[roomno,name])
    data=cur.fetchall()
    if cur.rowcount==1:
        q="delete from guest where roomno= %s or name=%s "
        cur.execute(q,[roomno,name])
        mycon.commit()
        print("DATA Deleted")
    else:
        print("Guest Data Not Found")
        

#<<<<<<<<<<<<<<<<<<<<<<<< FOR GUEST >>>>>>>>>>>>>>>>>>>>>>>>>
def guest():
    print(" ENJOY YOUR DREAM VACATIONS AT TAJ :)")
    print("HOW MAY I HELP YOU...")
    print("<<<<<<<<<<<< DO YOU WANT TO..? >>>>>>>>>>>>>>>>>")
    print("      1. KNOW ABOUT TAJ      ")
    print("      2. KNOW ABOUT OUR STAFF ")
    print("      3. ONLINE BOOKING      ")
    print("      4. EXIT               ")

#FUNCTION TO KNOW ABOUT TAJ
def taj():
    print("Create memories for a lifetime.Watch your child’s face light up in the golden sunlight as you build your first dream sandcastle together on a Taj Holiday. Let time stand still as you travel across a lake to a 16th century white marble palace. Discover architectural marvels on a Champagne tour, as peacocks strut by your side. Enjoy the romance of living in a rainforest while you walk through the clouds. Feel a cold shiver run down your spine as you hear a tiger roar in the dense forest. Indulge in a wellness treatment, crafted using centuries of traditional knowledge. Set your soul free to embrace the sheer magic of experiencing timeless traditions. Realize cherished moments for a lifetime with every Taj Holiday, crafted with impeccable details just for you and your loved ones.")

    input("press enter to continue")

#function to online booking
def on_booking():
    cur=mycon.cursor()
    print("FOR BOOKING SINGLE BED TYPE ROOM INPUT ROOM NO 101-125")
    print("FOR BOOKING FAMILY HALL TYPE ROOM INPUT ROOM NO 2O1-225")
    print("FOR BOOKING COUPLE SUITE TYPE ROOM INPUT ROOM NO 301-310")
    print("FOR BOOKING PENTHOUSE SUITE TYPE ROOM INPUT ROOM NO 401-402")
    roomno=input("Enter room no you are wishing to be booked  ")
    q="select * from guest where roomno = %s "
    cur.execute(q,[roomno])
    cur.fetchall()
    if cur.rowcount==1:
        print("room not available....")
    else:
        roomno=input("Enter room no you want *kindly read the above instructions for type of room you want*")
        name=input("enter your name ")
        adhaar=input("enter your adhar no")
        mobile=input("enter your phone no")
        DOB=input("Enter Date of booking yyyy-mm-dd ")
        nationality=input("enter your nationality")
        status="null"
        q="insert into guest values(%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(q,[roomno,name,DOB,mobile,adhaar,nationality,status])
        mycon.commit()
        q="Update room set status='booked' having roomno=%s"
        cur.execute(q,[roomno])
        mycon.commit()
    input("press enter to continue")
while 1:
    loginas()
    ch=int(input("Enter your Choice "))
    if ch==1:
         staffrec()
         ch=int(input("Enter your choice"))
         if ch==1:
             addemployee()
         elif ch==2:
             find_emp()
             ch=int(input("Enter your choice"))
             if ch==1:
                 showbyID()
             elif ch==2:
                 showbyphone()
             elif ch==3:
                 showbyadhar()
             else:
                 break    
         elif ch==3:
             editemp()
         elif ch==4:
             del_logs()
         else:
             break
             
    elif ch==2:
        guestDATA()
        ch=int(input("Enter your choice"))
        if ch==1:
            insertguest()
        elif ch==2:
            searchrno()
        elif ch==3:
            booking()
        elif ch==4:
            search_guest()
        elif ch==5:
            del_guest()
        else:
            break
            
    else:
        ch==3
        guest()
        ch=int(input("Enter your choice"))
        if ch==1:
            taj()
        elif ch==2:
            find_emp()
            ch=int(input("Enter your choice"))
            if ch==1:
                showbyID()
            elif ch==2:
                showbyphone()
            elif ch==3:
                showbyadhar()
            else:
                break
        elif ch==3:
            on_booking()
        else:
            break 
    
    








        

