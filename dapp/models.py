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

class OrderDetail(models.Model):
    customer_email= models.EmailField()
    item = models.ForeignKey(Items,on_delete=models.CASCADE)
    amount = models.IntegerField()
    stripe_payment_intent = models.CharField(max_length=200,null=True)
    has_paid = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
