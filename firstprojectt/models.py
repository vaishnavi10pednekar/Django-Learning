from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length = 120)
    is_completed = models.BooleanField(default = False) 

    def __str__(self):
        return self.task
    
class Information(models.Model):
    First_Name = models.CharField(max_length=50)
    SurName = models.CharField(max_length=50)
    Age = models.IntegerField()
    Date_of_birth = models.DateField()
    Gender = models.CharField(max_length=1)

    def __str__(self):
        return self.First_Name