from django.db import models
from datetime import datetime

# Create your models here.
class Task(models.Model):
    Title = models.CharField(max_length=50 , default="No title" , blank=False)
    Description = models.TextField(blank=False , null=False)
    Date = models.DateTimeField(default=datetime.now)
    image = models.ImageField(default="no image" , upload_to="images/")
    video = models.FileField(default="no video"  , upload_to="videos/")