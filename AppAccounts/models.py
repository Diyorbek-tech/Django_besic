from django.db import models

# Create your models here.

class Teacher(models.Model):
    name=models.CharField(max_length=30)
    skill=models.CharField(max_length=100)
    age=models.IntegerField()
    biography=models.TextField()
    images=models.ImageField()

    def __str__(self):
        return self.name
