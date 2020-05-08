from json import dumps
from utils import jsonDefault
from flask import abort


class NoteList:

    def __init__(self):
        self.notes = []

    def toJson(self):
        return dumps(self, default=jsonDefault)

    def addNote(self, note):
        self.notes.append(note)

    def __findNote(self, noteID):
        for note in self.notes:
            if note.ID == noteID:
                return note
        return None

    def editNote(self, noteID, newText):
        note = self.__findNote(noteID)
        if not note:
            abort(400, "Note is not found")
        note.edit(newText)

    def removeNote(self, noteID):
        self.notes = [note for note in self.notes if note.ID != noteID]
