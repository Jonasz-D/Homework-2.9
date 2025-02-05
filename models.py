
from mongoengine import Document
from mongoengine.fields import DateTimeField, StringField, ReferenceField, ListField

class Author(Document):
    fullname = StringField()
    born_date = DateTimeField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField()

