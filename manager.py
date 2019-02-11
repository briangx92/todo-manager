from textwrap import dedent
from sys import exit
from item import Item

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
            *********************
            * Create a new task *
            ********************* """))
            new_todo = input("> ")
            todofile.write(" " + new_todo + "\n")
            todofile.close()
            Item.add_time()
            prompt = input("Do you want to create a new task? yes or no?>  ")

            if prompt == "yes":
                Manager.create_task()
                Item.add_time()

            else:
                exit(0)

        elif new_task == 'list':
            todofile = open("todos.txt", "r")
            print(todofile.read())
            todofile.close()
            exit(0)

        elif new_task == 'help':
            print(dedent("""
            *****************************
            * new (creates a new task)  *
            * list (list all the items) *
            * exit (exit program)       *
            *****************************
            """))
            Manager.create_task()

        elif new_task == 'exit':
            exit(0)
        else:
            print("command not recognized")
            prompt = input("Do you want to restart? yes or no?> ")

            if prompt == 'yes':
                Manager.create_task()
            elif prompt == 'no':
                exit(0)

    def iscomplete():
        print(dedent("""
        *****************************************
        * Do you have a task that is completed? *
        *****************************************
        """))
        todofile = open("todos.txt", "a+")


Manager.create_task()
Item.add_time()
