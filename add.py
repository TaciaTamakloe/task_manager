from db import tasks

def add_tasks(task):
    # save task to database
    tasks.insert_one(task)
    # return response
    return True
