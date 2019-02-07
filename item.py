# # from sys import argv

# # script, filename = argv

# # txt = open(filename)

# class Item(object):

#     def create(self):
#         file1 = open("todos.txt","a+")
#         task = input("Create A New Task: ")
#         file1.write("/n"+ task)
#         file1.close() 
# #         f = open('todos.txt','r')
# #         message = f.read()
# #         print(message)
# #         f.close()
# #         return self.create

# # file1 = open("todos.txt","a+")
# # task = input("Create A New Task: ")
# # file1.write("/n"+ task)
# # file1.close()
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
