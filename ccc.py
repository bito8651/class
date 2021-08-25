from db import Db  # from file import * means import all of them  # from folders.filename import module


class Tool:
    def __init__(self):
        print('testing message')
        self.db = Db()


t = Tool()
