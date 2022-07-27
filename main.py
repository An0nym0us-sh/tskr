#!/usr/bin/env python3


help_text = """
Commands are passed in as just words
(All dates should be passed in the YYYY-MM-DD format)
Available Commands:
    new : 
        create a new task. Look at the example below.
        tskr new 2022-02-10 Observe Umbrella Day
    remove:
        remove a task from the task list 
        tskr remove 1 (This removes the first task)
    clear:
        clear al tasks from the list.
        tskr clear 
    set:
        use this to set the status and time of tasks (You can set statuses to any one word)
        tskr set status skippable n (sets the status of the nth task in the task list)
        tskr set time 2022-09-3 n (set the time of the nth task in the task list)

Warning: tskr doesn't validate input so invalid inputs should result in (most probably) harmless errors from python
"""

from datetime import datetime
from sys import argv

list_to_str = lambda lst: " ".join(lst)

# Replace the vaule with the path to task_file
task_file = "tskr_tasks"


class Task:
    def __init__(self, time , description, status):
        self.time = datetime.strptime(time , "%Y-%m-%d")
        self.description = description
        self.status = status

    def __repr__(self):
        return datetime.strftime(self.time , "%Y-%m-%d") + "\t" + self.description + "\t" + self.status

    def set_status(self, status):
        self.status = status

    def set_time(self, time):
        self.time = time
        


def main():
    task_list = [] # A list of all the tasks

    # We need to read current tasks from .json file
    # and sort by the dates

    with open(task_file, "r") as f:
        for task in f.readlines():
            if task != "\n":
                task_attribs = task.split("\t")
                task_list.append(Task(task_attribs[0], task_attribs[1] , task_attribs[2].rstrip()))
    

    if len(argv) == 1:
        task_list.sort(key= lambda task: task.time)
        for i in task_list:
            print(i)

        # we don't write to file this time
        exit()
    elif argv[1] == "help":
        print(help_text)
    
    # Create a new task
    elif argv[1] == "new":
        task_list.append(Task(argv[2],list_to_str(argv[3::]), "Incomplete"))

    # Clear task list
    elif argv[1] == "clear":
        task_list = []

    elif argv[1] == "set":
        if argv[2] == "status":
            task_list[argv[-1]].set_status(argv[3])
        if argv[2] == "time":
            task_list[argv[-1]].set_time(argv[3])

    # Remove tasks
    elif argv[1] == "remove":
        del task_list[int(argv[-1])-1]

    # Write the tasks to file
    # sort them first as well
    task_list.sort(key= lambda task: task.time)

    with open(task_file , "w") as f:
        for task in task_list:
            f.write(task.__repr__() + "\n")

    
if __name__ == "__main__":
    main()
        
