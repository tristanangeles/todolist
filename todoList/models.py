from django.db import models

# Create your models here.

class Task(models.Model):
    #code
    title=models.CharField(max_length=30)
    description=models.TextField(max_length=500)
    start=models.DateTimeField()
    deadline=models.DateTimeField()
    
    
    def __str__(self):
        return self.title
    

