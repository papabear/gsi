from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    status = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.status

#Project model. eh...
class Project(models.Model):
    proj_number = models.IntegerField()
    proj_name = models.CharField(max_length=200)
    users = models.ManyToManyField(User, verbose_name="list of users")
    status = models.ForeignKey(Status)
    
    def __unicode__(self):
        return self.proj_name
    
#Pushlist model. duh!
class Pushlist(models.Model):
    list = models.TextField()
    project = models.ForeignKey(Project)
    