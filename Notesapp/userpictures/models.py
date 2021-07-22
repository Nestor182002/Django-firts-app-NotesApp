from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class pictureUser(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    pictures =  models.ImageField(upload_to = 'gallery')

    
    
