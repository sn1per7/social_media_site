from django.db import models
from datetime import date
from django.contrib.auth.models import User
from mongoengine import *
from permitted.settings import DBNAME


connect(DBNAME)


class Person(Document):
    username = StringField(max_length=100, required=True, default="")
    email = StringField(max_length=100, required=True, default="")
    password = StringField(max_length=100, required=True, default="")

    def __str__(self):
        return self.username + " -> " + self.email


class Userinfo(Document):
    email = ReferenceField(Person)
    firstName = StringField(max_length=200, required=True, default="")
    lastName = StringField(max_length=200, required=True, default="")
    gender = StringField(max_length=2, required=True, default="")
    mobileNumber = StringField(max_length=200, required=True, default="")
    job = StringField(max_length=200, required=True, default="")
    bio = StringField(max_length=500, required=True, default="")
    hometown = StringField(max_length=200, required=True, default="")
    currentCity = StringField(max_length=200, required=True, default="")
    education = StringField(max_length=200, required=True, default="")
    profilePic = FileField()

    def __str__(self):
        return self.firstName + " -> " + self.email


class Chatbox(Document):
    sender = StringField(max_length=200, required=True, default="")
    receiver = StringField(max_length=200, required=True, default="")
    message = StringField(max_length=1000, required=True, default="")

    def __str__(self):
        return self.sender + " -> " + self.message
