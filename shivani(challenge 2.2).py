class BankAccount:
  def __init__(self, account_no, account_holder_name, initial_balance):
      self.__account_no= account_no
      self.__account_holder_name= account_holder_name
      self.__account_balance= initial_balance
  def deposit (self, amount):
    if amount>0:
      self.__account_balance+= amount
      print("Deposited ₹{}. New Balance : ₹{}.". format(amount, self.__account_balance))
    else:
      print("Invalid deposit")
  def withdraw (self, amount):
    if amount>0 and amount<= self.__account_balance:
      self.__account_balance-= amount
      print("Withdrawal ₹{}. New Balance: ₹{}".format(amount, self.__account_balance))
    else:
      print("Invalid withdrawal or insufficient amount")
  def display_balance (self):
      print(" Account balance for {} Account #{}: ₹{}". format(self.__account_holder_name, self.__account_no, self.__account_balance ))
account= BankAccount(account_no = "192837465",
      account_holder_name="Shiva",  initial_balance=5000.0)
account. display_balance()
account. deposit (500.0)
account. withdraw(200.0)
account. withdraw(2000.0)
account. display_balance ()











