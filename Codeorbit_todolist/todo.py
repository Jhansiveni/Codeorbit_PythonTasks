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
