import os
import sqlite3


class Bank:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance
    


class Customer(Bank):
    def __init__(self, account_no, name, balance, withdrawal, deposit):
        super().__init__(account_no, name, balance)
        self.withdrawal = withdrawal
        self.deposit_amount = deposit

    def process(self):
        if self.withdrawal==None:
            self.withdrawal=0
        if self.deposit_amount==None:
            self.deposit_amount=0
        
        self.balance = self.balance - self.withdrawal + self.deposit_amount

        return (f"\tWithdrawn:{self.withdrawal}\n\tDeposite:{self.deposit_amount}\n\tBalance:{self.balance}")
    

    
class Database(Customer):
    def __init__(self, account_no, name, balance, withdrawal, deposit):
        super().__init__(account_no, name, balance, withdrawal, deposit)
    
    def create_table(self):
        con = sqlite3.connect('bank.db')
        c = con.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Accounts'")
        table_exists = c.fetchone()
        if not table_exists:
            c.execute("""CREATE TABLE Accounts(
                    account_no text,
                    name text,
                    balance real,
                    withdrawal real,
                    deposit real
                    )""")
            con.commit()
        con.close()

    def add_data(self):
        con = sqlite3.connect('bank.db')
        c = con.cursor()
        account_no = self.account_no
        c.execute("SELECT * FROM Accounts WHERE account_no=?", (account_no,))
        items = c.fetchall()
        if not items:
            c.execute("INSERT INTO Accounts VALUES (?,?,?,?,?)", (self.account_no, self.name, self.balance, self.withdrawal, self.deposit_amount))
            con.commit()
        con.close()
    
    def search_data(self):
        con = sqlite3.connect('bank.db')
        c = con.cursor()
        account_no = self.account_no
        c.execute("SELECT * FROM Accounts WHERE account_no=?", (account_no,))
        searchlist = ["Account Number:", "Name:", "Balance:","Withdrawal:", "Deposit:"]
        counter = 0
        items = c.fetchall()
        if not items:
            print("No data found for the given account number.")
            return 0
        else:
            return 1
        

    def print_singular_data(self):
        con = sqlite3.connect('bank.db')
        c = con.cursor()
        account_no = self.account_no
        c.execute("SELECT * FROM Accounts WHERE account_no=?", (account_no,))
        searchlist = ["Account Number:", "Name:", "Balance:","Withdrawal:", "Deposit:"]
        counter = 0
        items = c.fetchall()
        if not items:
            print("No data found for the given account number.")
        else:
            bank_info = items[0]
            print(f"\n{'-'*20}\nRecord\n{'-'*20}")
            for item in bank_info:
                print(searchlist[counter], item)
                counter += 1
            print("\n")
        con.close()
    
    def duplicate_data(self):
        con = sqlite3.connect('bank.db')
        c = con.cursor()
        account_no = self.account_no
        c.execute("SELECT * FROM Accounts WHERE account_no=?", (account_no,))
        if c.fetchall():
            print("\nThe account number already exists\n")
            return 1
        con.close()
    
    def delete_data(self,search_data):
        if search_data!=0:
            con = sqlite3.connect('bank.db')
            c = con.cursor()
            account_no = self.account_no
            c.execute("DELETE FROM Accounts WHERE account_no=?", (account_no,))
            con.commit()
            print("Data deleted successfully.")
            con.close()
    
    def update_data(self,search_data):
        if search_data!=0:
            con = sqlite3.connect('bank.db')
            c = con.cursor()
            account_no = self.account_no
            c.execute("UPDATE Accounts SET balance=?, withdrawal=?, deposit=? WHERE account_no=?", (self.balance, self.withdrawal, self.deposit_amount, account_no))
            con.commit()
            print("Balance Updated Successfully.")
            con.close()
    
    def display_data(self):
        con = sqlite3.connect('bank.db')
        c = con.cursor()
        c.execute("SELECT * FROM Accounts")
        searchlist = ["Account Number:", "Name:", "Balance:","Withdrawal:", "Deposit:"]
        counter = 0
        items = c.fetchall()
        if not items:
            print("No data found.")
        else:
            for item in items:
                print(f"\n{'-'*20}\nRecord {counter+1}\n{'-'*20}")
                for i in range(5):
                    print(searchlist[i], item[i])
                counter += 1
        con.close()
    
    def close(self):
        os.remove('bank.db')
        print("Database deleted successfully.")



class Frontend:
    def __init__(self):
        pass

    def handle_choice(self):
        choice = '0'
        while choice != '3':
            print("1)Admin\n2)Customer\n3)Exit")
            choice = input("Enter your choice:")
            if choice == '1':
                self.admin()
            elif choice == '2':
                self.customer_end()
            elif choice == '3':
                print("Exiting...")
            else:
                print("Invalid choice")

    def admin(self):
        choice = '0'
        while choice != '4':
            print("1)Search Account:\n2)Display All Accounts:\n3)Delete Database:\n4)Exit:")
            choice = input("Enter your choice:")
            if choice == '1':
                acc_no = input("Enter Account Number:")
                c1 = Database(acc_no, None, None, None, None)
                c1.print_singular_data()
            elif choice == '2':
                c1 = Database(None, None, None, None, None)
                c1.display_data()
            elif choice == '3':
                c1 = Database(None, None, None, None, None)
                c1.close()

    def customer_end(self):
        choice = '0'
        while choice != '5':
            print("1. Add Account")
            print("2. Delete Account")
            print("3. Update Account")
            print("4. Withdraw/Deposit/Both")
            print("5. Exit")
            choice = input("Enter your choice:")

            if choice == '1':
                acc_no = input("Enter Account Number:")
                name = input("Enter Name:")
                bal = float(input("Enter Balance:"))
                w = 0
                d = 0
                c1 = Database(acc_no, name, bal, w, d)
                c1.create_table()
                c1.add_data()

            elif choice == '2':
                acc_no = input("Enter Account Number:")
                c1 = Database(acc_no, None, None, None, None)
                c1.delete_data(c1.search_data())

            elif choice == '3':
                acc_no = input("Enter Account Number:")
                bal = float(input("Enter Balance:"))
                c1 = Database(acc_no, None, bal, None, None)
                c1.update_data(c1.search_data())

            elif choice == '4':
                con = sqlite3.connect('bank.db')
                c = con.cursor()
                acc_no = input("Enter Account Number:")
                c.execute("SELECT * FROM Accounts WHERE account_no=?", (acc_no,))
                items = c.fetchall()
                bal = items[0][2]
                choice=input("Do you want to withdraw,deposit or both? (w/d/b):")
                if choice=="w":
                    w=int(input("Enter the withdrawal amount:"))
                    d=0
                elif choice=="d":
                    d=int(input("Enter the deposit amount:"))
                    w=0
                elif choice=="b":
                    w=int(input("Enter the withdrawal amount:"))
                    d=int(input("Enter the deposit amount:"))
                else:
                    w=0
                    d=0
                c1 = Database(acc_no, None, bal, w, d)
                c1.process()
                c1.update_data(c1.search_data())
                c1.display_data()


def main():
    f = Frontend()
    f.handle_choice()

if __name__ == "__main__":
    main()


