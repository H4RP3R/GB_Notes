import argparse

from note import Note
from note_storage import NoteStorage
from help_message import msg


class App:

    def __init__(self):
        self.storage = NoteStorage()

    def run(self):
        parser = argparse.ArgumentParser(description='A command line utility to store notes', usage=msg)
        choices = ['add', 'list', 'delete', 'update']
        parser.add_argument('command', help='add new note, list all notes, delete note, update note', choices=choices)
        parser.add_argument('-t', '--title', metavar='', type=str, help='note title', default='No title')
        parser.add_argument('-m', '--msg', metavar='', type=str, help='note text', default='Empty note')
        parser.add_argument('-i', '--id', metavar='', type=str, help='note id')
        args = parser.parse_args()

        match args.command:
            case 'add':
                self.add(args)
            case 'list':
                self.print_all()
            case 'delete':
                self.delete(args)
            case 'update':
                self.update(args)

    def add(self, args):
        note = Note(title=args.title, text=args.msg)
        self.storage.add(note)
        self.storage.save()

    def print_all(self):
        self.storage.read()
        for note in self.storage.repository:
            print(note)

    def delete(self, args):
        self.storage.delete(args.id)

    def update(self, args):
        self.storage.update(args)


if __name__ == "__main__":
    app = App()
    app.run()
