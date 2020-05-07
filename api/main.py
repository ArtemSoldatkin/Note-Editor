from note_list import NoteList
from note import Note

from flask import Flask, jsonify, request
app = Flask(__name__)

NoteList = NoteList()

# add errors
@app.route('/get-notes', methods=["GET"])
def getNotes():
    # add json serialize at NoteList
    return jsonify(str(NoteList)), 200


@app.route("/add-note", methods=["POST"])
def addNote():
    body = request.get_json(force=True)
    text = body.get("text")
    NoteList.addNote(Note(text))
    return jsonify("OK"), 200


@app.route("/edit-note/<id>", methods=["PUT"])
def changeNote(id):
    body = request.get_json(force=True)
    text = body.get("text")
    NoteList.editNote(id, text)
    return jsonify("OK"), 200


@app.route("/remove-note/<id>", methods=["DELETE"])
def removeNote(id):
    NoteList.removeNote(id)
    return jsonify("OK"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
