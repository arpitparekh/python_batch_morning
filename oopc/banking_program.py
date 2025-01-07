class Banking:

  def __init__(self,name,location,account_type,balance):
    self.name = name
    self.location = location
    self.account_type = account_type
    self.balance = balance

  def displayData(self):
    print("Name:",self.name)
    print("Location:",self.location)
    print("Account Type:",self.account_type)
    print("Balance:",self.balance)

  def withdraw(self,money):
    self.balance -= money
    print("Withdrawal Successfull")

  def deposit(self,money):
    self.balance += money
    print("Deposit Successfull")

  def __str__(self):
    return f"Name: {self.name}\nLocation: {self.location}\nAccount Type: {self.account_type}\nBalance: {self.balance}"

print("Please Enter Bank Account Details:")
print("Please Enter No of Accounts:")
n = int(input())   # 5

bank_account_list = []  # object list
for i in range(n):
  print("Enter Details of Account-----------------",i+1)
  name = input("Enter Name:")
  location = input("Enter Location:")
  account_type = input("Enter Account Type:")
  balance = int(input("Enter Balance:"))
  b = Banking(name,location,account_type,balance)
  bank_account_list.append(b)

print("Please Enter Bank Name Withdraw or Deposit:")
bank_name = input("Please Enter Bank Name:")
print("Please Enter  1 for Withdraw or 2 for Deposit:")
option = int(input())
print("Please Enter Amount:")
amount = int(input())

for bank in bank_account_list:
  if bank.name == bank_name:
    if(option == 1):
      # withdraw
      bank.withdraw(amount)

    elif(option == 2):
      # deposit
      bank.deposit(amount)
    else:
      print("Invalid Option")

for bank in bank_account_list:
    bank.displayData()


