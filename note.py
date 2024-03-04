import uuid
from datetime import datetime


class Note():

    def __init__(self, title, text, uid=str(uuid.uuid4()), create_date=datetime.now().strftime("%m.%d.%Y %H:%M:%S")):
        self.__id = uid
        self.__create_date = create_date
        self.__title = title.upper()
        self.__text = text

    def __str__(self):
        delimiter = '=' * 50
        return f'\n{self.__title}\n {self.__text}\nid: {self.__id[:8]}... created: {self.__create_date}\n{delimiter}'

    def get_id(self):
        return self.__id

    def to_json(self):
        return {
            'id': self.__id,
            'create_date': self.__create_date,
            'title': self.__title,
            'message': self.__text,
        }
