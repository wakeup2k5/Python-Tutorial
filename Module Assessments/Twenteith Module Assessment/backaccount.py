# The BankAccount class

from datetime import datetime
import hashlib


class BankAccount(object):
    def __init__(self, name, accountType, balance = 0):
        self.name = name
        self.accountType = accountType
        self.balance = balance
        self.accountNumber = hashlib.sha256(str(self.accountType+self.name+self.accountType).encode("utf-8")).hexdigest()[:16]
        self.filename = str(self.accountNumber) + "_" + self.accountType + "_" + self.name.replace(" ","_") + ".txt"

    def logTransaction(self, message):
        transactionLog = open(self.filename, "a+") # this mode will create the file if it doesn't exist already
        transaction_date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        transactionLog.write(transaction_date_time + ": " + message)
        transactionLog.close()

    def displayTransactionLog(self):
        print("Transaction History")
        transactionLog = open(self.filename, "r")
        transactionLogEntries = transactionLog.readlines()
        for logEntry in transactionLogEntries:
            print(logEntry)

    def deposit(self, amount):
        self.balance += amount
        self.logTransaction("$" + str(amount) + " deposited.  Closing balance: $" + str(self.balance) + "\n")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.logTransaction("$" + str(amount) + " withdrawn.  Closing balance: $" + str(self.balance) + "\n")
        else:
            self.logTransaction("$" + str(amount) + " cannot be withdrawn due to insufficient funds.  Closing balance: $" + str(self.balance) + "\n")

    def getBalance(self):
        return self.balance

    def getUserId(self):
        return self.name
    
    def getUsername(self):
        return self.name    
    
    def getAccountType(self):
        return self.accountType        
    
    def getAccountNumber(self):
        return self.accountNumber   

    def printAccountSummary(self):
        print("Account Summary")
        print("-> Name: ", self.getUsername())
        print("-> Account Type: ", self.getAccountType())
        print("-> Balance: ", self.getBalance())
        print("-> Account Number: ", self.getAccountNumber())
        print("---")