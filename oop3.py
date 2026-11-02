# classes
# customer - names, emails, kra, Dob, gender
# BankAccount - Customers, acc_no, acc_type,balance


class Customer:
    def __init__(self, name: str, email: str, kra: str, dob: str, gender: str, address: str = "",
                 city: str = "", state: str = "", zip_code: str = "") -> None:
        self.names = name
        self.address = address
        self.email = email
        self.kra = kra
        self.dob = dob
        self.gender = gender

        self.city = city
        self.state = state
        self.zip_code = zip_code
    def show_details(self):
        print(f"Name: {self.names} and KRA PIN: {self.kra}")
        # return f"Name: {self.names} and KRA PIN: {self.kra}"
    def __str__(self):
        return f"{self.names} {self.gender} {self.address} {self.city} {self.state} {self.zip_code}"
class Account:
    def __init__(self, owner:Customer, acc_no:str, acc_type:str, balance:float, gender:str = ""):
        self.owner = owner
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.gender = gender or owner.gender
        self.balance = balance
    def print_details(self):
        self.owner.show_details()
        print(f"Account No: {self.acc_no}")
        print(f"Account Type: {self.acc_type}")
        print(f"Gender: {self.gender}")
        print(f"Balance: {self.balance}")
        print("**************************")
    def deposit(self, amount:float):
        if amount <= 0:
            print("Amount must be positive")
        else:
            self.balance += amount

    def withdraw(self, amount:float):
        if amount <= 0:
            print("Amount must be positive")
        elif amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def __str__(self) -> str:
        return f"{self.balance} {self.acc_type} {self.gender} {self.acc_no}"



owner1 = Customer("Jim Jong", "jj@test.com", "KRA001", "31-8-2000", "M")
owner2 = Customer("Yuang Ti", "yt@test.com", "KRA002", "19-11-1995", "F")

acc1 = Account(owner1, "98765", "current", 80_000)
acc2 = Account(owner1, "98766", "savings", 1_000_000.50)
acc3 = Account(owner2, "98767", "savings", 71_000.00)

# print(owner1.dob) #private
# print(owner1.show_details())

acc1.print_details()
acc1.deposit(11_000)
acc1.print_details()
acc1.withdraw(10_000)
acc1.print_details()

print(acc1.owner)