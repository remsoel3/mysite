from django.db import models
from mongoengine import *
# Create your models here.
class Peliculas(Document):
    nombre = StringField(max_length=200)
    genero = StringField(max_length=200)
    año = StringField(max_length=200)
    

# from yourproject.models import Poll, Choice

# poll = Poll.objects(question__contains="What").first()
# choice = Choice(choice_text="I'm at DjangoCon.fi", votes=23)
# poll.choices.append(choice)
# poll.save()

# print poll.question
# 
