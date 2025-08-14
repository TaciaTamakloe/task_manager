import add
import show
import update
import delete

add_tasks_response = add.add_task("Sleep")
print(add_tasks_response)

show_tasks_response = show.show_tasks()
print(show_tasks_response)

update_tasks_response = update.show_tasks("sleep","wake up")
print(update_tasks_response)

delete_tasks_response = delete.delete_task("wake up")
print(delete_tasks_response)