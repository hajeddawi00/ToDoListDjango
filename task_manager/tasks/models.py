from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50)
    is_completed = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    