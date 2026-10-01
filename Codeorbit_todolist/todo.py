print(" ====== To Do List ====== ")

tasks = []   # this list stores all the tasks


def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added!")
def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        print("\nYour tasks:")
        number = 1
        for task in tasks:
            print(number, ".", task)
            number = number + 1

def remove_task():
    view_tasks()
    if len(tasks) > 0:
        try:
            number = int(input("Enter the task number to remove: "))
            tasks.pop(number - 1)
            print("Task removed!")
        except ValueError:
            print("Please enter a number only!")
        except IndexError:
            print("That task number does not exist!")

def save_tasks():
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()

# Main program
while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Save and exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        save_tasks()
        print("Tasks saved to tasks.txt. Goodbye!")
        break
    else:
        print("Invalid choice! Enter 1, 2, 3 or 4.")

