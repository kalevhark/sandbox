from django.db import models

class Feedback(models.Model):
    feedback_name = models.CharField(max_length=30)
    feedback_contact = models.CharField(max_length=30, blank=True)
    feedback_text = models.CharField(max_length=30)
