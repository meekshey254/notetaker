from flask import Flask, request, jsonify, render_template
from datetime import datetime
import os

NOTES_FILE = 'notes.txt'

app = Flask(__name__, template_folder='templates')

# Helper functions (copied from notetaker.py)
def add_note(note_text):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(NOTES_FILE, 'a') as f:
        f.write(f"{timestamp} | {note_text}\n")
    return {'status': 'success', 'message': 'Note added!'}

def list_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, 'r') as f:
        lines = f.readlines()
    notes = []
    for idx, line in enumerate(lines, 1):
        notes.append({'id': idx, 'content': line.strip()})
    return notes

def search_notes(keyword):
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, 'r') as f:
        lines = f.readlines()
    notes = []
    for idx, line in enumerate(lines, 1):
        if keyword.lower() in line.lower():
            notes.append({'id': idx, 'content': line.strip()})
    return notes

def delete_note(note_id):
    if not os.path.exists(NOTES_FILE):
        return {'status': 'error', 'message': 'No notes to delete.'}
    with open(NOTES_FILE, 'r') as f:
        lines = f.readlines()
    if note_id < 1 or note_id > len(lines):
        return {'status': 'error', 'message': 'Invalid note ID.'}
    del lines[note_id - 1]
    with open(NOTES_FILE, 'w') as f:
        f.writelines(lines)
    return {'status': 'success', 'message': 'Note deleted!'}

# API routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/notes', methods=['GET'])
def api_list_notes():
    return jsonify(list_notes())

@app.route('/api/notes', methods=['POST'])
def api_add_note():
    data = request.get_json()
    note_text = data.get('note')
    return jsonify(add_note(note_text))

@app.route('/api/notes/search', methods=['GET'])
def api_search_notes():
    keyword = request.args.get('keyword', '')
    return jsonify(search_notes(keyword))

@app.route('/api/notes/<int:note_id>', methods=['DELETE'])
def api_delete_note(note_id):
    return jsonify(delete_note(note_id))

if __name__ == '__main__':
    app.run(debug=True)
