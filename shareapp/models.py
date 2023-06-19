from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    type = models.CharField(max_length=10, choices=[('text', 'Text'), ('audio', 'Audio'), ('video', 'Video')])
    created_at = models.DateTimeField(auto_now_add=True)
    shared_with = models.ManyToManyField(User, related_name='shared_notes')
    file_name=models.FileField(upload_to="", default="")
    def __str__(self) -> str:
        return self.content