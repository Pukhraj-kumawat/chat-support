from django.db import models

class WhatsAppMessage(models.Model):
    STATUS_CHOICES = [
        ('sent', 'Sent'),
        ('received', 'Received'),
        ('failed', 'Failed'),
    ]

    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def __str__(self):
        return f"From {self.sender} to {self.receiver}: {self.content[:20]}"