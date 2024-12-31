class Bank:
  name = ""
  accountNumber = 0
  type=""
  balance = 0

  def assignValues(self,name,accountNumber,type,balance):  # assign properties using function
    self.name = name
    self.accountNumber = accountNumber
    self.type = type
    self.balance = balance

  def display(self):    # print function to display properties
    print("Name:",self.name)
    print("Account Number:",self.accountNumber)
    print("Type:",self.type)
    print("Balance:",self.balance)

  def enjoy(self):
    print("Enjoy your life today 31st Dec")


b1 = Bank()
b1.assignValues("SBI",123456789,"savings",10000)
b1.display()


b2 = Bank()
b2.assignValues("HDFC",987654321,"current",20000)
b2.display()

b3 = Bank()
b3.enjoy()
