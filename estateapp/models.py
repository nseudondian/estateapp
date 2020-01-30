from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class emergency(models.Model):
    name = models.CharField(max_length=20)
    Phone = models.CharField(max_length=15)
    Maritalstatus = models.TextField()
    StateOfOrigin = models.TextField
    Block = models.CharField(max_length=10)
    lease_period = models.DurationField
        
    
    def __str__(self):
        return self.name
    
    
    
    
    
