from django.db import models

# Create your models here.
class Task(models.Model):
    status_choice = [
        ('PENDING' , 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]
    title = models.CharField(max_length=25),
    description = models.TextField,
    status = models.CharField(max_length=20,choices=status_choice ),

    