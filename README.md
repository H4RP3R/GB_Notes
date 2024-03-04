# Notes
Command line note-taking utility
### Usage
```bash
python3 notes_app.py add -t "note title" -m "note message"
```
```bash
python3 notes_app.py list
```
```bash
python3 notes_app.py delete -i <note_id>
```
```bash
python3 notes_app.py update -i <note_id> -t "new title" -m "new message"
```
```bash
python3 notes_app.py filter -d <dd.mm.yyy>
```
### Positional arguments
| Argument | Description |
|---|---|
add | add new note
list | list all notes
delete | delete note
update | update note
filter | filter notes
### Options
| Option | Description |  
|---|---|
-h, --help | show this help message and exit
-t, --title | note title
-m, --msg | note message
-i, --id | note id (first eight characters)
-d, --date | date for filter
