# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 22:16:25 2024

@author: justi
"""

class BankAccount:

    def __init__(self, name, balance=0):
        
        self.name = name
        
        self.balance = balance
    
    def deposit(self, amount):
    
        if amount > 0 :
        
            self.balance += amount
            
            print (f"Deposited ${amount}. New balance: ${self.balance}") 
        else:
        
            print("Invalid amount for deposit.")
        
    def withdraw(self, amount):
    
        if 0 < amount <= self.balance :
        
            self.balance -= amount
            
            print(f"Withdrew ${amount}. New balance: $(self.balance)") 
        else :
        
            print("Insufficient funds.")
        
    def get_balance(self):
    
        return self.balance
    
    def __str__(self):

        return f"Account holder: {self.name}, Balance: ${self.balance}"

def main():

    print("Welcome to the Bank!")
    
    print("Create an account to get started.")
    
    name = input("Enter your name: ")
    
    initial_balance = float(input("Enter initial deposit amount: $"))
    
    account = BankAccount(name, initial_balance)

    while True:
    
        print("\n1. Deposit" )
        
        print("2. Withdraw")
        
        print("3. Check Balance")
        
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
    
            amount = float(input("Enter deposit amount: $"))
            
            account. deposit (amount)
        
        elif choice == '2':
        
            amount = float(input("Enter withdrawal amount: $"))
            
            account.withdraw(amount)
        
        elif choice == '3':
        
            print(f"Your balance: ${account.get_balance()}")
        
        elif choice == '4':

            print( "Thank you for banking with us!")

            break 
        else:

            print("Invalid choice. Please try again.")

if __name__== "__main__":

    main()



