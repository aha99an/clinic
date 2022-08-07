from django.db import models

# Create your models here.
class Referrer(models.Model):
    referrerName = models.CharField(max_length=255)

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.referrerName