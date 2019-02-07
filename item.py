from datetime import datetime
class Item(object):

    def createTask():
        now = datetime.now()
        date_time = now.strftime("%Y/%m/%d %H:%M:%S")
        file1 = open("todos.txt","a+")
        task = input("Create A New Task: ")
        file1.write("\n" + task + ' ' + date_time)
        print(f"{task} task created! at {date_time}")
    

Item.createTask()
