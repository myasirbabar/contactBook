from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True, null=False)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username
