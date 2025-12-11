from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Resource(models.Model):
    RESOURCE_TYPE_CHOICES = (
        ('Article', 'Article'),
        ('Video', 'Video'),
        ('PDF', 'PDF'),
        ('Other', 'Other'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    resource_type = models.CharField(max_length=50, choices=RESOURCE_TYPE_CHOICES)
    url = models.URLField(blank=True, null=True)      # for videos/articles
    file = models.FileField(upload_to='resources/', blank=True, null=True)  # for PDFs
    created_by = models.ForeignKey(User, related_name='resources', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=255, blank=True, null=True)  # optional comma-separated tags

    def __str__(self):
        return f"{self.title} ({self.resource_type})"
