tasks = []

#Function to add a new task to To-Do List
def add_task():
    task_name = input("Enter your task here: ")
    if task_name:
        tasks.append({"task": task_name, "done": False})
        print("Task added!")
    else:
        print("Task cannot be empty!")

#Function to view tasks in the To-Do List
def view_task():
    if not tasks:
        print("No tasks found.\n")
    else:
        print("---Your Tasks---")
        index = 1
        for task in tasks:
            print(f"{index}. Task: {task['task']}, Done: {task['done']}")
            index += 1

#Function to get valid index to use in other functions
def get_valid_index():
    try:
        index = int(input("Enter task index: "))
        if 0 < index <= len(tasks):
            return index -1
        else:
            print("Index out of range. Try again")
    except ValueError:
        print("Invalid input. Try again!")
    
    return None

#Function to remove a task from the To-Do List
def remove_task():
    
    view_task()
    index = get_valid_index()
    if index is not None:
        del tasks[index]
        print("Task deleted!")

#Function to mark a task as done in the To-Do List
def mark_task_done():

    view_task()
    index = get_valid_index()
    if index is not None:
        tasks[index]["done"] = True
        print("Task marked as done!")

#Function to edit a task already in the To-Do List    
def edit_task():

    view_task()
    index = get_valid_index()
    if index is not None:
        new_description = input("Enter your new edited task here: ")
        tasks[index]["task"] = new_description
        tasks[index]["done"] = False
        print("Task edited and marked as incomplete!")
    
    
#Main loop of the program
while True:
    print("--- TO DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Edit task")
    print("6. Exit")
    
    try:
        choice = int(input("Choose an option (1-6): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        if not tasks:
            print("No tasks found!")
        else:
            mark_task_done()
    elif choice == 4:
        if not tasks:
            print("No tasks found!")
        else:
            remove_task()
    elif choice == 5:
        if not tasks:
            print("No tasks found!")
        else:
            edit_task()
    elif choice == 6:
        print("Exiting the To-Do List. Bye!")
        break
    else:
        print("Invalid input. Try again!")
