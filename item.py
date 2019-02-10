from datetime import datetime
from textwrap import dedent
from sys import exit
from manager.py import Manager
class Item(object):

    def add_time():
        now = datetime.now()
        date_time = now.strftime("%Y/%m/%d %H:%M:%S")
        todofile = open("todos.txt", "a+")
        
Item.add_time()
        