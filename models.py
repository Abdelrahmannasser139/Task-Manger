from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Only use auto_now_add

    def __str__(self):
        return self.name
