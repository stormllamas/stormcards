from django.db import models
from datetime import datetime

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    # This allows the post titles to be defined as named
    def __str__(self):
        return self.title
    # This disables the pluralization of the model Posts by defining a plural form of the model posts as posts
    class Meta:
        verbose_name_plural = "Posts"