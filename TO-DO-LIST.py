# Initialize an empty to-do list
todo_list = []

# Function to add a task to the to-do list
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to view the to-do list
def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Function to mark a task as completed
def complete_task(task_index):
    if 1 <= task_index <= len(todo_list):
        completed_task = todo_list.pop(task_index - 1)
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print("Invalid task index.")

# Main loop
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        task_index = int(input("Enter the index of the completed task: "))
        complete_task(task_index)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")
