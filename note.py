import uuid
from datetime import datetime


class Note():

    def __init__(self, title, text, uid=str(uuid.uuid4()), create_date=datetime.now().strftime('%m.%d.%Y %H:%M:%S')):
        self.__id = uid
        self.__create_date = create_date
        self.__title = title
        self.__text = text

    def __str__(self):
        title = self.__title.upper()
        delimiter = '=' * 50
        id_part = self.__id[:8]
        return f'\n{title}\n{self.__text}\nid: {id_part}... created: {self.__create_date}\n{delimiter}'

    def get_id(self):
        return self.__id

    def get_create_date(self):
        return self.__create_date

    def set_title(self, new_title):
        self.__title = new_title
        self.update_create_date()

    def set_text(self, new_text):
        self.__text = new_text
        self.update_create_date()

    def to_json(self):
        return {
            'id': self.__id,
            'create_date': self.__create_date,
            'title': self.__title,
            'message': self.__text,
        }

    def update_create_date(self):
        self.__create_date = datetime.now().strftime('%m.%d.%Y %H:%M:%S')
