from datetime import datetime
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

    def update(self, args):
        if not args.id or len(args.id) < 8:
            return

        self.read()
        for note in self.repository:
            if note.get_id().startswith(args.id):
                if args.title != 'No title':
                    note.set_title(args.title)
                if args.msg != 'Empty note':
                    note.set_text(args.msg)
        self.save()

    def date_filter(self, date_str):
        try:
            datetime_obj = datetime.strptime(date_str, "%m.%d.%Y").date()
        except (ValueError, TypeError):
            return

        self.read()
        filtered_notes = []
        for note in self.repository:
            note_date = datetime.strptime(note.get_create_date(), "%m.%d.%Y %H:%M:%S").date()
            if note_date == datetime_obj:
                filtered_notes.append(note)

        return filtered_notes

    def select_one_note(self, note_id):
        self.read()
        for note in self.repository:
            if note.get_id().startswith(note_id):
                return note
