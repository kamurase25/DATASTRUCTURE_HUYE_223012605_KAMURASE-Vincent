
undo_stack = []  
task_queue = []  
completed_tasks = []  


def add_task(task):
    undo_stack.append(task)
    task_queue.append(task)
    print(f"Task '{task}' added.")


def assign_task():
    if task_queue:
        task = task_queue.pop(0)
        print(f"Task '{task}' assigned.")
    else:
        print("No tasks to assign.")


def complete_task(task):
    if task in undo_stack:
        undo_stack.remove(task)
        completed_tasks.append(task)
        print(f"Task '{task}' completed.")
    else:
        print("Task not found.")


def undo_last_task():
    if undo_stack:
        task = undo_stack.pop()
        if task in task_queue:
            task_queue.remove(task)
        print(f"Task '{task}' undone.")
    else:
        print("No tasks to undo.")


def show_completed_tasks():
    if completed_tasks:
        print("Completed tasks:", completed_tasks)
    else:
        print("No tasks have been completed yet.")


def menu():
    while True:
        print("\n--- Project Management Tool ---")
        print("1. Add a Task")
        print("2. Assign a Task")
        print("3. Complete a Task")
        print("4. Undo Last Task")
        print("5. Show Completed Tasks")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task description: ")
            add_task(task)
        
        elif choice == '2':
            assign_task()
        
        elif choice == '3':
            task = input("Enter the task to complete: ")
            complete_task(task)
        
        elif choice == '4':
            undo_last_task()
        
        elif choice == '5':
            show_completed_tasks()
        
        elif choice == '6':
            print("Exiting the tool. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


menu()