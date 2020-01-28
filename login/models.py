from django.db import models

class user(models.Model):
    institution = models.CharField(max_length=200,default="foobar")
    teamlogin = models.CharField(max_length=200,default="foobar")
    teampassword = models.TextField(max_length=200,default="foobar")
