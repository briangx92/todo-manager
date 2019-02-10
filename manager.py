from textwrap import dedent
from sys import exit

class Manager(object):

   def create_task():
        print(dedent("""
        **********************************
        * Type help for list of commands *
        **********************************
        """))
        new_task = input("What do you want to do? > ")

        if new_task == "new":
            todofile = open(r"todos.txt", "a+")
            print(dedent("""
            **********************
            * Create a new task  *
            ********************** """))
            new_todo = input("> ")
            todofile.write(new_todo + " " + "\n")
            todofile.close()
            Manager.create_task()

        elif new_task == 'list':
            todofile = open("todos.txt", "r")
            print(todofile.read())
            todofile.close()
            Manager.create_task

        elif new_task == 'help':
            print(dedent("""
            *****************************
            * new (creates a new task)  *
            * list (list all the items) *
            *****************************
            """))
            Manager.create_task()
        else:
            print("command not recognized")
            prompt = input("Do you want to restart? yes or no?> ")

            if prompt == 'yes':
                Manager.create_task()
            elif prompt == 'no':
                exit(0)
        
Manager.create_task()
