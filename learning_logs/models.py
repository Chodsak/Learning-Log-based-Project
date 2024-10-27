from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Returned a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Content related to the topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField(max_length=3000)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ to use entries instead of entrys when it needs to refer to more than one entry"""
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text) < 50:
            return self.text
        else:
            return f"{self.text[:50]}..."
