from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class User(models.Model):
    userID = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    pwd = models.CharField(max_length=100)
    nake_name = models.CharField(max_length=100)
    identity = models.CharField(max_length=1, default='0')
    introduction = models.TextField(default="No Information")

class Publications(models.Model):
    pubID = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    authors = models.CharField(max_length=1000)
    messages = models.CharField(max_length=100, default='no information')
    publishType = models.CharField(max_length=100,default=' ')
    journalname=models.CharField(max_length=1000,default=' ')
    date =  models.DateField(default=timezone.now)
    indexType = models.CharField(max_length=100,default=' ')
    uploadByUser = models.CharField(max_length=50,default='no records')
    isOpen = models.CharField(max_length=5,default='1')

class PubToUser(models.Model):
    pubID = models.BigIntegerField()
    username = models.CharField(max_length=50)

class Articles(models.Model):
    articleID = models.BigIntegerField(primary_key=True)
    authorID = models.IntegerField()
    title = models.CharField(max_length=500,default=' ')
    content = models.TextField()
    publish = models.CharField(max_length=5,default='0')
    editDateTime = models.DateField(default=datetime.datetime.now().date())
    isPrivate=models.CharField(max_length=5,default='0')