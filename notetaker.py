import sys
import os
from datetime import datetime

NOTES_FILE = 'notes.txt'

def add_note(note_text):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(NOTES_FILE, 'a') as f:
        f.write(f"{timestamp} | {note_text}\n")
    print('Note added!')

def list_notes():
    if not os.path.exists(NOTES_FILE):
        print('No notes found.')
        return
    with open(NOTES_FILE, 'r') as f:
        lines = f.readlines()
        if not lines:
            print('No notes found.')
            return
        for idx, line in enumerate(lines, 1):
            print(f"{idx}: {line.strip()}")

def search_notes(keyword):
    if not os.path.exists(NOTES_FILE):
        print('No notes found.')
        return
    with open(NOTES_FILE, 'r') as f:
        lines = f.readlines()
        found = False
        for idx, line in enumerate(lines, 1):
            if keyword.lower() in line.lower():
                print(f"{idx}: {line.strip()}")
                found = True
        if not found:
            print('No matching notes found.')

def delete_note(note_id):
    if not os.path.exists(NOTES_FILE):
        print('No notes to delete.')
        return
    with open(NOTES_FILE, 'r') as f:
        lines = f.readlines()
    if note_id < 1 or note_id > len(lines):
        print('Invalid note ID.')
        return
    del lines[note_id - 1]
    with open(NOTES_FILE, 'w') as f:
        f.writelines(lines)
    print('Note deleted!')

def print_usage():
    print('Usage:')
    print('  python notetaker.py add "your note here"')
    print('  python notetaker.py list')
    print('  python notetaker.py search "keyword"')
    print('  python notetaker.py delete <note_id>')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    command = sys.argv[1]
    if command == 'add' and len(sys.argv) >= 3:
        note_text = ' '.join(sys.argv[2:])
        add_note(note_text)
    elif command == 'list':
        list_notes()
    elif command == 'search' and len(sys.argv) >= 3:
        keyword = ' '.join(sys.argv[2:])
        search_notes(keyword)
    elif command == 'delete' and len(sys.argv) == 3:
        try:
            note_id = int(sys.argv[2])
            delete_note(note_id)
        except ValueError:
            print('Note ID must be an integer.')
    else:
        print_usage()
