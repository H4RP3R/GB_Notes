import json

from note import Note


class NoteStorage:

    def __init__(self):
        self.repository = []

    def add(self, note):
        self.read()
        self.repository.append(note)

    def save(self):
        with open("notes.json", "w") as f:
            json.dump(self.repository, f, indent=4, sort_keys=False, ensure_ascii=False, default=Note.to_json)

    def read(self):
        try:
            with (open('notes.json', 'r') as f):
                notes_data = json.load(f)
                for d in notes_data:
                    self.repository.append(Note(
                        title=d['title'],
                        text=d['message'],
                        uid=d['id'],
                        create_date=d['create_date']
                    ))
        except FileNotFoundError:
            with (open('notes.json', 'w') as f):
                pass

    def delete(self, note_id):
        if not note_id or len(note_id) < 8:
            return

        self.read()
        for note in self.repository:
            if note.get_id().startswith(note_id):
                self.repository.remove(note)
        self.save()
