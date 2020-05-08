from flask import Flask, jsonify, request
from note_list import NoteList
from note import Note

app = Flask(__name__)

NoteList = NoteList()

# Routes
@app.route('/get-notes', methods=["GET"])
def getNotes():
    return jsonify(NoteList.toJson()), 200


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

# Errors
@app.errorhandler(400)
def error400(e):
    print(e, flush=True)
    return jsonify({"message": e.description}), 400


@app.errorhandler(500)
def handle_exception(e):
    print(e, flush=True)
    return jsonify("Server error, try later"), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
