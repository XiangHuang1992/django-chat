""" Models for the chat app """
from uuid import uuid4

from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


def deserialize_user(user):
    """ 反序列化user --> json """
    return{
        "id": user.id, "username": user.username, "email": user.email,
        "first_name": user.first_name, "last_name": user.last_name
    }

