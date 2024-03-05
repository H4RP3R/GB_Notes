import argparse

from note import Note
from note_storage import NoteStorage
from help_message import *


class App:

    def __init__(self):
        self.storage = NoteStorage()

    def run(self):
        parser = argparse.ArgumentParser(description='Command line note-taking utility', usage=usage_msg)
        choices = ['add', 'list', 'delete', 'update', 'filter', 'show']
        parser.add_argument('command', choices=choices, help=help_msg)
        parser.add_argument('-t', '--title', metavar='', type=str, help='note title', default='No title')
        parser.add_argument('-m', '--msg', metavar='', type=str, help='note message', default='Empty note')
        parser.add_argument('-i', '--id', metavar='', type=str, help='note id')
        parser.add_argument('-d', '--date', metavar='', type=str, help='date for filter')
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
            case 'filter':
                self.date_filter(args)
            case 'show':
                self.select_one_note(args)

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

    def date_filter(self, args):
        filtered_notes = self.storage.date_filter(args.date)
        if filtered_notes:
            for note in filtered_notes:
                print(note)

    def select_one_note(self, args):
        note = self.storage.select_one_note(args.id)
        if note:
            print(note)


if __name__ == "__main__":
    app = App()
    app.run()
