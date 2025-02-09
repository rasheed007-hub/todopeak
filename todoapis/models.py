from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title