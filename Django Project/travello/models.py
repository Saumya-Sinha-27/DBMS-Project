from django.db import models
from django.contrib.auth.models import User, auth
# Create your models here.

class destination(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class Desti(models.Model):

    dest_id = models.ForeignKey(destination, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)