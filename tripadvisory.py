#MYSQL-PYTHON Project
'''defining a function Trip_Advisory which allows the user to run the program as an admin as well as a user '''
def Trip_Advisory():#defining a function Trip_Advisory 
     print("Welcome to 'KERALA TOURISM!'-This Program highlights the Hotels Available for a visit to KERALA-THE OFFICIAL HOST TO GOD'S OWN COUNTRY")
     while True:
         print("Press 1 to Enter as an Admin")
         print("Press 2 to Enter as a User")
         print("Press 3 to To Finalise ")
         choice=int(input("Enter your Choice"))
         if choice==1: admin_menu()#to add,update,delete and display the contents of the table
         elif choice==2: user_menu()#calling a funtion user_menu() to review the hotels,analysing and choosing the hotels suits to the user
         elif choice==3:
             ask=input("Enter The Hotel Name you Have Chosen")
             print("Congratulations! Your Hotel has been Booked\n THANK YOU FOR CHOOSING OUR SERVICES:)")
             break
         else: print("Your Input is Wrong,Please Enter the correct choice")


def admin_menu():
        while True:
            print('1 to create a database')
            print("2 to Show databases")
            print("3 to Show Tables")
            print("4 to Show the structure of the table")
            print("5 to Add data to the table")
            print("6 to Update data")
            print("7 to Delete data from the table")
            print("8 to Display the data")
            print("9 to exit")
            choice = int(input("Enter your choice"))
            if choice == 1: create_database()
            elif choice == 2: show_databases()
            elif choice == 3: show_tables()
            elif choice == 4: show_structure()
            elif choice == 5: insert_data()#calling a function within a defined function
            elif choice == 6: update_data()
            elif choice == 7: delete_data()
            elif choice == 8: display_data()
            elif choice == 9: print("Exiting");break#exiting
            else: print("Your Input is Wrong,Please Enter the correct choice")


def user_menu():
    print("WELLDONE!!! Kerala is Good Choice to Plan a Trip")
    print("To Look For Hotels Please Enter the Following Details")#asking the user to enter the personal details     
    name=input("Enter Your Name:")
    no=int(input("Enter Your Mobile Number:"))
    eid=input("Enter Your Email Id")
    while True:
        print("Honour! You are requested to Press 1 for Checking and Comparing for hotels which fits your Budget ")
        print("You are Requested to Press 2 for Comparing the Ratings of Hotels in Kerala")
        print("Press 3 to exit")
        choice = int(input("Enter your choice"))
        if choice == 1: search1()
        elif choice == 2: search2()
        elif choice == 3: print("Exiting...,Thank You!!!");break
        else: print("Wrong Input!!!,Please Enter the correct choice")
            


def create_database():
     import mysql.connector
     try:
          db=mysql.connector.connect(host="localhost",user ="root",password="gs15@rrr")
          cursor=db.cursor()
          sql="create database tourism"
          cursor.execute(sql)
          print("Database created")
     except:
          print("Database Exists")
     cursor.close()
     db.close()



def show_databases():
     import mysql.connector
     try:
          db=mysql.connector.connect(host = "localhost",user = "root",password = "gs15@rrr",database="tourism")
          cursor=db.cursor()
          sql = "show databases"
          cursor.execute(sql)
          for x in cursor:
               print(x)
     except:
          print("Error in Connection")
     cursor.close()
     db.close()
          

def show_tables():
     import mysql.connector
     try:
          db=mysql.connector.connect(host = "localhost",user = "root",password = "gs15@rrr",database="tourism")
          cursor=db.cursor()
          cursor.execute("show tables")
          for x in cursor:
               print(x)
     except:
          print("Error in connection")
     cursor.close()
     db.close()


def show_structure():
     import mysql.connector
     try:
          db=mysql.connector.connect(host = "localhost",user = "root",password = "gs15@rrr",database="tourism")
          cursor=db.cursor()
          cursor.execute("desc kerala")
          for x in cursor:
               print(x)
     except:
          print("Error in connection")
     cursor.close()
     db.close()
               
          

def insert_data():
     import mysql.connector#importing mysql.connector
     try:
        db = mysql.connector.connect(host = "localhost", user = "root", password = "gs15@rrr",database='tourism')
        cursor = db.cursor()
        Hotelno=int(input("Enter the Hotel number"))
        Hotelname=input("Enter the name of Hotel")
        Ratings=int(input("Enter the ratings for hotel out of 10"))
        Offer=float(input("Enter the Percentage Discount on Visit"))
        Special=input("Enter the Speciality about hotel")
        Cost=int(input("Enter the cost of room per day"))
        sql = "insert into KERALA values(%s,%s,%s,%s,%s,%s)"
        val = (Hotelno,Hotelname,Ratings,Offer,Special,Cost)
        cursor.execute(sql,val)
        db.commit()
        print("Record added")
     except:
        db.rollback()
        print("Record not added")
     cursor.close()
     db.close()


def update_data():
    import mysql.connector
    try:
        db = mysql.connector.connect(host = "localhost", user = "root", password = "gs15@rrr", database = "tourism")
        cursor = db.cursor()
        no=int(input("Enter Hotelno"))
        cost= int(input("Enter Cost"))
        sql = "Update KERALA SET Cost = %s where Hotelno = %s" 
        val = (no,cost)
        cursor.execute(sql,val)
        db.commit()
        print(cursor.rowcount,"Congratulations! Record updated")#record updated
    except:
        db.rollback()
        print("Record not updated")
    cursor.close()
    db.close()    



def delete_data():
    import mysql.connector
    try:
        db = mysql.connector.connect(host = "localhost", user = "root", password = "gs15@rrr", database = "tourism")
        cursor = db.cursor()
        verdict= int(input("Enter Ratings"))
        sql = "Delete from KERALA where Ratings = %s"#sql command to delete the contents of the table
        cursor.execute(sql,(verdict,))
        db.commit()
        print(cursor.rowcount, " SUCCESS! Record deleted")
    except:
        db.rollback()
        print("Record not deleted")
    cursor.close()
    db.close() 



def display_data():
    import mysql.connector
    try:
        db = mysql.connector.connect(host = "localhost", user = "root",  password = "gs15@rrr", database = "tourism")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM KERALA ")
        results = cursor.fetchall()
        for x in results:
            print(x[0],x[1],x[2],x[3],x[4],x[5])#displaying all the data added 
    except:
        print("Error, unable to fetch data")
    cursor.close()
    db.close()



def search1():
    print("Welcome! Here you can check for the Hotels in your range")
    import mysql.connector
    try:
        db = mysql.connector.connect(host = "localhost", user = "root",  password = "gs15@rrr", database = "tourism")
        cursor = db.cursor()
        r1=int(input("Enter the Minimum Amount Above which you are Looking For"))
        r2=int(input("Enter the Maximum Amount Upto which you are Looking For"))
        sql="SELECT * FROM KERALA where Cost >= %s and Cost <= %s"
        val=(r1,r2)
        cursor.execute(sql,val)
        while True:
            row = cursor.fetchone()
            if row == None:
                break
            print(row)#displaying hotels between the range the user can afford
    except:
        print("Error, unable to fetch data")
    print("We Hope this was Helpful!,Have A Wonderful Visit :)") 
    cursor.close()
    db.close()



def search2():
    import mysql.connector
    try:
        db = mysql.connector.connect(host = "localhost", user = "root", password = "gs15@rrr", database = "tourism")
        cursor = db.cursor()
        cursor.execute("select * from KERALA order by Ratings desc")
        results = cursor.fetchall()
        for x in results:
            print(x[0],x[1],x[2],x[3],x[4],x[5])
    except: 
        print("Error, unable to sort")
    cursor.close()
    db.close()

Trip_Advisory()#calling the function Trip_Advisory

    
