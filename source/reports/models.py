from profiles.models import Profiles
from django.db import models

class Report(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='reports', default='default.png')
    remarks = models.TextField()
    author = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name