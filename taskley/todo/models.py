from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
<<<<<<< HEAD
    title = models.CharField(max_length=100, null=True)

    content = models.CharField(max_length=1000, null=True, blank=True)

    date_pasted = models.DateTimeField(auto_now_add=True, null=True)

    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)
    
=======
    Title = models.CharField(max_length=85)
    
    content = models.CharField(max_length=300)
    
    date_posted = models.DateField( auto_now_add=True)
    
class Review(models.Model):
    Reviewer_name = models.CharField(max_length=85)
    Reviewer_title = models.CharField(max_length=100)
    
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
>>>>>>> 13320a8cfb700ff61ead02ac4813c3586e27629e
