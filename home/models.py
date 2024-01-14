from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    

class project(models.Model):
    project_title = models.CharField(max_length=50)
    project_text = models.TextField()
    