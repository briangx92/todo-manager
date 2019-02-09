from datetime import datetime
from textwrap import dedent
class Item(object):

    # def createTask():
    #     now = datetime.now()
    #     date_time = now.strftime("%Y/%m/%d %H:%M:%S")
    #     file1 = open("todos.txt","a+")
    #     task = input("Create A New Task: ")
    #     file1.write("\n" + task + ' ' + date_time)
    #     print(f"{task} task created! at {date_time}.")
    def createTask():
        now = datetime.now()
        date_time = now.strftime("%Y/%m/%d %H:%M:%S")
        todofile = open("todos.txt", "a+")
        print(dedent("""
        Type help for list of commands
        """))
        new_task = input("What do you want to do?")
        list = []
        new_task = prompt

        if new_task == "new todo":
            












    # def isCompleted():
    #     edit = open("todos.txt").read()
    #     print(edit)
    #     completedTask = input("What Task Did You Complete? ")

    #     s = edit.replace(completedTask, "This task is completed")
    #     f2 = open("todos.txt", 'w+')
    #     if s != f2:
    #         f2.write(s)
        
    #     elif s == f2:
    #         f2.write(s)
    #     else:
    #         print("item not in list")
    #     f2.close()

    #     f = open('todos.txt','r')
    #     message = f.read()
    #     print(message)
    #     f.close()


Item.createTask()
# Item.isCompleted()

