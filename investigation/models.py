from django.db import models

# Create your models here.
class Investigation(models.Model):
    investigationName = models.CharField(max_length=255)

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.investigationName