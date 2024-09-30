from django.db import models

class Complaint(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    complaint_text = models.TextField()
    sentiment = models.CharField(max_length=50, blank=True, null=True)
    image_classification = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint by {self.name}"