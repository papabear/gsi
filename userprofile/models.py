from django.db import models
from django.contrib.auth.models import User, UserManager

#Advanced user model
class UserProfile(models.Model):
    url = models.URLField()
    home_address = models.TextField()
    user = models.ForeignKey(User, unique=True)
