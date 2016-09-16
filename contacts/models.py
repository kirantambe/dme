from __future__ import unicode_literals

# from django.db import models
from mongoengine import *
# Create your models here.


class Option(EmbeddedDocument):
    num = IntField()
    image_url = URLField()
    name = StringField()
    answer_count = IntField()


class Question(EmbeddedDocument):
    type = StringField(choices=('single_answer', 'multi_answer'))
    question = StringField()
    count = IntField()
    options = EmbeddedDocumentListField(Option)
    correct_answer = ListField()


class Feed(Document):
    type_code = IntField()
    quiz_id = StringField()
    questions = EmbeddedDocumentListField(Question)