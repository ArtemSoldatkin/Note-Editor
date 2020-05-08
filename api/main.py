from flask import Flask, jsonify, request
from flask.logging import create_logger
from note_list import NoteList
from note import Note

app = Flask(__name__)
log = create_logger(app)

NoteList = NoteList()

# Routes
@app.route('/get-notes', methods=["GET"])
def getNotes():
    return jsonify(NoteList.toJson()), 200


@app.route("/add-note", methods=["POST"])
def addNote():
    body = request.get_json(force=True)
    text = body.get("text")
    note = Note(text)
    log.info(f"New note {note.ID}")
    NoteList.addNote(note)
    return jsonify({"message": "OK"}), 200


@app.route("/edit-note/<id>", methods=["PUT"])
def changeNote(id):
    body = request.get_json(force=True)
    text = body.get("text")
    NoteList.editNote(id, text)
    log.info(f"Note {id} is changed")
    return jsonify({"message": "OK"}), 200


@app.route("/remove-note/<id>", methods=["DELETE"])
def removeNote(id):
    NoteList.removeNote(id)
    log.info(f"Note {id} was deleted")
    return jsonify({"message": "OK"}), 200

# Errors
@app.errorhandler(400)
def error400(e):
    log.error(e)
    return jsonify({"message": e.description}), 400


@app.errorhandler(500)
def handle_exception(e):
    log.error(e)
    return jsonify("Server error, try later"), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
