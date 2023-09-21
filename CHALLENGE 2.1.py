class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print(
          f"Deposited ${amount:.2f}. New balance: ${self.__account_balance:.2f}"
      )
    else:
      print("Invalid deposit amount. Amount must be greater than zero.")

  def withdraw(self, amount):
    if 0 < amount <= self.__account_balance:
      self.__account_balance -= amount
      print(
          f"Withdrew ${amount:.2f}. New balance: ${self.__account_balance:.2f}"
      )
    elif amount > self.__account_balance:
      print("Insufficient funds for withdrawal.")
    else:
      print("Invalid withdrawal amount. Amount must be greater than zero.")

  def display_balance(self):
    print(
        f"Account balance for {self.__account_holder_name}: ${self.__account_balance:.2f}"
    )


# Testing the BankAccount class
if __name__ == "__main__":
  # Create a new bank account
  my_account = BankAccount("178685", "SOBIKA", 1000.0)

  # Display the initial balance
  my_account.display_balance()

  # Deposit money into the account
  my_account.deposit(5080.0)

  # Withdraw money from the account
  my_account.withdraw(2900.0)

  # Attempt to withdraw more money than the account balance
  my_account.withdraw(150900.0)

  # Attempt to deposit a negative amount
  my_account.deposit(-1090.0)

  # Display the final balance
  my_account.display_balance()
