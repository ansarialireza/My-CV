from django.db import models

class UserProfile(models.Model):
    full_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    job = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)  # Adjust max_length as needed

    def __str__(self):
        return self.full_name
