import sqlite3
import os

class Bank:
    
    def __init__(self,account_no,name,balance,user_id,password):
        self.account_no=account_no
        self.name=name
        self.balance=balance
        self.user_id=user_id
        self.password=password
con=sqlite3.connect('bank.db')                   #Creating Sqlite database within memory:
c=con.cursor()

def Check_AND_make_table():
    # Check if the table already exists
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Accounts'")
    table_exists = c.fetchone()

    if not table_exists:                              #Creating a Table:
        c.execute("""CREATE TABLE Accounts(
                account_no text,
                name text,
                balance real,
                user_id text,
                password text
                )""")
        con.commit()

def Adding_data():
    #Creating data and adding it to table:
    account_no=input("Account Number:")
    if Duplicate_data(account_no)==0:
        name=input("Name:")
        balance=float(input("Balance:"))
        user_id=input("User ID:")
        password=input("Password:")
        std=Bank(account_no,name,balance,user_id,password)
        c.execute("INSERT INTO Accounts VALUES (?,?,?,?,?)", (std.account_no,std.name,std.balance,std.user_id,std.password))
        con.commit()
    else:
        print("\nThe account number already exists\n")
        input()

def Search_data():
    # Searching data from the table:
    account_no = input("Enter Account Number to Search:")
    c.execute("SELECT * FROM Accounts WHERE account_no=?", (account_no,))
    searchlist = ["Account Number:", "Name:", "Balance:", "User ID:", "Password:"]
    counter=0
    items = c.fetchall()
    if not items:
        print("No data found for the given account number.")
    else:
        bank_info = items[0]
        for item in bank_info:
            print(searchlist[counter], item)
            counter+=1

def Duplicate_data(account_no):
    c.execute("SELECT * FROM Accounts WHERE account_no=?", (account_no,))
    if c.fetchall():
        return 1
    else:
        return 0

def Delete_data():
    account_no = input("Enter Account Number to Delete:")
    c.execute("DELETE FROM Accounts WHERE account_no=?", (account_no,))
    con.commit()
    print("Account Deleted Successfully.")

def Update_data():
    # Updating data to the table:
    account_no = input("Account Number:")
    if Duplicate_data(account_no)==0:
        print("No data found for the given account number.")
    else:
        balance = float(input("Update Balance:"))
        c.execute("UPDATE Accounts SET balance=? WHERE account_no=?", (balance,account_no))
        con.commit()
        print("Balance Updated Successfully.")

def Display_data():
    c.execute("SELECT * FROM Accounts")
    searchlist = ["Account Number:", "Name:", "Balance:", "User ID:", "Password:"]
    counter=0
    items = c.fetchall()
    if not items:
        print("No data found.")
    else:
        for bank_info in items:
            for item in bank_info:
                print(searchlist[counter], item)
                counter+=1
            print("\n")
    holder = input("\nPress Enter to continue...")


def admin():
    Check_AND_make_table()
    while True:
        #os.system('cls')
        print("\n1. Add Account\n2. Search Account\n3. Update Account\n4. Delete Account\n5. Display All Accounts\n6. Exit\n")       #Menu
        choice = input("Enter your choice:")
        if choice == '1':
            Adding_data()
        elif choice == '2':
            Search_data()
        elif choice == '3':
            Update_data()
        elif choice == '4':
            Delete_data()
        elif choice == '5':
            Display_data()
        elif choice == '6':
            break
        else:
            print("\nInvalid Choice\n")
            input()
    
if __name__ == "__main__":
    admin()
    con.close()



