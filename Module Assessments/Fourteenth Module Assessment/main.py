# Create a simple personal diary application where users can write and save their daily thoughts or experiences to a text file. 
# The program should allow users to view their previous entries and handle exceptions in a controlled manner (e.g., file not found errors and permission issues).

from datetime import datetime

menu_options = {"1" : "Create a New Entry", "2": "View Previous Entries"}

entries_data = open("entries_data.txt", "a+")

print("Personal Diary")
print("MENU")
print("---")
for key in menu_options:
    print(key,":", menu_options[key])
print("---")
selection = input("Please choose a menu number from above: ")



try:
    if menu_options[selection] == 'Create a New Entry':
        new_entry = input("Types a new entry and press Enter: ")
        entry_date_time_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        entries_data.write(str(entry_date_time_str) + ": " + new_entry + "\n")
    elif menu_options[selection] == 'View Previous Entries':
        entries_data.seek(0)
        previous_entries = entries_data.readlines()
        for entry in previous_entries:
            print(entry)
except:
    print("Invalid selection or file not found")
finally:
    entries_data.close()