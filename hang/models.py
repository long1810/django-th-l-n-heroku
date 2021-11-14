from django.db import models

# Create your models here.
class Post(models.Model):
    mah = models.CharField(max_length=100)
    ten = models.TextField()
    ngaynhap = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)
    gia = models.IntegerField()
    so = models.IntegerField()
    
    