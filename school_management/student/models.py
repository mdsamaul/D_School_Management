from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name="Student Name")
    roll=models.IntegerField(unique=True)
    father_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return (f'{self.name} - {self.roll}')