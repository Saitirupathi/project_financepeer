from django.db import models

# Create your models here.
class Upload(models.Model):
    file=models.FileField()

class DisplayItems(models.Model):
    userId=models.IntegerField()
    title=models.CharField(max_length=256)
    body=models.CharField(max_length=1024)    
