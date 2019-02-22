from textwrap import dedent
from sys import exit
from item import Item
# Print all of the to-do items in the list. x
# Add a new item to the list. x
# Mark an item as completed.

class Manager(object):


    def __init__(self, task, iscomplete):
        self.task = task
        self.iscomplete = iscomplete
    
    def todo_list(self):
        with open('todos.txt', 'r') as rf:
            for line in rf:
                print(line)

    def todo_new(self):
        with open('todos.txt', 'a+') as af:
            print("Create a new task")
            new_task = input("> ")
            af.write(new_task + '\n')
    
    # def todo_iscomplete(self):
    #     with open('todos.txt', 'r') as edit:
    #          # take user input which represents name of task
    #         completed_task = input("What Task Did You Complete? ")
    #         # copy contents of txt
    #         for line in edit:
    #             if completed_task == edit.readlines:
    #                 edit.write(line)
                

        # delete text file's contents

        # look at copy, check each line that task name matches user input

        # change that line so that it is shown to be completed

        # that copy string, you can put back into the text file
            

taskmanager = Manager(False, False)           
print(taskmanager.todo_new())
print(taskmanager.todo_list())