from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Items(models.Model):
    seller = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    file = models.FileField(upload_to='file_uploads')

    def __str__(self):
        return self.name
