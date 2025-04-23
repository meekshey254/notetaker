# Notetaker: Command-Line & Web GUI

A lightweight Python tool to add, list, search, and delete notes stored in a plain text file. Now available as both a command-line app and a modern web interface!

---

## Features
- Add timestamped notes
- List all notes
- Search notes by keyword
- Delete notes by ID
- Use via CLI or a graphical web interface

---

## Usage

### Command-Line

```
python notetaker.py add "your note here"
python notetaker.py list
python notetaker.py search "keyword"
python notetaker.py delete <note_id>
```

- Notes are stored in `notes.txt` in the same directory.
- Each note is timestamped.

#### Example
```
python notetaker.py add "Buy groceries"
python notetaker.py list
python notetaker.py search groceries
python notetaker.py delete 1
```

---

### Web Interface

1. Install Flask if you haven't:
   ```
   pip install flask
   ```
2. Start the web server:
   ```
   python notetaker_web.py
   ```
3. Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)
4. Use the simple graphical UI to add, search, and delete notes!

---

## File Structure
- `notetaker.py` - Command-line tool
- `notetaker_web.py` - Flask web backend
- `templates/index.html` - Web UI
- `notes.txt` - Where your notes are stored

---

Feel free to contribute or customize!
