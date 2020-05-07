class NoteList:

    def __init__(self):
        self.notes = []

    def __str__(self):
        return ", ".join(str(note) for note in self.notes)

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
            return
        note.edit(newText)

    def removeNote(self, noteID):
        self.notes = [note for note in self.notes if note.ID != noteID]
