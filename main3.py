from add import add_tasks
from show import show_tasks

task_title = input("what task are you going to do ?:")
add_tasks({"title": task_title})

for task in show_tasks():
    print(task)
