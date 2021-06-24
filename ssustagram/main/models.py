from django.db import models

# Create your models here.

class feed(models.Model):
    mainphoto=models.ImageField(blank=True,null=True)
    content=models.TextField()
    create_date=models.DateTimeField()