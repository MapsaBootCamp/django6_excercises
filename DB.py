
from enum import unique
from typing_extensions import Required
from mongoengine import *
from mongoengine.connection import connect
from mongoengine.document import Document
from mongoengine.fields import StringField

connect('Resturant')




class Singleton(type):
    _instanse = None
    
    def __call__(self, *args, **kwargs):
        if self._instanse is None:
            self._instance = super().__call__
        return self._instanse

class DB(Document, metaclass=Singleton):
    pass
