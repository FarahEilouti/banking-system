from abc import ABC, abstractmethod

# In the README file we will find the overall description of this program idea (Banking System)

class BankAccount(ABC):
    '''
    In this class, we gather and define the first 3 functions we will use in the program 
    and will be displayed in the menu of options.
    '''
    
    def __init__(self, name, balance=0):
        '''
        constructor function 
        '''

        self.name = name
        self.balance = balance

# -------------------------------------------------
    def deposit(self, amount: int):
        '''
        function for the deposit operation 
        where a user adds amount of money to their original account,
        and the total balance increases.  
        '''

        amount = int(amount)
        self.balance += amount
        print(
            "\n amount deposited= " + str(amount) + "\nyour balance= " + str(self.balance)
        )
        return self.balance

# --------------------------------------------------
    def withdraw(self, amount: int):
        '''
        function for the deposit operation 
        where a user takes/pulls amount of money from their original account,
        and the total balance decreases
        '''

        amount = int(amount)
        if self.balance < amount:
            print("Not enough balance")
        else:
            print(
                "\namount withdrawn= "
                + str(amount)
                + "\nyour balance= "
                + str(self.balance)
            )
            self.balance -= amount
        return self.balance

# ----------------------------------------------------
    def calculate_income_tax(self, income):
        '''
        function to calculate 
        the tax amount upon the income salary in Jordanian Dinar currency
        '''

        if income <= 5000:
            tax = 0
        elif income <= 10000:
            tax = (income - 5000) * 0.05
        elif income <= 15000:
            tax = (income - 10000) * 0.10
        elif income <= 20000:
            tax = (income - 15000) * 0.15
        elif income <= 1000000:
            tax = (income - 20000) * 0.20
        else:
            tax = (income - 1000000) * 0.30
        print("your annual income tax in jordan is", tax, "JODS")
        return tax

# --------------------------------------------------
    def get_balance(self):
        '''
        To return the current amount of money in the account
        '''
        return self.balance

    def __str__(self) -> str:
        return "name: " + self.name + " - balance: " + str(self.balance)



# --------------------------------------------------
# --------------------------------------------------
class Saving_account(BankAccount):
    '''
    This class contains functions 
    which operate the saving account option, 
    in where we create an account only for savings and 
    use functionalities upon. (using super method)
    '''

    def __init__(self, name, balance=0):
        super().__init__(name, balance)

    def __str__(self) -> str:
        return super().__str__()

# --------------------------------------------------
# --------------------------------------------------
class Running_account(BankAccount):
    '''
    This class represents the functions of the main account
    which the user interacts and deals with
    '''

    def __init__(self, name, balance=0):
        super().__init__(name, balance)

    def __str__(self) -> str:
        return super().__str__()


def welcome():
    '''
    function for the Welcome message for the user 
    '''
    print(
        """
----------------------------------------
----------------------------------------
          Welcome To The Bank
****************************************
"""
    )


def services(account: BankAccount):
    '''
    function to display the main menu of options.
    '''
    while True:
        print(
            """
**************************************************
** Please enter the number of service you need: **
** #1. Withdraw                                 **
** #2. Deposit                                  **
** #3. Calculate Income Tax                     **
** #4. View Balance                             **
** #5. Create New Savings Account               ** 
** #6. Quit                                     **
**************************************************
            """
        )
        service = input("Enter service number from 1 to 6:\n>").lower()
        if service == "1":
            amount = int(input("please enter amount to withdraw: \n>"))
            account.withdraw(amount)
        elif service == "2":
            amount = int(input("please enter amount to deposit: \n>"))
            account.deposit(amount)
        elif service == "3":
            income = int(input("please enter your yearly income: \n>"))
            account.calculate_income_tax(income)
        elif service == "4":
            print("balance: " , account.get_balance())
        elif service == "5":
            new_account = Saving_account(account.name, account.balance)
            print("new account created " + new_account.__str__())
        elif service == "6":
            break
        else:
            print("Service Not Supported, please enter a valid number from the services 1 to 6.")


def goodbye():
    '''
    function to display the goodbye message for the user
    after they finish their operations
    '''
    print(
        """
****************************************
    thank you for using this service
            see you soon!!
----------------------------------------
----------------------------------------
"""
    )


if __name__ == "__main__":
    welcome()
    username = input("Please enter your name: \n >")
    balance = int(input("Please enter your balance: \n >"))
    user_account = Running_account(username, balance)
    services(user_account)
    goodbye()
