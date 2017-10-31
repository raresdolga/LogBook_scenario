from django.db import models


class User(models.Model):
    firstName = models.CharField(max_length=140)
    lastName = models.CharField(max_length=140)
    email = models.EmailField()
    password = models.CharField(max_length=140)



class Log(models.Model):
    title = models.TextField();
    body = models.TextField();
    userId = models.CharField(max_length=140)
