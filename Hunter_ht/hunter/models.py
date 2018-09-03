from django.db import models
# Create your models here.
class User(models.Model):
    userID = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    nake_name = models.CharField(max_length=50)
