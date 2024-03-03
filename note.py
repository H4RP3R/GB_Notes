import json
import uuid
from datetime import datetime


class Note():

    def __init__(self, title, text):
        self.__id = uuid.uuid4()
        self.__create_date = datetime.now()
        self.__title = title
        self.__text = text

    def __str__(self):
        time_fmt = self.__create_date.strftime("%m.%d.%Y %H:%M:%S")
        delimiter = '=' * 50
        return f'{self.__title.upper()}\n {self.__text}\nid: {str(self.__id)[:8]}... | created: {time_fmt}\n{delimiter}'

    def to_json(self):
        return {
            'id': str(self.__id),
            'create_date': self.__create_date.strftime("%m.%d.%Y %H:%M:%S"),
            'title': self.__title,
            'body': self.__text,
        }
