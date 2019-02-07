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

class Item():
    def showAll():
        readTask = open("todos.txt", "r")
        readTask.readlines()
        readTask.close()

    def markComplete():
        edit = open("todos.txt").read()
        completedTask = input("What Task Did You Complete? ")
        s = edit.replace(completedTask, completedTask + " This task is completed")
        f2 = open("todos.txt", 'w+')
        f2.write(s)
        f2.close()

        f = open('todos.txt','r')
        message = f.read()
        print(message)
        f.close()

    def createTask():
        file1 = open("todos.txt","a+")
        task = input("Create A New Task: ")
        file1.write("\n" + task)
        file1.close()


Item.createTask()
Item.markComplete()