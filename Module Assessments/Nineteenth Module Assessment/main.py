# Create a simple inventory system that manages information about products in a store. 
# Each product should have specified attributes like name, price, and quantity. 
# Use classes to represent products and include methods for displaying product information, updating quantities, and calculating the total value of the inventory.

import os
clear = lambda: os.system('cls')

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def displayInformation(self):
        print("PRODUCT NAME: " + self.name + " | PRICE: " + str(self.price) + " | QUANTITY: " + str(self.quantity))

    def updateQuantity(self, quantity):
        self.quantity = quantity
    
class Inventory:
    products = []
    
    def __init__(self):
        pass

    def addProduct(self, product):
        self.products.append(product)
        
    def listProducts(self):
        totalQuantity = 0
        totalValue = 0
        for idx in range(len(self.products)):
            totalQuantity += int(self.products[idx].quantity)
            totalValue += int(self.products[idx].quantity) * float(self.products[idx].price)
            print(str(idx + 1) + " : PRODUCT NAME: " + self.products[idx].name + " | PRICE: " + str(round(self.products[idx].price,2)) + " | QUANTITY: " + str(self.products[idx].quantity))
        print(str(totalQuantity) + " product(s) in total, with a total inventory value of $" + str(round(totalValue,2)))

def main():
    clear()
    catalogue = Inventory()
    catalogue.addProduct(Product("Phone Charger", 9.99, 1))
    catalogue.addProduct(Product("Headphones", 19.99, 2))
    catalogue.addProduct(Product("Speaker Set", 29.99, 3))
    catalogue.addProduct(Product("Screwdriver Set", 14.99, 4))
    catalogue.addProduct(Product("Electrical Tape", 0.99, 5))

    menu_options = {
        "1": "Inventory Overview", 
        "2": "View Individual Product", 
        "3": "Update Product Quantity", 
        "4": "Exit", 
        }

    print("Product Inventory")
    
    exitProgram = False

    while exitProgram == False:
        clear()
        print("MAIN MENU")
        print("---")
        for key in menu_options:
            print(key,":", menu_options[key])
        print("---")
        selection = input("Please choose a menu number from above: ")
        if selection == "1":
            clear()
            catalogue.listProducts()
            input("\nPress Enter to return to main menu...")
        if selection == "2":
            clear()
            chosenProduct = int(input("Please choose a product number to view: "))
            if(chosenProduct <= len(catalogue.products) and chosenProduct > 0):
                chosenProductIndex = chosenProduct - 1
                catalogue.products[chosenProductIndex].displayInformation()
            else:
                print("\nInvalid selection.  Please try again.")

            input("\nPress Enter to return to main menu...")
        if selection == "3":
            clear()
            catalogue.listProducts()
            chosenProduct = int(input("Choose a product to update Quantity: "))
            if(chosenProduct <= len(catalogue.products) and chosenProduct > 0):
                chosenProductQuantity  = int(input("Enter the Quantity: "))
                chosenProductIndex = chosenProduct - 1
                catalogue.products[chosenProductIndex].updateQuantity(chosenProductQuantity)
            else:
                print("\nInvalid selection.  Please try again.")

            input("\nPress Enter to return to main menu...")
        if selection == "4":
            clear()
            break

main()