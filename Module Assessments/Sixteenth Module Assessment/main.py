# Develop a simple task list manager that allows users to add, remove, and view tasks. 
# The program should save the task list to a text file and handle exceptions in a controlled manner

def add_new_task():
    tasks_data = open("tasks_data.txt", "a")
    new_task = input("Enter task details: ")
    if new_task != "":
        tasks_data.write(new_task + "\n")
    tasks_data.close()

def view_previous_tasks():
    tasks_data = open("tasks_data.txt", "r")    
    tasks_data.seek(0)
    previous_tasks = tasks_data.readlines()
    for idx in range(len(previous_tasks)):
        print(str(idx+1) + " : " + previous_tasks[idx].rstrip() )
    tasks_data.close()

def remove_task(task_number):
    old_tasks_data = open("tasks_data.txt", "r")  
    old_tasks_data.seek(0)
    previous_tasks = old_tasks_data.readlines()
    old_tasks_data.close()
    task_index_to_be_removed = int(task_number) - 1
    new_tasks_data = open("tasks_data.txt", "w")  
    for indx in range(len(previous_tasks)):
        if(indx != task_index_to_be_removed):
            new_tasks_data.write(previous_tasks[indx])
    new_tasks_data.close()

def main(): 
    menu_options = {"1" : "Add a new task", "2": "View Previous Tasks", "3": "Remove a Task", }

    print("Task Tracker")
    print("MENU")
    print("---")
    for key in menu_options:
        print(key,":", menu_options[key])
    print("---")
    selection = input("Please choose a menu number from above: ")

    try:
        if menu_options[selection] == 'Add a new task':
            add_new_task()
        elif menu_options[selection] == 'View Previous Tasks':
            view_previous_tasks()
        elif menu_options[selection] == 'Remove a Task':
            view_previous_tasks()
            task_number =  input("Choose the task to be removed (numberic): ")
            remove_task(task_number)

    except Exception as argument:
        print("ERROR: " + str(argument))
    
main()