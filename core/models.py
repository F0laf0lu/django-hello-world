from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


    class Report(models.Model):
        STATUS_CHOICES = [
            ('lost', 'Lost'),
            ('found', 'Found'),
        ]
        title = models.CharField(max_length=255)
        description = models.TextField()
        image = models.ImageField(upload_to='upload/', null=True)
        location = models.ForeignKey(Location, on_delete=models.CASCADE)
        date_reported = models.DateField(auto_now_add=True)
        phone_number = models.CharField(max_length=11)
        status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='lost')
        reporter = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title