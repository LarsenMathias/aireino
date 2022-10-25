from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-date_added']
