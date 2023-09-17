from django.db import models

class ContactSubmission(models.Model):
    contactName = models.CharField(max_length=100)
    contactEmail = models.EmailField(max_length=100)
    contactSubject = models.CharField(max_length=100, blank=True)
    contactMessage = models.TextField()