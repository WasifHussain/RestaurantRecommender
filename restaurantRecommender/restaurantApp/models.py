from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    alcohol = models.CharField(max_length=50,blank=True, null=True)
    smoking_area = models.CharField(max_length=50,blank=True, null=True)
    dresscode = models.CharField(max_length=50,blank=True, null=True)
    accessibility = models.CharField(max_length=50,blank=True, null=True)
    price = models.CharField(max_length=10)
    ambience = models.CharField(max_length=50,blank=True, null=True)
    area = models.CharField(max_length=50,blank=True, null=True)
    other_services = models.TextField(max_length=100,blank=True, null=True)
    favorite = models.ManyToManyField(User, related_name='favorite')

    def __str__(self):
        return self.name

class Review(models.Model):
    review = models.TextField(max_length=200,blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='restaurant')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
