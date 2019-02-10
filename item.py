from datetime import datetime
from textwrap import dedent
from sys import exit
class Item(object):

    def create_task():
        now = datetime.now()
        date_time = now.strftime("%Y/%m/%d %H:%M:%S")
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
            todofile.write(new_todo + " "+ date_time + "\n")
            todofile.close()
            Item.create_task()

        elif new_task == 'list':
            todofile = open("todos.txt", "r")
            print(todofile.read())
            todofile.close()
            Item.create_task

        elif new_task == 'help':
            print(dedent("""
            *****************************
            * new (creates a new task)  *
            * list (list all the items) *
            *****************************
            """))
            Item.create_task()
        else:
            print("command not recognized")
            prompt = input("Do you want to restart? yes or no?> ")

            if prompt == 'yes':
                Item.create_task()
            elif prompt == 'no':
                exit(0)

Item.create_task()

