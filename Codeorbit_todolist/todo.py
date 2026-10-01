print(" ====== To Do List ====== ")

tasks = []   # this list stores all the tasks


def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added!")

