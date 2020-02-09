from django.db import models

# Create your models here.
class Loan(models.Model):
    title = models.TextField()
    userID = models.TextField()
    
    