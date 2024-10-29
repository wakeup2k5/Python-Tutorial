# Build a library catalogue system that manages information about books, including their title, author, and availability status. 
# Use classes to represent books and include methods for checking out and returning books.
import os
clear = lambda: os.system('cls')

class Book:
    def __init__(self, title, author, status):
        self.title = title
        self.author = author
        self.status = status
        
    def checkout(self):
        self.status = "checked out"
        print(self.title + " checked out successfully")

    def checkin(self):
        self.status = "available"
        print(self.title + " checked in successfully")
    
class Catalogue:
    books = []
    
    def __init__(self):
        pass

    def addBook(self, book):
        self.books.append(book)
        
    def listBooks(self):
        for idx in range(len(self.books)):
            print(str(idx + 1) + " : " + self.books[idx].title + " by " + self.books[idx].author + " | STATUS: " + self.books[idx].status)

def main():
    clear()
    catalogue = Catalogue()
    catalogue.addBook(Book("The Road", "Cormac McCarthy", "available"))
    catalogue.addBook(Book("Never Let Me Go", "Kazuo Ishiguro", "available"))
    catalogue.addBook(Book("White Teeth", "Zadie Smith", "available"))
    catalogue.addBook(Book("Normal People", "Sally Rooney", "available"))
    catalogue.addBook(Book("The Night Circus", "Erin Morgenstern", "available"))

    menu_options = {
        "1": "View Entire Catalogue", 
        "2": "Check out book", 
        "3": "Check in book", 
        "4": "Exit", 
        }

    print("Book Catalogue")
    
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
            catalogue.listBooks()
            input("\nPress Enter to return to main menu...")
        if selection == "2":
            clear()
            catalogue.listBooks()
            chosenBook = int(input("\nEnter a book number to check out: "))
            if(chosenBook <= len(catalogue.books) and chosenBook > 0):
                chosenBookIndex = chosenBook - 1
                catalogue.books[chosenBookIndex].checkout()
            else:
                print("\nInvalid selection.  Check out failed.")
            input("\nPress Enter to return to main menu...")
        if selection == "3":
            clear()
            catalogue.listBooks()
            chosenBook = int(input("\nEnter a book number to check in: "))
            if(chosenBook <= len(catalogue.books) and chosenBook > 0):
                chosenBookIndex = chosenBook - 1
                catalogue.books[chosenBookIndex].checkin()
            else:
                print("\nInvalid selection.  Check in failed.")
            input("\nPress Enter to return to main menu...")
        if selection == "4":
            clear()
            break

main()