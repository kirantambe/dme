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


class User(Document):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = EmailField(required=True)
    google_id = StringField(required=True)
    height = IntField()
    weight = IntField()
    dob = DateTimeField(required=True)
    gender = StringField(choices=('male', 'female'))
    workout_preference = StringField(choices=('get fit', 'weight loss', 'muscle building'))
    meal_preference = StringField(choices=('veg', 'non veg', 'eggetarian', 'jain'))