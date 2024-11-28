# childapp/models.py
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.URLField()

    def __str__(self):
        return self.title

class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    rights_description = models.TextField()
    content = models.TextField()
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='child_videos', null=True, blank=True)

    def __str__(self):
        return self.name
