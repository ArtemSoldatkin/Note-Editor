from uuid import uuid4 as uuid
from datetime import datetime


class Note:

    def __init__(self, text):
        self.text = text
        self.ID = str(uuid())
        self.date = datetime.now()
        self.changed = False

    def edit(self, newText):
        self.text = newText
        self.date = datetime.now()
        self.changed = True
