# This project allows you to apply the knowledge gained from all Python modules covered in the learning platform. 
# The knowledge from each module is essential for implementing certain functionalities in this project.
# In this project, you will simulate bank account operations using object-oriented programming (OOP). 
# You should create a class called BankAccount, specializing in all banking operations, including:
# Creating an account.
# Depositing money.
# Withdrawing money.
# Checking the balance.
# Getting the account type.
# Getting the account number.
# Getting the holder name.
# Keeping a transaction history.

from backaccount import BankAccount
import os
clear = lambda: os.system('cls')

def main():
    jamesAccount = BankAccount("James Collins", "Chequing", 50)

    clear()
    jamesAccount.printAccountSummary()

    input("Press Enter to continue")
    clear()

    amountToDeposit = 50
    jamesAccount.deposit(amountToDeposit)
    print("Attempted to deposit: $" + str(amountToDeposit))

    amountToWithdraw = 10
    jamesAccount.withdraw(amountToWithdraw)      
    print("Attempted to withdraw: $" + str(amountToWithdraw))

    amountWithdrawToTriggerInsufficientFunds = 1000
    jamesAccount.withdraw(amountWithdrawToTriggerInsufficientFunds) # this should log "insufficient funds"
    print("Attempted to withdraw: $" + str(amountWithdrawToTriggerInsufficientFunds))

    input("Press Enter to continue")
    clear()

    print("Method Testing")
    print("getBalance: ", jamesAccount.getBalance())
    print("getUserId: ", jamesAccount.getUserId())
    print("getUsername: ", jamesAccount.getUsername())
    print("getAccountType: ", jamesAccount.getAccountType())
    print("getAccountNumber: ", jamesAccount.getAccountNumber())
    print("getAccountNumber: ", jamesAccount.getAccountNumber())

    input("Press Enter to continue")
    clear()

    # Display transactions
    jamesAccount.displayTransactionLog()

main()