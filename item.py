from datetime import datetime
from textwrap import dedent
from sys import exit
class Item(object):

    def add_time():
        now = datetime.now()
        date_time = now.strftime("%Y/%m/%d %H:%M:%S")
        todofile = open("todos.txt", "a+")
        todofile.write(f"\t ~~~{date_time} \n")

              