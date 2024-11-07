# Fa$t Banking Program
# This program includes a class "BankAcct" that holds various methods used to interact with the user's
# "bank account." The user can deposit, withdrawal, check their balance, and choose an interest
# rate for their bank account.


# module for organizing and displaying interest rates in a table
from texttable import Texttable

import time

global amount

# multi-use strings
DIV = "---" * 30
SM = "successful!"


class BankAcct:


    def __init__(self, name, a_num, amnt):


        # user account info
        self.name = name
        self.a_num = a_num

        # "monetary" float variables
        self.bal: float = 0
        self.amnt: float = amnt

        # interest rate variables
        self.int_rate : float = 0
        self.str_rate = ""
        self.str_bal = ""
        self.str_time = ""
        self.annual : float

        # user input for "option"
        self.opt = None

        # withdrawal variables
        self.insuff_funds = False


    # assigns value to interest rate based on user input
    def adj_int(self, opt):

        # if the user chose option one,
        if self.opt == 1:

            # then the int_rate is .002, and so on
            self.int_rate = .002

        elif self.opt == 2:

            self.int_rate = .005

        elif self.opt == 3:

            self.int_rate = .008

        elif self.opt == 4:

            self.int_rate = .04

        return self.int_rate


    # calculates interest earned with simple interest formula (P*r*t)
    def calc_int(self):

        # if statement that calculates interest based on user-chosen percentage
        if self.int_rate == .002:

            # interest rate expressed in a string
            self.str_rate = ".2%"

            # interest term that differs for each rate
            self.str_time = "month"

            # the equation's product becomes "amnt"
            # "amnt" is obtained by calculating interest based on the number of terms
            self.amnt = self.annual / 12

            # annual interest earnings
            self.annual = self.bal * self.int_rate

        elif self.int_rate == .005:

            self.str_rate = ".5%"

            self.str_time = "two months"

            self.amnt = self.bal * self.int_rate / 6

            self.annual = self.bal * self.int_rate

        elif self.int_rate == .008:

            self.str_rate = ".8%"

            self.str_time = "quarter"

            self.amnt = self.bal * self.int_rate / 4

            self.annual = self.bal * self.int_rate

        elif self.int_rate == .04:

            self.str_rate = "4%"

            self.str_time = "year"

            self.amnt = self.bal * self.int_rate * 1

            self.annual = self.amnt

        # returns the product
        return self.amnt


    # deposit method; only used for adding money to the account
    def deposit(self, amnt):

        # self.amnt gets added to balance
        self.bal += self.amnt

        print(DIV)

        # displays success message
        print(f"\n\tDeposit " + SM + "\n")

        return self.bal


    # calculates account withdrawals; also prompts the user to enter a valid amount if
    # their account would go negative upon withdrawal
    def withdrawal(self, amnt):

        # initially makes the withdrawal
        self.bal -= self.amnt

        # if statement detects withdrawals that would make the account go negative
        if self.bal < 0:

            self.insuff_funds = True

            print("\nInsufficient funds!\n")

            # withdrawal amount gets added back to balance
            self.bal += self.amnt

            # prints current balance
            print(self.__str__())

            # user gets prompted to enter a valid amount, the input is saved to self.amnt
            self.amnt = float(input("Please enter a valid withdrawal amount: "))

            # the input is withdrawn their balance
            self.bal -= self.amnt

            # if the user enters another invalid amount, this while loop will reiterate
            # until valid input has been attained
            while self.bal < 0:

                # the invalid amount is added back to the account
                self.bal += self.amnt

                # the user is prompted again
                self.amnt = float(input("Please enter a valid withdrawal amount: "))

                # determining statement that will make the while loop condition true or false
                self.bal -= self.amnt

        print(DIV)

        # print success message
        print(f"\n\tWithdrawal " + SM + "\n")

        return self.bal


    # displays account balance, interest rate, and monetary accumulation
    def __str__(self):

        # formatting pattern that adds a comma in every thousands place
        # and only allows 2 visible digits after a decimal point
        amnt_fmt = '{:,.2f}'

        # all the numerical amounts are reformatted
        self.str_annual = amnt_fmt.format(self.annual)
        self.str_bal = amnt_fmt.format(self.bal)
        self.str_amnt = amnt_fmt.format(self.amnt)

        # stores only the current balance to be printed in withdrawal method
        self.cb = f"\nCurrent balance: ${self.str_bal}\n"

        # stores interest rate and accumulated amount in string
        self.acc_int = (f"\nEstimated interest accumulated every {self.str_time} "
                        f"based on interest rate of {self.str_rate}: "
                        f"${self.str_amnt}") +"\n"

        print(DIV)

        # if statement iterates when user does not choose the annual interest option
        if self.int_rate != .04:

            # adds this string to acc_int to display the annual interest
            self.acc_int += f"\nAnnual interest earnings: ${self.str_annual}\n"

        # only returns the current balance when warning the user of insufficient funds
        if self.insuff_funds is True:

            return self.cb

        # returns the current balance and other info when viewing their balance
        return self.cb + self.acc_int



# initial function that starts program with "login" and welcome message
def main():


    print("\nFa$t Banking Login\n")


    print("Please enter the following info :)")

    name = input("Your Name: ")
    a_num = input("Your Account number: ")

    print(DIV)

    print(f"Welcome back {name}!\n")

    init_transaction(name, a_num)


# the initial deposit transaction and interest rate choice occur here
def init_transaction(name, a_num):

    # globalizes future BankAcct instantiation
    global my_acc

    # variable that changes based on user input and controls "while" loop
    adj = "y"

    while adj == "y" or adj == "y":

        # options and info for each rate stored in sub lists
        rate_info = [["Option", "Frequency", "Interest Rate"],
                     ["1", " Monthly ", ".2%"],  # 30 days
                     ["2", " Bimonthly ", ".5%"],  # 60 days
                     ["3", " Quarterly ", ".8%"],  # 90 days
                     ["4", " Annually ", "4%"]]  # 365 days

        # create and format a table for the rate_info
        t = Texttable()

        t.set_cols_align(["c", "l", "c"])

        t.add_rows(rate_info)

        # prompt used in typo_checker
        prompt = "Please enter the amount you would like to deposit: "

        # run typo_checker and save its return value to amount
        amount = typo_checker(prompt)

        # BankAcct class is instantiated
        my_acc = BankAcct(name, a_num, amount)


        print(DIV)

        print("Perfect! We have a few options for accumulating interest in your savings account.")

        # draw the interest "rate_info" table
        int_table = t.draw()

        # define the table title and save it to a variable
        int_table_title = "\n   -=-=- Interest Rate Options -=-=-"

        # print the interest rate options title and table
        print(int_table_title)
        print("\n" + int_table)

        # helper function that prompts for valid input if needed
        option_validator()

        # deposit the amount inputted by the user to their balance
        my_acc.deposit(amount)

        # adjust the interest according to their choice
        my_acc.adj_int(option)

        # calculate the total earnings based on the interest rate
        my_acc.calc_int()

        # display balance and estimated interest earned
        print(my_acc.__str__())

        print(DIV)

        # input that exits the while loop or restarts it
        adj = input("Enter y to make adjustments or any other key to continue: ")

        # if statement that keeps the code neatness consistent
        if adj == "y" or adj == "Y":

            print(DIV)

    else:

        menu(int_table_title, int_table)


# typo checker for validating amounts that the user inputs
def typo_checker(prompt):

    # try-except block that checks for typos in "amount" input
    try:

        amount = float(input(f"{prompt}"))

    except ValueError:

        # if there is a typo, typo_found = True
        typo_found = True

        # while there are typos in the input...
        while typo_found is True:

            # this try-except block reiterates until the user
            # enters a typo-free response
            try:

                amount = float(input("\nTypo found! Please retry: "))

            except ValueError:

                typo_found = True

            # when the input is typo-free, typo_found = False
            # and the while loop ends
            else:

                typo_found = False

    return amount


# function that validates a user choice based on which "option" they enter
def option_validator():

    # globalizes user input for "option"
    global option

    # try-except block that catches a value error when a letter is entered
    try:

        option = int(input("\nEnter the character that corresponds to your choice: "))

    except ValueError:

        exit_()


    # while loop that reiterates until it receives valid input
    while option < 1 or option > 4:

        option = input(int("That is not a valid option. Try again: "))

    # when valid input is achieved...
    else:

        # change "opt" attribute according to the user's choice
        my_acc.opt = option

        return option


# main menu where the user can choose what action they want to take
def menu(int_table_title, int_table):

    # while loop that ends when the user enters an "X"; Although this isn't
    # made known, there needed to be a condition for the loop that ends the program
    # when the user wants to exit
    while option != "x" or option != "X":

        print(DIV)

        time.sleep(1)


        print("\n   -=-=-=- Main Menu -=-=-=-\n")

        # options and account actions stored in sub lists
        menu_options = [["Option", "Account Actions"],
                     ["1", "Deposit"],
                     ["2", "Withdrawal"],
                     ["3", "Check Balance"],
                     ["4", "Adjust Interest Rate"],
                     ["Any Key", "Exit =>"]]

        # create a menu table for the rate_info
        mt = Texttable()

        mt.set_cols_align(["c", "l"])

        mt.add_rows(menu_options)

        # prints a table of account actions that the user can take
        print(mt.draw())

        # validate input option
        option_validator()

        # option 1: account deposit
        if option == 1:

            print(DIV)

            #prompt for typo_checker
            prompt = "\nAmount to deposit: "

            # run typo_checker and save its return value to amount
            amount = typo_checker(prompt)

            # replace "amnt" value with updated "amount" value
            my_acc.amnt = amount

            # deposit the amount into the account
            my_acc.deposit(amount)

            # after making the deposit, calculate the interest
            my_acc.calc_int()


        # option 2: account withdrawal
        elif option == 2:

            print(DIV)

            # prompt for typo_checker
            prompt = "\nAmount to withdrawal: "

            # run typo_checker and save its return value to amount
            amount = typo_checker(prompt)

            # replace "amnt" value with updated "amount" value
            my_acc.amnt = amount

            # withdrawal the amount from the account
            my_acc.withdrawal(amount)

            # after making the withdrawal, calculate the interest
            my_acc.calc_int()


        # option 3: displays account balance / interest earnings
        elif option == 3:

            print(my_acc.__str__())


        # option 4: for adjusting the current interest rate
        elif option == 4:

            print(int_table_title)

            # print table of interest rate options
            print(int_table)

            # validate input option
            option_validator()

            # replace "opt" value with updated "option" value
            my_acc.opt = option

            # adjust interest rate
            my_acc.adj_int(option)

            # calculate new interest
            my_acc.calc_int()

            # then, display balance and interest rate info
            print(my_acc.__str__())


    # if the user enters an X, the program will end
    else:

        exit_()


# function that ends the program
def exit_():

    print("Thank you for choosing Fa$t Banking!")

    time.sleep(1.3)

    exit()


# call the initial function
main()