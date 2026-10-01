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
